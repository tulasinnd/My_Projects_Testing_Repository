import streamlit as st

def snacks_veg():
    # Define the list of veg breakfast recipes
    recipes = [
        {"id":1,
        "name": "Omelette",
          "steps": ["Whisk eggs and milk", 
                    "Heat a non-stick pan", 
                    "Pour in egg mixture",
                    "Add fillings", 
                    "Fold and serve"],
            "image_link":"www.google.com"},

        {"id":2,
        "name": "Poha", 
         "steps": ["Wash and soak poha for 10 minutes", 
                   "Heat oil in a pan", 
                   "Add mustard seeds and curry leaves", 
                   "Add chopped onions, green chillies, and ginger", 
                   "Add poha and mix well", 
                   "Garnish with coriander leaves and serve"],
            "image_link":"www.google.com"},

        {"id":3,
        "name": "Upma", 
         "steps": ["Roast semolina in a pan", 
                   "Heat oil in another pan", 
                   "Add mustard seeds, urad dal, and curry leaves", 
                   "Add chopped onions, green chillies, and ginger", 
                   "Add water, salt, and boiled vegetables", 
                   "Add roasted semolina and mix well", 
                   "Garnish with coriander leaves and serve"],
            "image_link":"www.google.com"}
    ]

    # Create an expander for each recipe
    for recipe in recipes:
        with st.expander(recipe["name"]):
            # Display the steps for the recipe
            col1,col2=st.columns([5,5])
            with col1:
                for i, step in enumerate(recipe["steps"]):
                    st.write(f"Step {i+1}: {step}")
            with col2:
                st.write(recipe["image_link"])

def snacks_nonveg():
    # Define the list of veg breakfast recipes
    recipes = [
        {"id":1,
        "name": "Omelette",
          "steps": ["Whisk eggs and milk", 
                    "Heat a non-stick pan", 
                    "Pour in egg mixture",
                    "Add fillings", 
                    "Fold and serve"],
            "image_link":"www.google.com"
            },

        {"id":2,
        "name": "chicken soup", 
         "steps": ["Wash and soak poha for 10 minutes", 
                   "Heat oil in a pan", 
                   "Add mustard seeds and curry leaves", 
                   "Add chopped onions, green chillies, and ginger", 
                   "Add poha and mix well", 
                   "Garnish with coriander leaves and serve"],
            "image_link":"www.google.com"},

        {"id":3,
        "name": "mutton soup", 
         "steps": ["Roast semolina in a pan", 
                   "Heat oil in another pan", 
                   "Add mustard seeds, urad dal, and curry leaves", 
                   "Add chopped onions, green chillies, and ginger", 
                   "Add water, salt, and boiled vegetables", 
                   "Add roasted semolina and mix well", 
                   "Garnish with coriander leaves and serve"],
            "image_link":"www.google.com"}
    ]

    # Create an expander for each recipe
    for recipe in recipes:
        with st.expander(recipe["name"]):
            # Display the steps for the recipe
            col1,col2=st.columns([5,5])
            with col1:
                for i, step in enumerate(recipe["steps"]):
                    st.write(f"Step {i+1}: {step}")
            with col2:
                st.write(recipe["image_link"])