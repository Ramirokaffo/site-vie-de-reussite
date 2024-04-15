
class VideoComment {
    constructor(content) {
        this.content = content;
    }

    static fromMap(mapData){
        return new VideoComment(mapData["content"]);
    }



    getDOMComponent() {
        const myComment = document.createElement("div")
        myComment.innerHTML = `<div class="one-comment-div">
        <svg height="50" width="50" xmlns="http://www.w3.org/2000/svg" fill="var(--color3)"
            viewBox="0 0 24 24">
            <path fill-rule="evenodd"
                d="M12 20a8 8 0 0 1-5-1.8v-.6c0-1.8 1.5-3.3 3.3-3.3h3.4c1.8 0 3.3 1.5 3.3 3.3v.6a8 8 0 0 1-5 1.8ZM2 12a10 10 0 1 1 10 10A10 10 0 0 1 2 12Zm10-5a3.3 3.3 0 0 0-3.3 3.3c0 1.7 1.5 3.2 3.3 3.2 1.8 0 3.3-1.5 3.3-3.3C15.3 8.6 13.8 7 12 7Z"
                clip-rule="evenodd" />
        </svg>
        <div class="one-comment-div-right">
            <div class="one-comment-div-right-header">
                <h5>Vous</h5> 
                <i>maintenant</i>
            </div>
            <p>${this.content}</p>
            <hr>
        </div>
    </div>`;
    return myComment;
    }
}




sendComment = async (sendMessageSpinner) => {
    commentList = document.getElementById("comment-list")
    onComment = document.createElement("div")
    const userComment = document.getElementById("userComment");
    // sendMessageSpinner.style.display = "inline"; 

    const sendCommentButton = document.getElementById("sendCommentBtn");
    const messageUrl = document.getElementById("comment-form-id").getAttribute("message_url");
    const userId = document.getElementById("comment-form-id").getAttribute("userId");
    const videoId = document.getElementById("comment-form-id").getAttribute("videoId");
    const csrfToken = document.querySelector('div[id="comment-form-id"] input[name="csrfmiddlewaretoken"]').value;
    const dataToSend = { userComment: userComment.value, userId: userId, videoId: videoId };
    if (userComment.value.length == 0) {
        UIkit.notification("Veuillez renseigner le contenu de votre commentaire !", {status:'primary'})
        return;
    }
    sendCommentButton.innerHTML = "Envoie en cours...";
    sendMessageSpinner.style.display = "inline"; 


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
    if (data.status == "1") {
            userComment.value = "";
            const myComment = VideoComment.fromMap(data.comment);
            commentList = document.getElementById("comment-list")
            commentList.appendChild(myComment.getDOMComponent(), commentList.lastChild)
            UIkit.notification("Votre commentaire a été ajouté avec succès !", {status:'success'})
        } else {
        UIkit.notification("Une erreur inconnue s'est produite", {status:'danger'})
        }
    })
    .catch((error) => {
        // alert(error)
        UIkit.notification("Désolé nous n'avons pas pu ajouter votre commentaire...", {status:'danger'});
    });
    sendCommentButton.innerHTML = "Ajouter mon commentaire";
    sendMessageSpinner.style.display = "none"; 


}

showDescription = (commentBtn, descriptionBtn, commentDiv, videoDescription) => {
    descriptionBtn.classList.add("selected-tab");
    commentBtn.classList.remove("selected-tab");
    commentDiv.style.display = "none";
    videoDescription.style.display = "inline";
    

}


showComment = (commentBtn, descriptionBtn, commentDiv, videoDescription) => {
    commentBtn.classList.add("selected-tab");
    descriptionBtn.classList.remove("selected-tab");
    videoDescription.style.display = "none";
    commentDiv.style.display = "inline";

}


window.onload = (event) => {
const sendMessageSpinner = document.getElementById("dotSpinnerComment");

    submitBtn = document.getElementById("sendCommentBtn");
    submitBtn.addEventListener("click", (event)=>{
        sendComment(sendMessageSpinner);
    })

    
    videoDescription = document.getElementById("video-descriptiion");
    commentDiv = document.getElementById("comment-div");
    commentBtn = document.getElementById("commentBtnId");
    descriptionBtn = document.getElementById("descriptionBtn");

    descriptionBtn = document.getElementById("descriptionBtn");
    descriptionBtn.addEventListener("click", (event)=>{
        showDescription(commentBtn, descriptionBtn, commentDiv, videoDescription);
    })


    commentBtnId = document.getElementById("commentBtnId");
    shortcut_to_comment = document.getElementById("shortcut_to_comment");
    commentBtnId.addEventListener("click", (event)=>{
        showComment(commentBtn, descriptionBtn, commentDiv, videoDescription);
    })

    shortcut_to_comment.addEventListener("click", (event)=>{
        showComment(commentBtn, descriptionBtn, commentDiv, videoDescription);
    })


}






var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('video-id', {
    videoId: document.getElementById("video-id").getAttribute("yt_v_id"),
    playerVars: {
        "modestbranding": 1,
        "rel": 0,
        'showinfo': 0
      },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange,
      "onError": onErrorOccur
    }
  });

}

function onPlayerReady(event) {
    loader = document.getElementById("video-loader");
    loader.style.visibility = "hidden";
    
  event.target.playVideo();
}



function onErrorOccur(event) {
    loader = document.getElementById("video-loader");
    loader.style.visibility = "hidden";
    // for (const prop in event) {
    //     console.log(`Propriété : ${prop}`);
    //     console.log(`Valeur : ${event[prop]}`);
    //     console.log(`Type : ${typeof event[prop]}`);
    //     console.log("----------------");
    //   }
//   event.target.playVideo();
}

function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
        next_vdeo = document.getElementById("next-video-a");
        next_vdeo.click();
    }

}
function stopVideo() {
  player.stopVideo();
}



