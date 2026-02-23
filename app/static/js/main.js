/**
 * Zanethemba Cleaning Services - Main JavaScript
 */

// ── SPLASH SCREEN ──
window.addEventListener('DOMContentLoaded', () => {
  const splash = document.getElementById('splash');
  if (splash) {
    setTimeout(() => splash.classList.add('hide'), 2800);
    setTimeout(() => splash.style.display = 'none', 3700);
  }
});

// ── PAGE NAVIGATION ──
function showPage(page) {
  // Hide all pages
  document.querySelectorAll('.page').forEach(p => {
    p.classList.remove('active');
  });
  
  // Remove active from all nav links
  ['home', 'about', 'contact'].forEach(id => {
    const navLink = document.getElementById('nav-' + id);
    const mobLink = document.getElementById('mob-' + id);
    if (navLink) navLink.classList.remove('active');
    if (mobLink) mobLink.classList.remove('active');
  });
  
  // Show selected page
  const targetPage = document.getElementById('page-' + page);
  if (targetPage) {
    targetPage.classList.add('active');
  }
  
  // Activate nav link
  const navLink = document.getElementById('nav-' + page);
  const mobLink = document.getElementById('mob-' + page);
  if (navLink) navLink.classList.add('active');
  if (mobLink) mobLink.classList.add('active');
  
  // Scroll to top
  window.scrollTo({top: 0, behavior: 'smooth'});
  
  // Restart animations
  if (targetPage) {
    targetPage.querySelectorAll('.anim-fadeup').forEach(el => {
      el.style.animation = 'none';
      el.offsetHeight; // Force reflow
      el.style.animation = '';
    });
  }
}

// ── HAMBURGER MENU ──
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  const btn = document.getElementById('hamburger');
  
  if (menu && btn) {
    menu.classList.toggle('open');
    btn.classList.toggle('open');
    document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
  }
}

// ── SCROLL NAV ──
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (navbar) {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  }
});

// ── FORM HANDLING ──
function handleSubmit(e) {
  e.preventDefault();
  
  const form = document.getElementById('contactForm');
  const success = document.getElementById('formSuccess');
  
  if (form && success) {
    form.style.display = 'none';
    success.style.display = 'block';
  }
  
  return false;
}

// ── CAROUSEL ENGINE ──
function createCarousel(id, interval, dotsId) {
  const el = document.getElementById(id);
  if (!el) return;
  
  const slides = el.querySelectorAll('.carousel-slide');
  if (slides.length === 0) return;
  
  const dots = dotsId ? document.getElementById(dotsId) : null;
  let current = 0;

  function goTo(idx) {
    slides[current].classList.remove('active');
    if (dots) {
      const dotElements = dots.querySelectorAll('.carousel-dot');
      if (dotElements[current]) {
        dotElements[current].classList.remove('active');
      }
    }
    
    current = (idx + slides.length) % slides.length;
    slides[current].classList.add('active');
    
    if (dots) {
      const dotElements = dots.querySelectorAll('.carousel-dot');
      if (dotElements[current]) {
        dotElements[current].classList.add('active');
      }
    }
  }

  // Expose goTo globally for hero dots
  if (id === 'heroCarousel') {
    window.heroGoTo = goTo;
  }

  // Auto-rotate
  setInterval(() => goTo(current + 1), interval);
}

// Initialize carousels on page load
document.addEventListener('DOMContentLoaded', () => {
  // Hero carousel (5 seconds, 4 slides, has dots)
  createCarousel('heroCarousel', 5000, 'heroDots');
  
  // Image break carousel (7 seconds, 2 slides)
  createCarousel('breakCarousel', 7000, null);
  
  // Community carousel (6 seconds, 2 slides)
  createCarousel('communityCarousel', 6000, null);
});

// ── SCROLL REVEAL ──
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.1});
  
  document.querySelectorAll('.service-card, .stat-item, .value-item').forEach(el => {
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
});

// ── AJAX FORM SUBMISSION (Optional Enhancement) ──
function submitContactForm(formData) {
  return fetch('/api/contact', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .catch(error => {
    console.error('Error:', error);
    return {success: false, error: 'Network error'};
  });
}
