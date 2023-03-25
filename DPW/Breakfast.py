import streamlit as st

def breakfast_veg():
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

def breakfast_nonveg():
    import streamlit as st
    # Define function to create block with colored heading
    def create_block(heading, content,pic, color,col):
        # st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px;"><h4 style="color:{col}">{heading}</h4><p style="color:{col}; font-size: 20px">{content}</p></div>', unsafe_allow_html=True)
        # st..image(pic, caption=' ', use_column_width=True, output_format='JPEG')
        st.write(f'<div style="background-color:{color}; padding:10px; border-radius:5px; margin-bottom:10px; display:flex; align-items:center;">'
                f'<div style="flex:1;"><h4 style="color:{col}">{heading}</h4><p style="color:{col}; font-size: 20px">{content}</p></div>'
                f'<div style="flex:1;"><img src="{pic}" style="width:100%; height:auto;"></div>'
                f'</div>',
                unsafe_allow_html=True)
    # Define educational qualifications
    skills = [
        {'skill': 'Spinach and Egg Scramble',
         'd1':"""We are so obsessed with eggs, especially fried and sunny-side up.
         We can crack eggs on any vegetable we cook in a pan and this spinach recipe 
         is one of our favorite keto breakfast recipes. OMG that yolk leaking on the 
         cooked spinach is just irresistible! Watch the video below and see it yourself!
         Nobody can resist that yolk! YUM! We sometimes have it even for a busy weeknight dinner. """,
         'd2':"https://www.giverecipe.com/wp-content/uploads/2019/01/eggs-with-spinach.jpg",
         },

        {'skill': '2 DESCRIPTIVE STATISTICS',
         'd1':'DISTRIBUTIONS:&nbsp;&nbsp;&nbsp;Normal, Exponential, Power-Law etc',
         'd2':"https://www.athousandcountryroads.com/wp-content/uploads/2019/04/eggwithspinach.jpg",
         },

        {'skill': '3 DATA VISUALIZATION',
         'd1':'MATPLOTLIB: Line, Bar, Box, Pie, Scatter Plots etc',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},

         {'skill': '4 EDA & FE',
         'd1':'Data Cleaning, Descriptive Statistics',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},

        {'skill': '5 MACHINE LEARNING',
         'd1':'Supervised Learning: Linear, Logistic, Decision Tree, Random Forest',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},

        {'skill': '6 DEEP LEARNING',
         'd1':'Activation Functions: ReLU ( and variants), sigmoid, tanh',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},

        {'skill': '7 DATABASES',
         'd1':'MySQL: CRUD, Constraints, Joins, Normalization',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},
        
        {'skill': '8 GUI & DEPLOYMENT',
         'd1':'Plotly',
         'd2':r"C:\Users\91939\OneDrive\Desktop\Personal_Projects\DIET_RECEPIES\Diet_Dataset\bf-1.jpg",},
    ]

    # Print each qualification as a block with different color
    #colors = ['rgb(255, 102, 102, 0.2)', 'rgb(102, 255, 178, 0.2)', 'rgb(255, 178, 102, 0.2)', 'rgb(102, 204, 255, 0.2)']
    colors = ['rgb(255, 102, 255,0.2)', 'rgba(54, 162, 235, 0.4)', 'rgba(255, 206, 86, 0.4)', 'rgba(75, 192, 192, 0.4)', 'rgba(153, 102, 255, 0.4)', 'rgb(0, 102, 255,0.3)', 'rgba(37, 121, 140, 0.4)', 'rgba(238, 130, 238, 0.4)']
    colors1 = ['#ff66ff', '#36A2EB', '#ffcc00', '#4BC0C0', '#bf80ff', '#4d94ff', '#00b300', '#ff99ff']

    col1, col2 = st.columns(2)
    for i, skill in enumerate(skills):                
                create_block(f"{skill['skill']}", f"{skill['d1']}",f"{skill['d2']}", colors[i % len(colors)], colors1[i % len(colors)])
        


# SOUPS
# SALADS[coconut]
# BOILED
# HEALTH JUICES
# SMOOTHIS

# RAGI [carrot, beets, onions, ginger, garlic, spring onions]
# Finger millet(Ragi) & Great millet(Jonna)
# Finger millet(Ragi) & pearl millet(Sajja)
# Finger millet(Ragi) & foxtail millet(Korra)
# Finger millet(Ragi) & Little millet(Sama)
# Finger millet(Ragi) & Kodo millet(Arika)

# EGGS [peas, chick peas, sweetcorn, groundnuts, spring onions, carrots, beets, mint,Cilantro, pepper, lemons ]
# Spinach and Egg Scramble
# Egg and tomato skillet 
# Garlic Cabbage and Egg Delight
# potatos and Egg 

# SALADS [coconut, pepper, yogurt, mint, Cilantro, chilli flakes, tomatos, onions, lemons, roasted nuts, cheese, Mayonnaise, sesame, carrots, beets]
# Grilled Chicken, Boiled Chicken, Roasted Chicken
# Boiled Proten Salad [ sanagalu (chickpeas), beans, alasandalu(black eyed peas), ulavalu(Horse gram), kidney beans ]
# Sprouts Salad [sanagalu (chickpeas),  alasandalu(black eyed peas), ulavalu(Horse gram), pesalu(moong)]
# Boiled Sprouts Salad 

# SOUPS [coconut milk, curry leaves, tamarind, yogurt, cilantro, mint]
# Lentils [red lentils, green lentils, split peas]
# Vegetables [carrots, peas, beans, spinach, cabbage, cauliflower, tomatoes, potatoes, onions]
# Spices [cumin, coriander, turmeric, garam masala, mustard seeds, red chili powder, pepper]






# Oatmeal with toppings like fresh berries, nuts, and honey
# Greek yogurt with granola and fruit
# Avocado toast with a poached egg and cherry tomatoes
# Scrambled eggs with spinach and feta cheese
# Smoothie bowl with frozen fruit, yogurt, and granola
# Breakfast burrito with scrambled eggs, black beans, and salsa
# Pancakes with fruit and maple syrup
# Breakfast sandwich with egg, cheese, and bacon or sausage
# Fruit and nut butter toast
# Homemade breakfast muffins or scones with fruit or nuts.


# Here are some breakfast ideas you can make using the ingredients you listed:

# Veggie omelet: Beat the eggs in a bowl and add chopped onions, chillies, cabbage, peas, and sweetcorn. Heat a non-stick pan, pour in the egg mixture, and cook until the eggs are set. Fold the omelet and serve with a side of sliced tomatoes.

# Roasted vegetable hash: Preheat the oven to 425°F. Cut the sweet potato, potato, carrot, beetroot, and onion into small cubes, and place them on a baking sheet. Drizzle with olive oil, salt, and pepper, and roast for 20-25 minutes, stirring occasionally. Serve with poached eggs on top.

# Spicy sweet potato toast: Cut the sweet potato into 1/2-inch thick slices and toast in a toaster or oven until tender. Mash some avocado and spread it on the sweet potato slices. Top with cooked beans, chopped chillies, and a squeeze of lemon.

# Tomato and coconut chutney sandwich: Make a quick chutney by blending chopped tomatoes, coconut, chillies, lemon juice, and honey in a food processor. Toast some bread and spread the chutney on one slice. Top with sliced boiled eggs and cabbage, and another slice of bread.

# Vegetable frittata: Beat the eggs in a bowl and add chopped onions, peas, sweetcorn, and grated carrot. Heat a non-stick pan, pour in the egg mixture, and cook until the eggs are set. Top with grated cheese and place under the broiler until the cheese is melted and bubbly. Serve with a side of sliced tomatoes.
