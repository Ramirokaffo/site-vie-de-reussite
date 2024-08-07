// alert("Je suis")


const profileElement = document.getElementById('profile');
const mediaFileInput = document.getElementById('profilImage');
var userProfilUrl = document.getElementById('userProfilUrlId');
var editProfilIcon = document.getElementById('edit-profil-icon');


if (userProfilUrl) {
  userProfilUrl = userProfilUrl.getAttribute("userProfilUrl");
  profileElement.style.backgroundImage = `url(${userProfilUrl})`;
  profileElement.classList.add('hasImage');

}

// ----- On render -----
profileElement.classList.add('dragging');
profileElement.classList.remove('dragging');

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
      profileElement.style.backgroundImage = `url(${reader.result})`;
      profileElement.classList.add('hasImage');
    };
  }
});

// Handle profile click to open file input
profileElement.addEventListener('click', function () {
  mediaFileInput.click();
});

// Handle profile click to open file input
editProfilIcon.addEventListener('click', function () {
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
