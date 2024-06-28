


window.onscroll = function() {
    myFunction();
    scrollFunction();
};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}


// When the user scrolls down 20px from the top of the document, show the button
// window.onscroll = function() {};

function scrollFunction() {
let mybutton = document.getElementById("myScrollToTopBtn");

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "flex";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

const site_cookies_div = document.getElementById("site_cookies_div")
const agree_coockies_btn = document.getElementById("agree_coockies_btn")

agree_coockies_btn.addEventListener("click", (event) => {
  site_cookies_div.style.display = "none";
  document.cookie = 'cookie_accepted=true';
  // sessionStorage.setItem("cookie_accepted", "true");
})