document.addEventListener("DOMContentLoaded", () => {
    const burger = document.getElementById("burger");
    const navLinks = document.getElementById("nav-links");
  
    burger.addEventListener("click", () => {
      navLinks.classList.toggle("show");
    });
  });
  
document.addEventListener("DOMContentLoaded", function () {
    const scrollable = document.querySelector(".skills-scrollable");
    const leftButton = document.querySelector(".left-btn");
    const rightButton = document.querySelector(".right-btn");

    leftButton.addEventListener("click", () => {
      scrollable.scrollBy({ left: -200, behavior: "smooth" });
    });

    rightButton.addEventListener("click", () => {
      scrollable.scrollBy({ left: 200, behavior: "smooth" });
    });
  });
  
document.addEventListener("DOMContentLoaded", function () {
  const samples = document.querySelector(".projects-samples");
  const projects = document.querySelectorAll(".projeckko");
  const leftButton = document.querySelector(".project-left-btn");
  const rightButton = document.querySelector(".project-right-btn");

  let currentIndex = 0;

  // Function to update the visible project
  function updateSlider(index) {
    // Calculate the transform based on the index
    const translateXValue = -index * 100; // Move by 100% of the container width
    samples.style.transform = `translateX(${translateXValue}%)`;
  }

  // Event listeners for buttons
  leftButton.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + projects.length) % projects.length; // Loop back to the last project if going left from the first
    updateSlider(currentIndex);
  });

  rightButton.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % projects.length; // Loop to the first project if going right from the last
    updateSlider(currentIndex);
  });

  // Initialize slider
  updateSlider(currentIndex);
});
