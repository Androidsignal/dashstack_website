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
}

// Event delegation for tabs (works if tabs are added later)
document.querySelector(".vision-tabs").addEventListener("click", (e) => {
  const tab = e.target.closest(".vision-tab");
  if (!tab) return;
  updateSlide(Number(tab.dataset.index));
});

if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
window.addEventListener('popstate', (e) => {
  updateSlide(0);
  window.scrollTo({ top: 0, left: 0 });
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
