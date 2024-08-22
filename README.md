# 🎨 Real-Time Hand Gesture Drawing & AI Analysis

A Python-based project enabling real-time drawing through hand gestures captured by a webcam. The drawings are then analyzed using a generative AI model for insightful feedback.

## 🚀 Features
- **Hand Gesture Recognition**: Use hand movements and finger gestures to draw on a virtual canvas.
- **AI-Powered Drawing Analysis**: Leverage Google's Generative AI to analyze the drawings and provide interpretations.
- **Gesture-Based Controls**: Clear the canvas, save drawings, and trigger AI analysis with specific hand gestures.

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ravi2196/hand-gesture-drawing-ai.git
   cd hand-gesture-drawing-ai

2. **Install Required Packages**
    

3. **Configure Google Generative AI**
Obtain an API key from Google and set it up in your script:
        genai.configure(api_key="YOUR_API_KEY_HERE")

## 🎨 How It Works

1. **Run the Application**
        python hand_gesture_drawing.py

2. **Gesture Controls**
    **- Draw:** Raise the index finger to draw.
    **- Clear Canvas:** Raise the thumb and small finger to clear the canvas.
    **- Save & Analyze:** Raise all fingers except the thumb to save the drawing and send it to the AI for analysis.

3. **Exit**
    Press '**q**' to close the application.

## 📚 Dependencies

    - OpenCV
    - NumPy
    - Pillow
    - cvzone
    - Google Generative AI

Install all dependencies with:
    pip install opencv-python-headless numpy pillow cvzone google-generativeai

## 🎯 Project Objectives

    - Implement real-time hand tracking for creative applications.
    - Explore the integration of gesture-based drawing with generative AI models.

## 🤝 Contributing

    Contributions are welcome! Fork this repository, submit issues, or make pull requests.

## 📧 Contact

    For any questions or feedback, feel free to reach out at rshankar0901@gmail.com.