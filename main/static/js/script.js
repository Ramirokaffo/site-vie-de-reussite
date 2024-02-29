

sendMessage = async () => {
    const userName = document.getElementById("name-id").value;
    const userEmail = document.getElementById("email-id").value;
    const userMessage = document.getElementById("message-id").value;
    const sendMessageSpinner = document.getElementById("dot-spinner-message");
    // const sendMessageButton = document.getElementById("contact-submit-id");
    const sendMessageButtonText = document.getElementById("contact-submit-text");
    const messageUrl = document.getElementById("message-form-id").getAttribute("message_url");
    const csrfToken = document.querySelector('div[id="message-form-id"] input[name="csrfmiddlewaretoken"]').value;
    const dataToSend = { name: userName, email: userEmail, message: userMessage };
    
    if (userMessage.length == 0) {
        UIkit.notification("Veuillez renseigner le contenu de votre message !", {status:'primary'})
        return;
    }
    sendMessageButtonText.innerHTML = "Envoie en cours...";
    sendMessageSpinner.style.visibility = "visible"; 
    await fetch(messageUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(dataToSend),
  })
    .then((response) => response.json())
    .then((data) => {
        UIkit.notification("Votre message a été envoyé avec succès !", {status:'success'})
    })
    .catch((error) => {
        UIkit.notification("Désolé nous n'avons pas pu envoyé votre message...", {status:'danger'})
    });
    sendMessageButtonText.innerHTML = "Envoyer";
    sendMessageSpinner.style.visibility = "hidden"; 
}


window.onload = (event) => {
    submitBtn = document.getElementById("contact-submit-id");
    submitBtn.addEventListener("click", (event)=>{
        sendMessage();
    })
}



