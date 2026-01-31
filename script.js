// Wingman Labs - Landing Page Interactions
// Optimized for mobile performance

(function() {
    'use strict';
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Track CTA clicks (add analytics later)
    const ctaButtons = document.querySelectorAll('.cta-primary');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add analytics tracking here
            console.log('CTA clicked:', this.textContent.trim());
            
            // For now, show a simple message
            // Replace with actual purchase flow
            if (this.getAttribute('href') === '#buy') {
                e.preventDefault();
                alert('Great choice! Grab your Wingman Labs Energy at the checkout counter.');
            }
        });
    });
    
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe sections for scroll animations
    document.querySelectorAll('section:not(.hero)').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
    
    // Add loading state for images
    const heroImage = document.querySelector('.hero-image img');
    if (heroImage) {
        heroImage.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        heroImage.style.opacity = '0';
        heroImage.style.transition = 'opacity 0.3s ease';
    }
    
    // Performance: Lazy load images below fold
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(img => {
            img.src = img.dataset.src || img.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/lazysizes@5/lazysizes.min.js';
        document.body.appendChild(script);
    }
    
    // Track page view (add analytics here)
    console.log('Wingman Labs landing page loaded');
    
})();
