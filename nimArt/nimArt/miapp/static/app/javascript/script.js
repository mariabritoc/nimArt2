window.addEventListener("scroll", function() {
  var footer = document.querySelector(".footer");
  var contentHeight = document.querySelector(".content").offsetHeight;
  var scrollPosition = window.innerHeight + window.pageYOffset;
  if (scrollPosition >= contentHeight) {
    footer.style.bottom = "0";
  } else {
    footer.style.bottom = "-60px";
  }
});