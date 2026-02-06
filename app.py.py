import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="GreenAcres Farm Store", page_icon="🚜", layout="wide")

# 2. Session State (This remembers the cart when you click buttons)
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 3. Define your Agri-Products (Data)
products = [
    {"id": 1, "name": "Organic Honey 🍯", "price": 12.00, "unit": "500g Jar", "desc": "Raw, wildflower honey."},
    {"id": 2, "name": "Farm Eggs 🥚", "price": 5.50, "unit": "Dozen", "desc": "Free-range, brown eggs."},
    {"id": 3, "name": "Crisp Apples 🍎", "price": 3.00, "unit": "1 kg", "desc": "Freshly picked Gala apples."},
    {"id": 4, "name": "Sourdough Bread 🍞", "price": 6.50, "unit": "Loaf", "desc": "Baked fresh this morning."},
    {"id": 5, "name": "Local Spinach 🥬", "price": 4.00, "unit": "Bunch", "desc": "Pesticide-free greens."}
]

# 4. Sidebar: Shopping Cart
with st.sidebar:
    st.header("🛒 Your Basket")
    
    if len(st.session_state.cart) == 0:
        st.write("Your basket is empty.")
    else:
        total = 0
        for item in st.session_state.cart:
            st.write(f"- {item['name']} (${item['price']})")
            total += item['price']
        
        st.markdown("---")
        st.subheader(f"Total: ${total:.2f}")
        
        # Payment Button (Mock)
        if st.button("Checkout via WhatsApp"):
            # Generates a pre-filled WhatsApp link with the order
            order_text = "%0A".join([f"{i['name']} - ${i['price']}" for i in st.session_state.cart])
            wa_link = f"https://wa.me/1234567890?text=Hello, I would like to buy:%0A{order_text}"
            st.markdown(f"[Click to Send Order]({wa_link})")
            
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()

# 5. Main Page Layout
st.title("🚜 GreenAcres Farm Direct")
st.write("Fresh produce directly from our fields to your table.")

# Display Products in a Grid
cols = st.columns(3) # Create 3 columns

for i, product in enumerate(products):
    with cols[i % 3]: # Cycle through columns
        with st.container(border=True): # improved card UI
            st.subheader(product["name"])
            st.write(product["desc"])
            st.write(f"**${product['price']:.2f}** / {product['unit']}")
            
            if st.button(f"Add to Cart", key=product["id"]):
                st.session_state.cart.append(product)
                st.toast(f"Added {product['name']} to cart!")
                st.rerun() # Refresh to update sidebar count

# 6. Contact / Footer
st.markdown("---")
st.markdown("### 📍 Delivery Info")
st.info("We deliver to Zip Codes 10001 - 10005 every Tuesday and Friday.")
import streamlit as st
import pandas as pd
import random

# --- 1. CONFIG & SETUP ---
st.set_page_config(page_title="AgriSmart Store", page_icon="🌱", layout="wide")

if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'box_fill' not in st.session_state:
    st.session_state.box_fill = 0

# --- 2. DATA (MOCK DATABASE) ---
products = [
    {"id": 1, "name": "Organic Honey 🍯", "price": 12.00, "category": "Pantry"},
    {"id": 2, "name": "Farm Eggs (Dozen) 🥚", "price": 5.50, "category": "Dairy"},
    {"id": 3, "name": "Gala Apples 🍎", "price": 3.00, "category": "Fruit"},
    {"id": 4, "name": "Fresh Spinach 🥬", "price": 4.00, "category": "Veg"},
    {"id": 5, "name": "Sourdough Bread 🍞", "price": 6.50, "category": "Bakery"},
    {"id": 6, "name": "Carrots (Bunch) 🥕", "price": 2.50, "category": "Veg"},
]

# Simple Logic for Recipe Suggestions
recipes = {
    "Omelet": ["Farm Eggs (Dozen) 🥚", "Fresh Spinach 🥬"],
    "Honey Toast": ["Organic Honey 🍯", "Sourdough Bread 🍞"],
    "Healthy Snack": ["Gala Apples 🍎", "Organic Honey 🍯"]
}

