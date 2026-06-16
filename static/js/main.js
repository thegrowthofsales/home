/* ============================================================
   THE GROWTH OF SALES - MAIN JAVASCRIPT
   ============================================================ */

'use strict';

// ============================================================
// PRELOADER
// ============================================================
window.addEventListener('load', function () {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(function () {
            preloader.classList.add('hidden');
        }, 2200);
    }
});

// ============================================================
// AOS INITIALIZATION
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 700,
            easing: 'ease-out-cubic',
            once: true,
            offset: 60,
            delay: 0
        });
    }
});

// ============================================================
// NAVBAR
// ============================================================
(function () {
    const navbar = document.getElementById('mainNav');
    const navToggle = document.getElementById('navToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const scrollTopBtn = document.getElementById('scrollTopBtn');

    // Scroll effect
    function handleScroll() {
        const scrollY = window.scrollY;

        if (navbar) {
            if (scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        if (scrollTopBtn) {
            if (scrollY > 400) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Run on init

    // Mobile menu toggle
    if (navToggle && mobileMenu) {
        navToggle.addEventListener('click', function () {
            navToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close on link click
        const mobileLinks = mobileMenu.querySelectorAll('.mobile-link');
        mobileLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                navToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close on outside click
        document.addEventListener('click', function (e) {
            if (
                mobileMenu.classList.contains('active') &&
                !mobileMenu.contains(e.target) &&
                !navToggle.contains(e.target)
            ) {
                navToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // Scroll to top
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
})();

// ============================================================
// SWIPER TESTIMONIALS
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    const swiperEl = document.querySelector('.testimonials-swiper');
    if (swiperEl && typeof Swiper !== 'undefined') {
        new Swiper('.testimonials-swiper', {
            slidesPerView: 1,
            spaceBetween: 28,
            loop: true,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
                pauseOnMouseEnter: true
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
                dynamicBullets: true
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev'
            },
            breakpoints: {
                640: { slidesPerView: 1 },
                768: { slidesPerView: 2 },
                1024: { slidesPerView: 3 }
            },
            grabCursor: true,
            effect: 'slide'
        });
    }
});

// ============================================================
// COUNTER ANIMATION
// ============================================================
function animateCounter(el, target, suffix) {
    const duration = 2000;
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const timer = setInterval(function () {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        el.textContent = Math.floor(current) + suffix;
    }, 16);
}

function initCounters() {
    const statNumbers = document.querySelectorAll('.stat-number');
    if (statNumbers.length === 0) return;

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                entry.target.dataset.animated = 'true';
                const raw = entry.target.dataset.target || entry.target.textContent;
                const suffix = raw.replace(/[0-9]/g, '');
                const number = parseInt(raw.replace(/[^0-9]/g, ''), 10);
                if (!isNaN(number)) {
                    animateCounter(entry.target, number, suffix);
                }
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(function (el) {
        observer.observe(el);
    });
}

document.addEventListener('DOMContentLoaded', initCounters);

// ============================================================
// CONTACT FORM
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

    const submitBtn = contactForm.querySelector('[type="submit"]');
    const formMsg = document.getElementById('formMessage');

    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Button loading state
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        }

        const formData = new FormData(contactForm);

        fetch('/contact', {
            method: 'POST',
            body: formData
        })
        .then(function (res) {
            return res.json().then(function (data) {
                return { status: res.status, data: data };
            });
        })
        .then(function (result) {
            if (formMsg) {
                formMsg.style.display = 'block';
                if (result.status === 200) {
                    formMsg.className = 'form-message success';
                    formMsg.innerHTML = '<i class="fas fa-check-circle"></i> ' + result.data.message;
                    contactForm.reset();
                } else {
                    const errors = result.data.errors || ['Something went wrong.'];
                    formMsg.className = 'form-message error';
                    formMsg.innerHTML = '<i class="fas fa-exclamation-circle"></i> ' + errors.join(', ');
                }
                setTimeout(function () {
                    formMsg.style.display = 'none';
                }, 6000);
            }
        })
        .catch(function () {
            if (formMsg) {
                formMsg.style.display = 'block';
                formMsg.className = 'form-message error';
                formMsg.innerHTML = '<i class="fas fa-exclamation-circle"></i> Network error. Please try again.';
            }
        })
        .finally(function () {
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> <span>Send Message</span>';
            }
        });
    });
});

// ============================================================
// SMOOTH HOVER EFFECTS FOR SERVICE CARDS
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.service-card, .strategy-card, .industry-card');
    cards.forEach(function (card) {
        card.addEventListener('mouseenter', function () {
            this.style.willChange = 'transform';
        });
        card.addEventListener('mouseleave', function () {
            this.style.willChange = 'auto';
        });
    });
});

// ============================================================
// PAGE TRANSITION
// ============================================================
document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('page-loaded');
});