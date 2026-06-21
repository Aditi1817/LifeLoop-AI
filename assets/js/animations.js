/**
 * LifeLoop AI - Animation Library
 * Custom animations for enhanced user experience
 */

// ============ ANIMATION UTILITIES ============

class LifeLoopAnimations {
    constructor() {
        this.observer = null;
        this.initIntersectionObserver();
    }

    // Initialize Intersection Observer for scroll animations
    initIntersectionObserver() {
        if ('IntersectionObserver' in window) {
            this.observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animated');
                        this.observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            // Observe all elements with animation classes
            document.addEventListener('DOMContentLoaded', () => {
                document.querySelectorAll('.animate-on-scroll').forEach(el => {
                    this.observer.observe(el);
                });
            });
        }
    }

    // Counter animation
    animateCounter(element, target, duration = 2000) {
        const start = 0;
        const startTime = performance.now();
        
        const updateCounter = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const current = Math.floor(progress * target);
            
            element.textContent = current;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        };
        
        requestAnimationFrame(updateCounter);
    }

    // Typewriter effect
    typewriter(element, text, speed = 50) {
        let index = 0;
        element.textContent = '';
        
        const type = () => {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            }
        };
        
        type();
    }

    // Confetti effect (celebration)
    createConfetti(duration = 3000) {
        const colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#FF8E53', '#A8E6CF', '#FFB7B2'];
        const container = document.createElement('div');
        container.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
            overflow: hidden;
        `;
        document.body.appendChild(container);
        
        const startTime = Date.now();
        const confettiCount = 150;
        
        for (let i = 0; i < confettiCount; i++) {
            const confetti = document.createElement('div');
            const color = colors[Math.floor(Math.random() * colors.length)];
            const size = Math.random() * 10 + 5;
            const left = Math.random() * 100;
            const delay = Math.random() * 1000;
            const duration = Math.random() * 2000 + 1500;
            
            confetti.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size * 0.6}px;
                background: ${color};
                left: ${left}%;
                top: -10px;
                border-radius: 2px;
                transform: rotate(${Math.random() * 360}deg);
                animation: confettiFall ${duration}ms ease-in ${delay}ms forwards;
            `;
            
            container.appendChild(confetti);
        }
        
        // Add keyframe animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes confettiFall {
                0% {
                    transform: translateY(0) rotate(0deg) scale(1);
                    opacity: 1;
                }
                100% {
                    transform: translateY(110vh) rotate(720deg) scale(0.5);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        
        // Clean up after duration
        setTimeout(() => {
            container.remove();
            style.remove();
        }, duration + 1000);
    }

    // Particle background effect
    createParticleBackground(canvasId, color = 'rgba(255,255,255,0.3)') {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        let width, height;
        const particles = [];
        const particleCount = 80;
        
        const resize = () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        };
        
        window.addEventListener('resize', resize);
        resize();
        
        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.size = Math.random() * 3 + 1;
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.speedY = (Math.random() - 0.5) * 0.5;
            }
            
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                
                if (this.x < 0 || this.x > width) this.speedX *= -1;
                if (this.y < 0 || this.y > height) this.speedY *= -1;
            }
            
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = color;
                ctx.fill();
            }
        }
        
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }
        
        const animate = () => {
            ctx.clearRect(0, 0, width, height);
            
            particles.forEach(particle => {
                particle.update();
                particle.draw();
            });
            
            // Draw connections
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 150) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(255,255,255,${0.1 * (1 - distance / 150)})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            
            requestAnimationFrame(animate);
        };
        
        animate();
    }

    // Gradient animation
    animateGradient(element, colors, duration = 5000) {
        let index = 0;
        element.style.background = `linear-gradient(135deg, ${colors[0]}, ${colors[1]})`;
        element.style.backgroundSize = '400% 400%';
        element.style.animation = `gradientAnimation ${duration}ms ease infinite`;
        
        // Add keyframe animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
        `;
        document.head.appendChild(style);
    }

    // Shake animation for error feedback
    shakeElement(element) {
        element.style.animation = 'shake 0.5s ease';
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
                20%, 40%, 60%, 80% { transform: translateX(10px); }
            }
        `;
        document.head.appendChild(style);
        
        setTimeout(() => {
            element.style.animation = '';
            style.remove();
        }, 500);
    }

    // Progress bar animation
    animateProgressBar(element, targetPercent, duration = 1000) {
        const startTime = performance.now();
        const startPercent = parseFloat(element.style.width) || 0;
        
        const updateProgress = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const currentPercent = startPercent + (targetPercent - startPercent) * progress;
            
            element.style.width = `${currentPercent}%`;
            
            if (progress < 1) {
                requestAnimationFrame(updateProgress);
            }
        };
        
        requestAnimationFrame(updateProgress);
    }

    // Float animation for elements
    addFloatAnimation(element, duration = 3) {
        element.style.animation = `float ${duration}s ease-in-out infinite`;
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
            }
        `;
        document.head.appendChild(style);
    }

    // Smooth scroll to element
    smoothScrollTo(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    // Pulsing glow effect
    addPulseGlow(element, color = '#FF6B6B') {
        element.style.animation = `pulseGlow 2s ease-in-out infinite`;
        element.style.boxShadow = `0 0 20px ${color}40`;
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes pulseGlow {
                0%, 100% { box-shadow: 0 0 20px ${color}40; }
                50% { box-shadow: 0 0 40px ${color}80; }
            }
        `;
        document.head.appendChild(style);
    }
}

// ============ DOM READY INITIALIZATION ============

// Initialize animations when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const animations = new LifeLoopAnimations();
    
    // Auto-initialize elements with data-animation attribute
    document.querySelectorAll('[data-animation]').forEach(el => {
        const animationType = el.getAttribute('data-animation');
        switch(animationType) {
            case 'counter':
                const target = parseInt(el.getAttribute('data-target'));
                if (target) {
                    animations.animateCounter(el, target);
                }
                break;
            case 'typewriter':
                const text = el.getAttribute('data-text');
                if (text) {
                    animations.typewriter(el, text);
                }
                break;
            case 'float':
                animations.addFloatAnimation(el);
                break;
            case 'shake':
                el.addEventListener('click', () => {
                    animations.shakeElement(el);
                });
                break;
        }
    });

    // Auto-initialize progress bars
    document.querySelectorAll('[data-progress]').forEach(el => {
        const target = parseFloat(el.getAttribute('data-progress'));
        if (target) {
            const progress = new LifeLoopAnimations();
            progress.animateProgressBar(el, target);
        }
    });

    // Auto-initialize particle backgrounds
    document.querySelectorAll('[data-particles]').forEach(el => {
        const canvas = document.createElement('canvas');
        canvas.id = 'particle-canvas';
        canvas.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        `;
        el.appendChild(canvas);
        
        const color = el.getAttribute('data-particle-color') || 'rgba(255,255,255,0.3)';
        const animations = new LifeLoopAnimations();
        animations.createParticleBackground('particle-canvas', color);
    });
});

// ============ UTILITY FUNCTIONS ============

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for performance
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LifeLoopAnimations;
}