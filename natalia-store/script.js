// ===== NATALIA ALYSSANDRA E-COMMERCE =====
// Product Data & Store Functionality

const products = [
    {
        id: 1,
        name: "Bikini Martini",
        price: 45,
        image: "images/bikini-martini.jpg",
        category: "lingerie",
        badge: "sold-out",
        soldOut: true,
        description: "Sparkling rhinestone lingerie set with long sleeves. Perfect for those show-stopping moments."
    },
    {
        id: 2,
        name: "Tini Weenie Kini",
        price: 40,
        image: "images/tini-weenie-kini.jpg",
        category: "bikini",
        badge: "bestseller",
        description: "Classic string bikini with rhinestone crystal details. Made for beach days and pool parties."
    },
    {
        id: 3,
        name: "Winkini",
        price: 45,
        image: "images/winkini.jpg",
        category: "lingerie",
        description: "Flirty two-piece teddy bodysuit. Stretch mesh for the perfect fit."
    },
    {
        id: 4,
        name: "Talk the Talkini",
        price: 50,
        image: "images/talk-the-talkini.jpg",
        category: "bodysuit",
        description: "Mesh body stocking that speaks for itself. Bold, confident, irresistible."
    },
    {
        id: 5,
        name: "Shockini",
        price: 50,
        image: "images/shockini.jpg",
        category: "lingerie",
        badge: "new",
        description: "Exotic pole dancewear with rhinestone details. Turn the club into your runway."
    },
    {
        id: 6,
        name: "Peach Bellini",
        price: 55,
        image: "images/peach-bellini.jpg",
        category: "bodysuit",
        description: "Full body net suit with hot diamond details. Serve looks from head to toe."
    },
    {
        id: 7,
        name: "Flirtini",
        price: 55,
        image: "images/flirtini.jpg",
        category: "lingerie",
        description: "Fishnet tube bra and shorts with rhinestone crystals. Flirty and fabulous."
    },
    {
        id: 8,
        name: "I Know U Lookini",
        price: 55,
        image: "images/i-know-u-lookini.jpg",
        category: "lingerie",
        description: "Mesh two-piece with iron ring details. They can look, but they can't touch."
    },
    {
        id: 9,
        name: "Sculptini",
        price: 55,
        image: "images/sculptini.jpg",
        category: "bodysuit",
        description: "Ultra-thin aurora bodysuit. High elastic smooth fabric that hugs every curve."
    },
    {
        id: 10,
        name: "Jetskini",
        price: 50,
        image: "images/jetskini.jpg",
        category: "bodysuit",
        description: "Large mesh fishnet bodystocking. Summer vibes only."
    },
    {
        id: 11,
        name: "Dripini",
        price: 65,
        image: "images/dripini.jpg",
        category: "lingerie",
        badge: "new",
        description: "Fishnet garter belt stocking set. The ultimate drip for your next event."
    },
    {
        id: 12,
        name: "Riskini",
        price: 60,
        image: "images/riskini.jpg",
        category: "bikini",
        description: "Bling rhinestones fishnet bra and shorts. Worth the risk."
    },
    {
        id: 13,
        name: "Temptini",
        price: 50,
        image: "images/temptini.jpg",
        category: "bodysuit",
        description: "Rave festival bodysuit with rhinestones. Pure temptation."
    },
    {
        id: 14,
        name: "Twerkini",
        price: 35,
        image: "images/twerkini.jpg",
        category: "bikini",
        badge: "bestseller",
        description: "Hollow out bikini set. Perfect for summer vibes and making moves."
    },
    {
        id: 15,
        name: "Strikini",
        price: 55,
        image: "images/strikini.jpg",
        category: "bodysuit",
        description: "Aurora smooth bodysuit with high elasticity. Strike a pose."
    },
    {
        id: 16,
        name: "Workini",
        price: 50,
        image: "images/workini.jpg",
        category: "lingerie",
        description: "Hot diamond shiny underwear set. Put in the work, look like a million bucks."
    },
    {
        id: 17,
        name: "Freakini",
        price: 55,
        image: "images/freakini.jpg",
        category: "lingerie",
        description: "Tight babydoll dress lingerie. Let your freak flag fly."
    },
    {
        id: 18,
        name: "Kinkini",
        price: 35,
        image: "images/kinkini.jpg",
        category: "lingerie",
        description: "Fetish latex harness lingerie. Explore your wild side."
    },
    {
        id: 19,
        name: "Mystery Box",
        price: 45,
        image: "images/mystery-box.jpg",
        category: "special",
        badge: "limited",
        description: "What's in Natalia's beach bag? Surprise pieces hand-selected by Natalia herself."
    },
    {
        id: 20,
        name: "Push Up Inserts",
        price: 20,
        image: "images/push-up.jpg",
        category: "accessories",
        description: "3D silicone bra inserts. The secret to that perfect lift."
    }
];

