

const profileElement = document.getElementById('profile');
const my_testimony_form = document.getElementById('my_testimony_form');
const submit_feedback_btn = document.getElementById('submit_feedback_btn');
const mediaFileInput = document.getElementById('profilImage');
var userProfilUrl = document.getElementById('userProfilUrlId');
if (userProfilUrl) {
  userProfilUrl = userProfilUrl.getAttribute("userProfilUrl");
  profileElement.style.backgroundImage = `url(${userProfilUrl})`;
  profileElement.classList.add('hasImage');

}

// ----- On render -----
profileElement.classList.add('dragging');
profileElement.classList.remove('dragging');

submit_feedback_btn.addEventListener('click', function (e) {
  e.preventDefault()

  if (mediaFileInput.files.length === 0 && !profileElement.style.backgroundImage) {
    UIkit.notification("Veuillez renseigner une photo de profil !", {status:'primary'})
  } else {
    my_testimony_form.submit();
  }

});

// Handle drag events
profileElement.addEventListener('dragover', function () {
  profileElement.classList.add('dragging');
});

profileElement.addEventListener('dragleave', function () {
  profileElement.classList.remove('dragging');
});

profileElement.addEventListener('drop', function (event) {
  profileElement.classList.remove('dragging', 'hasImage');

  if (event.dataTransfer) {
    const file = event.dataTransfer.files[0];
    mediaFileInput.files = event.dataTransfer.files;
    const reader = new FileReader();

    // Attach event handlers here...

    reader.readAsDataURL(file);
    reader.onload = function (event) {
      console.log(reader.result);
      profileElement.style.backgroundImage = `url(${reader.result})`;
      profileElement.classList.add('hasImage');
    };
  }
});

// Handle profile click to open file input
profileElement.addEventListener('click', function () {
  mediaFileInput.click();
});

// Handle file input change
mediaFileInput.addEventListener('change', function (event) {
  const input = event.target;
  if (input.files && input.files[0]) {
    const file = input.files[0];

    const reader = new FileReader();

    reader.readAsDataURL(file);
    reader.onload = function (event) {
      console.log(reader.result);
      profileElement.style.backgroundImage = `url(${reader.result})`;
      profileElement.classList.add('hasImage');
    };
  }
});

// Prevent default behavior for global drag events (optional)
window.addEventListener("dragover", function (event) {
  event.preventDefault();
}, false);

window.addEventListener("drop", function (event) {
  event.preventDefault();
}, false);
