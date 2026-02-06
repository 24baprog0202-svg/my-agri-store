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