let cart = [];
let currentProduct = null;
let modalQty = 1;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderProducts('all');
    setupFilterButtons();
    loadCart();
});

// Render Products
function renderProducts(filter) {
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';
    
    const filtered = filter === 'all' 
        ? products 
        : products.filter(p => p.category === filter);
    
    filtered.forEach((product, index) => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.style.animationDelay = `${index * 0.05}s`;
        card.id = `product-${product.name.toLowerCase().replace(/\s+/g, '-')}`;
        
        let badgeHTML = '';
        if (product.badge) {
            const badgeClass = product.badge === 'sold-out' ? 'sold-out' : '';
            const badgeText = product.badge === 'sold-out' ? 'Sold Out' 
                : product.badge === 'new' ? 'New'
                : product.badge === 'bestseller' ? 'Best Seller'
                : product.badge === 'limited' ? 'Limited'
                : product.badge;
            badgeHTML = `<span class="product-badge ${badgeClass}">${badgeText}</span>`;
        }
        
        card.innerHTML = `
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}" loading="lazy">
                ${badgeHTML}
                <div class="product-overlay">
                    <button class="quick-view-btn" onclick="openQuickView(${product.id})">
                        ${product.soldOut ? 'View Details' : 'Quick View'}
                    </button>
                </div>
            </div>
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-price">C$${product.price.toFixed(2)}</p>
            </div>
        `;
        
        grid.appendChild(card);
    });
}

// Filter Buttons
function setupFilterButtons() {
    const buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderProducts(btn.dataset.filter);
        });
    });
}

