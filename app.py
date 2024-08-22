import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import Image
import google.generativeai as genai
from flask import Flask, render_template, Response, request, jsonify
import os

# Configure the generative AI model with your API key
genai.configure(api_key="AIzaSyASuLr7I0WDReo98aa2ELzDeEtAbbIFI8Y")
ai_model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

# Initialize the hand detector with specified parameters
hand_detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

previous_position = None
drawing_canvas = None

# Function to save the drawing as an image file
def save_drawing(canvas):
    if not os.path.exists('saved_drawings'):
        os.makedirs('saved_drawings')
    image = Image.fromarray(canvas)
    image.save("saved_drawings/hand_drawing.png")

# Function to send the drawing to an AI model
def analyze_drawing_with_ai(canvas):
    image = Image.fromarray(canvas)
    response = ai_model.generate_content(["Analyze this drawing:", image])
    return response.text

def generate_frames():
    global drawing_canvas, previous_position
    capture = cv2.VideoCapture(0)
    while True:
        # Read a frame from the webcam
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        if drawing_canvas is None:
            drawing_canvas = np.zeros_like(frame)
        
        # Detect hands and landmarks in the current frame
        hands, frame = hand_detector.findHands(frame, draw=False, flipType=True)
        if hands:
            # Extract the first detected hand's landmarks
            hand_data = hands[0]
            landmarks_list = hand_data["lmList"]
            fingers_up = hand_detector.fingersUp(hand_data)
            
            # Draw if the index finger is raised
            if fingers_up == [0, 1, 0, 0, 0]:
                current_position = landmarks_list[8][:2]
                if previous_position is not None:
                    # Draw on the canvas
                    cv2.line(drawing_canvas, tuple(previous_position), tuple(current_position), (0, 0, 255), 5)
                previous_position = current_position
            else:
                previous_position = None
            
            # Clear the canvas if the thumb and small finger is raised
            if fingers_up == [1, 0, 0, 0, 1]:
                drawing_canvas = np.zeros_like(drawing_canvas)

        # Overlay the drawing on the frame
        frame = cv2.addWeighted(frame, 1, drawing_canvas, 0.5, 0)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/save_drawing', methods=['POST'])
def save_drawing_route():
    global drawing_canvas
    if drawing_canvas is not None:
        save_drawing(drawing_canvas)
        return jsonify({"message": "Drawing saved successfully."})
    return jsonify({"message": "No drawing to save."})

@app.route('/analyze_drawing', methods=['POST'])
def analyze_drawing_route():
    global drawing_canvas
    if drawing_canvas is not None:
        analysis_result = analyze_drawing_with_ai(drawing_canvas)
        return jsonify({"analysis": analysis_result})
    return jsonify({"message": "No drawing to analyze."})

if __name__ == '__main__':
    app.run(debug=True)
