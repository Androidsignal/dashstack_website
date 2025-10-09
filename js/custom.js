// tab and slider sync
const tabs = document.querySelectorAll(".vision-tab");
const dots = document.querySelectorAll(".vision-dot");
const slides = document.querySelector(".vision-slides");
let currentIndex = 0;

function updateSlide(index) {
  currentIndex = index;
  slides.style.transform = `translateX(-${index * 100}%)`;

  tabs.forEach((t) => t.classList.remove("active"));
  tabs[index].classList.add("active");

  dots.forEach((d) => d.classList.remove("active"));
  dots[index].classList.add("active");
}

tabs.forEach((tab) => {
  tab.addEventListener("click", () => updateSlide(Number(tab.dataset.index)));
});

dots.forEach((dot) => {
  dot.addEventListener("click", () => updateSlide(Number(dot.dataset.index)));
});

// Enhanced navigation with scroll effect
window.addEventListener("scroll", function () {
  const navbar = document.getElementById("mainNavbar");
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Close Bootstrap collapse when clicking outside (navbar collapse)
document.addEventListener("click", function (event) {
  const navbar = document.querySelector(".navbar");
  const collapseEl = document.querySelector(".navbar-collapse");
  if (!collapseEl) return;

  // If click isn't inside navbar and collapse is open, hide it
  if (!navbar.contains(event.target) && collapseEl.classList.contains("show")) {
    // Use Bootstrap Collapse API
    const collapse = bootstrap.Collapse.getOrCreateInstance(collapseEl);
    collapse.hide();
  }
});

// Animate elements on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
};

const observer = new IntersectionObserver(function (entries) {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = "1";
      entry.target.style.transform = "translateY(0)";
    }
  });
}, observerOptions);

//count on scroll
var counted = 0;
$(window).scroll(function () {
  var oTop = $("#counter").offset().top - window.innerHeight;
  if (counted == 0 && $(window).scrollTop() > oTop) {
    $(".count").each(function () {
      var $this = $(this),
        countTo = $this.attr("data-count");
      $({
        countNum: $this.text(),
      }).animate(
        {
          countNum: countTo,
        },

        {
          duration: 2000,
          easing: "swing",
          step: function () {
            $this.text(Math.floor(this.countNum));
          },
          complete: function () {
            $this.text(this.countNum);
            //alert('finished');
          },
        }
      );
    });
    counted = 1;
  }
});

// remove no-js class if JS is enabled
document.documentElement.classList.remove("no-js");
