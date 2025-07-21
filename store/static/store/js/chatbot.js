// chatbot.js
document.addEventListener('DOMContentLoaded', function () {
  const chatIcon = document.createElement('div');
  chatIcon.id = 'chatbot-icon';
  chatIcon.innerText = '💬';
  document.body.appendChild(chatIcon);

  const chatWindow = document.createElement('div');
  chatWindow.id = 'chatbot-window';
  chatWindow.style.display = 'none';  // ✅ Fixes auto-open issue
  chatWindow.innerHTML = `
    <div id="chatbot-header">Support Assistant <span id="chatbot-close">✖</span></div>
    <div id="chatbot-messages"></div>
    <input id="chatbot-input" placeholder="Ask me anything..." />
  `;
  document.body.appendChild(chatWindow);

  chatIcon.onclick = () => {
    chatWindow.style.display = 'block';
  };

  document.getElementById('chatbot-close').onclick = () => {
    chatWindow.style.display = 'none';
  };

  document.getElementById('chatbot-input').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      const msg = this.value;
      const messages = document.getElementById('chatbot-messages');
      messages.innerHTML += `<div class='user-msg'>${msg}</div>`;
      this.value = '';
      fetch(`/chatbot-response/?q=${encodeURIComponent(msg)}`)
        .then(res => res.json())
        .then(data => {
          messages.innerHTML += `<div class='bot-msg'>${data.response}</div>`;
          messages.scrollTop = messages.scrollHeight;
        });
    }
  });
});
