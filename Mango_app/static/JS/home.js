const hamburger=document.querySelector('.hamburger');
const navLinks =document.querySelector('.nav-links');
let menuOpen=false;

hamburger.addEventListener('click',()=>{
    if (menuOpen == false)
    {
        navLinks.style.display='block';
        menuOpen=true;
    }
    else if (menuOpen ==true)
    {
        navLinks.style.display="none";
        menuOpen=false;
    }
})

window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
      navLinks.style.display = 'flex'; 
      menuOpen = false; 
  } else if (!menuOpen) {
      navLinks.style.display = 'none'; 
  }
});

window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        navLinks.style.display = 'flex'; 
        menuOpen = false; 
    } else if (!menuOpen) {
        navLinks.style.display = 'none'; 
    }
  });
  let slideIndex = 1;
  showSlides(slideIndex);
  
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
  }