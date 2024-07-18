
function isEmailValid(email) {
    const regex = /^(([^<>()[\]\\.,;:\s@"]+)(\.[^<>()[\]\\.,;:\s@"]+)*)@((([a-z0-9-\w]+\.)+[a-z]{2,}))$/i;
    return regex.test(email);
  }


sendComment = async () => {
    newsletter_input = document.getElementById("newsletter_input")
    const email = newsletter_input.value;
    const dataToSend = { email: email };
    if (newsletter_input.value.length == 0 || !isEmailValid(email)) {
        UIkit.notification("Veuillez entrer correctement votre adresse mail !", {status:'primary'})
        return;
    }

    await fetch("/newsletter/subscribe", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend),
  })
    .then((response) => response.json())
    .then((data) => {
    if (data.status == "1") {
        newsletter_input.value = "";
            UIkit.notification("La souscription a réussi", {status:'success'})
        } else if (data.status == "0") {
        newsletter_input.value = "";
            UIkit.notification("Vous êtes déjà inscrit à notre newsletter", {status:'warning'})
        } else {
            UIkit.notification("La suscription a échoué, veuillez reéssayer", {status:'danger'});
        }
    })
    .catch((error) => {
        UIkit.notification("La suscription a échoué, veuillez reéssayer", {status:'danger'});
    });

}


window.onload = (event) => {
    submitBtn = document.getElementById("subscribeBtn");
    submitBtn.addEventListener("click", (event)=>{
        sendComment();
    })

}








