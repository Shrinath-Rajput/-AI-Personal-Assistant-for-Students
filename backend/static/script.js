// MARKS PREDICTION
function predict() {
    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            hours: document.getElementById("hours").value,
            attendance: document.getElementById("attendance").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "📈 Marks: " + data.marks;
    })
    .catch(err => console.error(err));
}


// RESUME UPLOAD
function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file!");
        return;
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        const text = e.target.result;

        fetch("/resume", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({resume: text})
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("resumeResult").innerText =
                "📄 Score: " + data.score + "%";
        });
    };

    reader.readAsText(file);
}


// CHATBOT
function sendMessage() {
    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            message: document.getElementById("chatInput").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chatResult").innerText =
            "🤖 " + data.reply;
    })
    .catch(err => console.error(err));
}