# --- 3. SIDEBAR: SMART CART ---
with st.sidebar:
    st.header("🛒 Smart Cart")
    cart_names = [item['name'] for item in st.session_state.cart]
    
    # Cart Display
    if not st.session_state.cart:
        st.info("Basket is empty")
    else:
        for item in st.session_state.cart:
            st.write(f"▪ {item['name']} - ${item['price']}")
        
        total = sum(i['price'] for i in st.session_state.cart)
        st.markdown(f"### Total: ${total:.2f}")
        
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()
            
    st.markdown("---")
    
    # INNOVATION 1: RECIPE RECOMMENDER
    st.subheader("👨‍🍳 Chef's Suggestions")
    found_recipe = False
    for recipe_name, ingredients in recipes.items():
        # Check if user has at least one ingredient but not all
        has_some = any(ing in cart_names for ing in ingredients)
        has_all = all(ing in cart_names for ing in ingredients)
        
        if has_some and not has_all:
            missing = [ing for ing in ingredients if ing not in cart_names]
            st.warning(f"**Make {recipe_name}!**")
            st.caption(f"You are missing: {', '.join(missing)}")
            found_recipe = True
    
    if not found_recipe and len(st.session_state.cart) > 0:
        st.caption("Add more items to unlock recipe ideas!")

# --- 4. MAIN LAYOUT WITH TABS ---
st.title("🌱 AgriSmart: The Future of Farm Direct")

# We use tabs to separate the "Buying" experience from the "Data" experience
tab1, tab2, tab3 = st.tabs(["🛍️ Shop Market", "📦 Build-A-Box", "📊 Farm Transparency"])

# --- TAB 1: STANDARD SHOP ---
with tab1:
    st.subheader("Fresh Harvest This Week")
    
    # Search Bar
    search = st.text_input("🔍 Search products...", "")
    
    col1, col2, col3 = st.columns(3)
    filtered_products = [p for p in products if search.lower() in p['name'].lower()]
    
    for i, p in enumerate(filtered_products):
        with [col1, col2, col3][i % 3]:
            with st.container(border=True):
                st.markdown(f"### {p['name']}")
                st.write(f"**${p['price']:.2f}**")
                if st.button("Add to Cart", key=f"add_{p['id']}"):
                    st.session_state.cart.append(p)
                    st.toast(f"Added {p['name']}!")
                    st.rerun()

# --- TAB 2: INNOVATION 2 (SUBSCRIPTION BUILDER) ---
with tab2:
    st.subheader("📦 Build Your Weekly Subscription Box")
    st.write("Fill your box to 100% to get free shipping!")
    
    # Visual Progress Bar
    current_fill = len(st.session_state.cart) * 15 # Assuming each item is 15% of a box
    if current_fill > 100: current_fill = 100
    
    st.progress(current_fill)
    st.caption(f"Box is {current_fill}% Full")
    
    if current_fill == 100:
        st.success("🎉 Your box is full! You qualify for Free Shipping.")
    else:
        st.info(f"Add {int((100-current_fill)/15)} more items to fill the box.")

# --- TAB 3: INNOVATION 3 (FARM DATA) ---
with tab3:
    st.subheader("📊 Transparency Dashboard")
    st.write("We believe in open data. Here is what we harvested yesterday vs today.")
    
    # Mock Data for Charts
    chart_data = pd.DataFrame({
        'Crop': ['Tomatoes', 'Potatoes', 'Spinach', 'Carrots'],
        'Yesterday (kg)': [50, 120, 30, 40],
        'Today (kg)': [65, 110, 45, 60]
    }).set_index('Crop')
    
    st.bar_chart(chart_data)
    
    st.metric(label="Total Co2 Saved (vs Supermarket)", value="124 kg", delta="12%")
