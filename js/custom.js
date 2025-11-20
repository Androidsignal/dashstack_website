// tab and slider sync
// const tabs = document.querySelectorAll(".vision-tab");
// const dots = document.querySelectorAll(".vision-dot");
// const slides = document.querySelector(".vision-slides");
// let currentIndex = 0;

// function updateSlide(index) {
//   currentIndex = index;
//   slides.style.transform = `translateX(-${index * 100}%)`;

//   tabs.forEach((t) => t.classList.remove("active"));
//   tabs[index].classList.add("active");

//   dots.forEach((d) => d.classList.remove("active"));
//   dots[index].classList.add("active");
// }

// tabs.forEach((tab) => {
//   tab.addEventListener("click", () => updateSlide(Number(tab.dataset.index)));
// });

// dots.forEach((dot) => {
//   dot.addEventListener("click", () => updateSlide(Number(dot.dataset.index)));
// });


// new slider code
// tab, dot, nav + auto-scroll sync
const slidesEl = document.querySelector(".vision-slides");
let currentIndex = 0;

function $tabs() { return Array.from(document.querySelectorAll(".vision-tab")); }
function $dots() { return Array.from(document.querySelectorAll(".vision-dot")); }
function slideCount() { return document.querySelectorAll(".vision-slide").length; }

function updateSlide(index) {
  const total = slideCount();
  currentIndex = ((index % total) + total) % total; // wrap both ways

  // move slides
  slidesEl.style.transform = `translateX(-${currentIndex * 100}%)`;

  // tabs state
  const tabs = $tabs();
  tabs.forEach(t => t.classList.remove("active"));
  if (tabs[currentIndex]) tabs[currentIndex].classList.add("active");

  // dots state
  const dots = $dots();
  dots.forEach(d => d.classList.remove("active"));
  if (dots[currentIndex]) dots[currentIndex].classList.add("active");

  // auto-scroll active tab into view (when overflowing)
  // const activeTab = document.querySelector(`.vision-tab[data-index="${currentIndex}"]`);
  // if (activeTab) activeTab.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
}

//function goTo(delta) { updateSlide(currentIndex + delta); }

// Event delegation for tabs (works if tabs are added later)
document.querySelector(".vision-tabs").addEventListener("click", (e) => {
  const tab = e.target.closest(".vision-tab");
  if (!tab) return;
  updateSlide(Number(tab.dataset.index));
});

// Event delegation for dots
// document.querySelector(".vision-dots").addEventListener("click", (e) => {
//   const dot = e.target.closest(".vision-dot");
//   if (!dot) return;
//   updateSlide(Number(dot.dataset.index));
// });

// Prev/Next buttons
// document.querySelector(".vision-prev").addEventListener("click", () => goTo(-1));
// document.querySelector(".vision-next").addEventListener("click", () => goTo(1));

// Optional: arrow keys
// document.addEventListener("keydown", (e) => {
//   if (e.key === "ArrowLeft") goTo(-1);
//   if (e.key === "ArrowRight") goTo(1);
// });

// Init
//updateSlide(0);

// slider code ended 

// Enhanced navigation with scroll effect
// window.addEventListener("scroll", function () {
//   const navbar = document.getElementById("mainNavbar");
//   if (window.scrollY > 50) {
//     navbar.classList.add("scrolled");
//   } else {
//     navbar.classList.remove("scrolled");
//   }
// });

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

$(document).ready(function () {
  const $navbar = $('#navbarNav'); // your collapse ID

  // When navbar opens
  $navbar.on('shown.bs.collapse', function () {
    $('body').addClass('overflow-hidden');
  });

  // When navbar closes (outside click, link click, ESC, anything)
  $navbar.on('hidden.bs.collapse', function () {
    $('body').removeClass('overflow-hidden');
  });
});
// remove no-js class if JS is enabled
document.documentElement.classList.remove("no-js");
