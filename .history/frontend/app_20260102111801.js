/* =========================
   INITIAL SETUP
========================= */

// Temporary username (later replaced with auth)
const username = "You";

// DOM references
const messagesContainer = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const typingIndicator = document.getElementById("typingIndicator");

// Socket connection (backend will listen on this)
const socket = io("http://localhost:5000");

/* =========================
   SOCKET EVENTS
========================= */

// Join event
socket.emit("join", { username });

// Incoming message
socket.on("message", (data) => {
    appendMessage(data.text, "left");
});

// Status updates (join/leave)
socket.on("status", (data) => {
    appendSystemMessage(data.msg);
});

// Typing indicator
socket.on("typing", () => {
    showTypingIndicator();
});

/* =========================
   MESSAGE HANDLING
========================= */

function appendMessage(text, side) {
    const msg = document.createElement("div");
    msg.classList.add("message", side);
    msg.textContent = text;

    messagesContainer.appendChild(msg);
    autoScroll();
}

function appendSystemMessage(text) {
    const msg = document.createElement("div");
    msg.classList.add("message", "left");
    msg.style.opacity = "0.6";
    msg.textContent = text;

    messagesContainer.appendChild(msg);
    autoScroll();
}

function autoScroll() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

/* =========================
   SEND MESSAGE
========================= */

sendBtn.addEventListener("click", sendMessage);

messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
    socket.emit("typing");
});

function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    appendMessage(text, "right");

    socket.emit("message", {
        user: username,
        text: text
    });

    messageInput.value = "";
}

/* =========================
   TYPING INDICATOR
========================= */

let typingTimeout;

function showTypingIndicator() {
    typingIndicator.style.opacity = "1";

    clearTimeout(typingTimeout);
    typingTimeout = setTimeout(() => {
        typingIndicator.style.opacity = "0";
    }, 1200);
}
