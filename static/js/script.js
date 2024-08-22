// script.js

// script.js

document.getElementById('save-button').addEventListener('click', () => {
    fetch('/save_drawing', {method: 'POST'})
        .then(response => response.json())
        .then(data => alert(data.message));
});

document.getElementById('analyze-button').addEventListener('click', () => {
    fetch('/analyze_drawing', {method: 'POST'})
        .then(response => response.json())
        .then(data => {
            document.getElementById('analysis-result').textContent = data.analysis || data.message;
        });
});


function animateButton(buttonId) {
    const button = document.getElementById(buttonId);
    button.classList.add('clicked');
    setTimeout(() => button.classList.remove('clicked'), 500);
}
