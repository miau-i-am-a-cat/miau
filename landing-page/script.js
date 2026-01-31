// Wingman Labs In-Store Landing Page
// Minimal interactions, optimized for mobile

(function() {
    'use strict';
    
    // FAQ accordion (optional enhancement)
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        // Initially show all answers (no accordion behavior)
        // Can be enhanced later if needed
    });
    
    // Track CTA clicks (placeholder for analytics)
    const ctaButtons = document.querySelectorAll('.btn');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const buttonText = this.textContent.trim();
            
            // Placeholder for analytics tracking
            // Example: gtag('event', 'cta_click', { button: buttonText });
            
            console.log('CTA clicked:', buttonText);
        });
    });
    
    // Lazy loading images (browser native)
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            img.loading = 'lazy';
        });
    }
    
    // Smooth scroll for anchor links (if any added later)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Viewport height fix for mobile browsers
    function setVH() {
        const vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    }
    
    setVH();
    window.addEventListener('resize', setVH);
    
    // Performance: Mark page as interactive
    if ('performance' in window && 'mark' in window.performance) {
        window.addEventListener('load', function() {
            performance.mark('page-interactive');
        });
    }
    
})();
