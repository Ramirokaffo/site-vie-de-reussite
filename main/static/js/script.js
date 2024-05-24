

sendMessage = async () => {
    const userName = document.getElementById("name-id");
    const userEmail = document.getElementById("email-id");
    const userMessage = document.getElementById("message-id");
    const sendMessageSpinner = document.getElementById("dot-spinner-message");
    // const sendMessageButton = document.getElementById("contact-submit-id");
    const sendMessageButtonText = document.getElementById("contact-submit-text");
    const messageUrl = document.getElementById("message-form-id").getAttribute("message_url");
    const csrfToken = document.querySelector('div[id="message-form-id"] input[name="csrfmiddlewaretoken"]').value;
    const dataToSend = { name: userName.value, email: userEmail.value, message: userMessage.value };
    
    if (userMessage.value.length == 0) {
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
        if (data["status"] = "1") {
            userName.value = "";
            userEmail.value = "";
            userMessage.value = "";
            UIkit.notification("Votre message a été envoyé avec succès !", {status:'success'})
        } else {
        UIkit.notification("Une erreur inconnue s'est produite", {status:'danger'})
        }
    })
    .catch((error) => {
        UIkit.notification("Désolé nous n'avons pas pu envoyé votre message...", {status:'danger'});
    });
    sendMessageButtonText.innerHTML = "Envoyer";
    sendMessageSpinner.style.visibility = "hidden"; 

}




window.onload = (event) => {



    submitBtn = document.getElementById("contact-submit-id");
    submitBtn.addEventListener("click", (event)=>{
        sendMessage();
    });


    welcomeEventModal = document.getElementById("welcomeEventModal")

    UIkit.modal(welcomeEventModal).show();
}



