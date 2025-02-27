import streamlit as st

def coffee_bot():
    st.title("Welcome to the Cafe! 🎉")
    orders = []

    while True:
        size = get_size()
        drink_type = get_drink_type()
        type_of_cup = cup_type()
        hot_iced = hot_or_iced()

        orders.append((size, hot_iced, drink_type, type_of_cup))

        if not additional_drink():
            break

    st.write("\n### Here are your orders:")
    for i, order in enumerate(orders, 1):
        st.write(f"{i}. {order[0].capitalize()} {order[1]} {order[2]} in a {order[3]}")

    name = st.text_input("Can I get your name please?")
    if name:
        st.success(f"Thanks, {name}! Your drinks will be ready shortly. 🎉")

# Size of drink
def get_size():
    size = st.selectbox("What size drink can I get for you?", ["Small", "Medium", "Large"])
    return size.lower()

# Drink type
def get_drink_type():
    drink = st.selectbox("What type of drink would you like?", ["Brewed Coffee", "Mocha", "Latte"])
    if drink == "Latte":
        return order_latte()
    return drink

# Type of milk for latte
def order_latte():
    milk = st.selectbox("What kind of milk for your latte?", ["2% milk", "Non-fat milk", "Soy milk"])
    if milk == "2% milk":
        return "latte"
    elif milk == "Non-fat milk":
        return "non-fat latte"
    elif milk == "Soy milk":
        return "soy latte"

# Type of cup
def cup_type():
    cup = st.selectbox("Would you like a:", ["Plastic cup", "Reusable cup"])
    return cup.lower()

# Hot or iced
def hot_or_iced():
    temperature = st.selectbox("Would you like your drink hot or iced?", ["Hot", "Iced"])
    return temperature.lower()

# Additional drink
def additional_drink():
    if st.button("Do you want another drink?"):
        return True
    return False

# Run the coffee bot
coffee_bot()