// Quick View Modal
function openQuickView(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;
    
    currentProduct = product;
    modalQty = 1;
    
    document.getElementById('modalImage').src = product.image;
    document.getElementById('modalImage').alt = product.name;
    document.getElementById('modalName').textContent = product.name;
    document.getElementById('modalPrice').textContent = `C$${product.price.toFixed(2)}`;
    document.getElementById('modalDescription').textContent = product.description;
    document.getElementById('modalQty').textContent = modalQty;
    
    const addBtn = document.querySelector('.add-to-cart-btn');
    if (product.soldOut) {
        addBtn.textContent = 'Sold Out';
        addBtn.disabled = true;
        addBtn.style.opacity = '0.5';
    } else {
        addBtn.textContent = 'Add to Bag';
        addBtn.disabled = false;
        addBtn.style.opacity = '1';
    }
    
    document.getElementById('quickViewModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeQuickView() {
    document.getElementById('quickViewModal').classList.remove('active');
    document.body.style.overflow = '';
    currentProduct = null;
}

function updateModalQty(change) {
    modalQty = Math.max(1, modalQty + change);
    document.getElementById('modalQty').textContent = modalQty;
}

// Cart Functions
function addToCartFromModal() {
    if (!currentProduct || currentProduct.soldOut) return;
    
    const size = document.getElementById('modalSize').value;
    
    const existingItem = cart.find(item => 
        item.id === currentProduct.id && item.size === size
    );
    
    if (existingItem) {
        existingItem.qty += modalQty;
    } else {
        cart.push({
            id: currentProduct.id,
            name: currentProduct.name,
            price: currentProduct.price,
            image: currentProduct.image,
            size: size,
            qty: modalQty
        });
    }
    
    saveCart();
    updateCartUI();
    closeQuickView();
    toggleCart();
    
    // Show added animation
    const btn = document.querySelector('.add-to-cart-btn');
    btn.textContent = 'Added!';
    setTimeout(() => {
        btn.textContent = 'Add to Bag';
    }, 1500);
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    updateCartUI();
}

function updateCartQty(index, change) {
    cart[index].qty = Math.max(1, cart[index].qty + change);
    saveCart();
    updateCartUI();
}

function updateCartUI() {
    const cartItems = document.getElementById('cartItems');
    const cartFooter = document.getElementById('cartFooter');
    const cartCount = document.getElementById('cartCount');
    const cartSubtotal = document.getElementById('cartSubtotal');
    
    const totalItems = cart.reduce((sum, item) => sum + item.qty, 0);
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
    
    cartCount.textContent = totalItems;
    cartSubtotal.textContent = `C$${subtotal.toFixed(2)}`;
    
    if (cart.length === 0) {
        cartItems.innerHTML = `
            <div class="empty-cart">
                <p>Your bag is empty</p>
                <a href="#shop" class="continue-shopping" onclick="toggleCart()">Continue Shopping</a>
            </div>
        `;
        cartFooter.style.display = 'none';
    } else {
        cartItems.innerHTML = cart.map((item, index) => `
            <div class="cart-item">
                <div class="cart-item-image">
                    <img src="${item.image}" alt="${item.name}">
                </div>
                <div class="cart-item-details">
                    <p class="cart-item-name">${item.name}</p>
                    <p class="cart-item-size">Size: ${item.size}</p>
                    <div class="cart-item-qty">
                        <button onclick="updateCartQty(${index}, -1)">−</button>
                        <span>${item.qty}</span>
                        <button onclick="updateCartQty(${index}, 1)">+</button>
                    </div>
                    <button class="remove-item" onclick="removeFromCart(${index})">Remove</button>
                </div>
                <div class="cart-item-price">C$${(item.price * item.qty).toFixed(2)}</div>
            </div>
        `).join('');
        cartFooter.style.display = 'block';
    }
}

function saveCart() {
    localStorage.setItem('natalia_cart', JSON.stringify(cart));
}

function loadCart() {
    const saved = localStorage.getItem('natalia_cart');
    if (saved) {
        cart = JSON.parse(saved);
        updateCartUI();
    }
}

// Toggle Functions
function toggleCart() {
    document.getElementById('cartOverlay').classList.toggle('active');
    document.getElementById('cartSidebar').classList.toggle('active');
}

function toggleMenu() {
    document.getElementById('mobileMenu').classList.toggle('active');
    document.body.style.overflow = document.getElementById('mobileMenu').classList.contains('active') ? 'hidden' : '';
}

// Newsletter
function handleNewsletter(e) {
    e.preventDefault();
    const input = e.target.querySelector('input');
    const email = input.value;
    
    // Simulated submission
    const btn = e.target.querySelector('button');
    btn.textContent = 'Subscribed! 💕';
    btn.style.background = '#2ecc71';
    input.value = '';
    
    setTimeout(() => {
        btn.textContent = 'Subscribe';
        btn.style.background = '';
    }, 3000);
}

// Close modals on escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeQuickView();
        if (document.getElementById('cartSidebar').classList.contains('active')) {
            toggleCart();
        }
        if (document.getElementById('mobileMenu').classList.contains('active')) {
            toggleMenu();
        }
    }
});

// Click outside modal to close
document.getElementById('quickViewModal').addEventListener('click', (e) => {
    if (e.target === document.getElementById('quickViewModal')) {
        closeQuickView();
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offset = 100;
            const position = target.getBoundingClientRect().top + window.pageYOffset - offset;
            window.scrollTo({ top: position, behavior: 'smooth' });
        }
    });
});

// Navbar background on scroll
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.main-nav');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(10, 10, 10, 0.98)';
    } else {
        nav.style.background = 'rgba(10, 10, 10, 0.95)';
    }
});
