// Get references to the UI elements
const recordBtn = document.getElementById("record-btn");
const stopBtn = document.getElementById("stop-btn");
const transcript = document.getElementById("transcript");
const submitBtn = document.getElementById("submit-btn");

// Add event listeners to the buttons
recordBtn.addEventListener("click", startRecording);
stopBtn.addEventListener("click", stopRecording);
submitBtn.addEventListener("click", submitTranscript);

// Initialize the speech recognition object
const recognition = new window.SpeechRecognition();
recognition.interimResults = true;

// Initialize the transcript variable
let finalTranscript = "";

// Define the startRecording function
function startRecording() {
    // Reset the transcript variable
    finalTranscript = "";

    // Start the recognition process
    recognition.start();

    // Disable the record button and enable the stop button
    recordBtn.disabled = true;
    stopBtn.disabled = false;

    // Update the UI
    transcript.value = "Recording...";
}

// Define the stopRecording function
function stopRecording() {
    // Stop the recognition process
    recognition.stop();

    // Enable the record button and disable the stop button
    recordBtn.disabled = false;
    stopBtn.disabled = true;

    // Update the UI
    transcript.value = finalTranscript;
}

// Define the submitTranscript function
function submitTranscript() {
    // Add code here to submit the transcript to the AI assistant program for processing
}

// Add event listeners to the speech recognition object
recognition.addEventListener("result", event => {
    const interimTranscript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join("");

    if (event.results[0].isFinal) {
        finalTranscript += interimTranscript;
    }

    transcript.value = finalTranscript;
});

recognition.addEventListener("end", () => {
    // If the recognition process was not stopped intentionally, start it again
    if (recordBtn.disabled) {
        recognition.start();
    }
});

// Add code here to establish a connection to the AI assistant program and handle responses from it
