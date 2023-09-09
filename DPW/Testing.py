import streamlit as st

def test():
    import streamlit as st
    # Define function to create block with colored heading
    def create_block(ingredients,heading,pic,col):
        st.write(f'<div style="align-items:center;">'
         #f'<div style="flex:1;"><h4 style="color:{col}">{heading}</h4><p style="color:{col}; font-size: 20px">{content}</p></div>'
         f'<div ><h4 style="color:{col}">{heading}</h4><img src="{pic}" style="width:384px; height:auto;"></div>'
         f'</div>',
         unsafe_allow_html=True)
        with st.expander("See explanation"):
            st.write(ingredients)

    # Define educational qualifications
    skills = [
        {'skill': 'Spinach Egg Scramble',
         'd1':"""   Ingredients:<br>
                    - 2 tablespoons olive oil<br>
                    - 1/2 onion, diced<br>
                    - 2 cloves garlic, minced<br>
                    - 2 cups fresh spinach leaves, washed and chopped<br>
                    - 4 eggs, beaten<br>
                    - Salt and pepper, to taste<br>
                    - Additional twists: mushrooms, bell peppers<br>
                    - Optional toppings: cheese, avocado, hot sauce<br><br>                    
                    Preparation:<br>
                    - Heat oil in skillet, medium heat.<br>
                    - Saute onion until soft, 3-4 min.<br>
                    - Add garlic, cook 1-2 min.<br>
                    - Add spinach, cook until wilted, stir occasionally.<br>
                    - Pour in beaten eggs, scramble.<br>
                    - Cook eggs until set, stir occasionally, break up chunks.<br>
                    - Season with salt and pepper.<br>
                    - Serve hot with optional toppings. Enjoy! """,
         'd2':"https://www.giverecipe.com/wp-content/uploads/2019/01/eggs-with-spinach.jpg",
         },

        {'skill': 'Egg Tomato Skillet ',
         'd1':'''Ingredients:<br>
                - 2 eggs<br>
                - 1 large tomato, diced<br>
                - 1/4 onion, diced<br>
                - 1 clove garlic, minced<br>
                - 1 tablespoon oil or butter<br>
                - Salt and pepper to taste<br><br>
                Preparation:<br>
                - Heat oil or butter in a skillet over medium heat.<br>
                - Add onion and garlic and cook about 2-3 minutes.<br>
                - Add tomato and cook until softened, about 5 minutes.<br>
                - Use a spoon to make 2 wells in the tomato mixture.<br>
                - Crack an egg and season with salt and pepper.<br>
                - Cover the skillet and cook until the eggs are set.<br>
         ''',
         'd2':'https://foreignfork.com/wp-content/uploads/2022/12/Shakshuka-FEATURE.jpg',
         },

        {'skill': 'Garlic Cabbage Egg Delight',
         'd1':'''
        Ingredients:<br>
        - 4 large eggs<br>
        - 4 cups shredded cabbage<br>
        - 2 cloves garlic, minced<br>
        - 2 tablespoons oil<br>
        - Salt and pepper to taste<br><br>
        Preparation:<br>
        - Heat oil in a skillet over medium heat.<br>
        - Add minced garlic and cook for 1-2 minutes.<br>
        - Add shredded cabbage and cook about 5 minutes.<br>
        - Beat the eggs in a bowl and season with salt and pepper.<br>
        - Pour the beaten eggs into the skillet with the cabbage.<br>
        - Stir gently and cook until the eggs are set.<br>
         ''',
         'd2':'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F44%2F2019%2F08%2F27045156%2F3756472.jpg',},

         {'skill': 'Classic Potato Egg Mix',
         'd1':'''
        Ingredients:<br>
        - 2 medium potatoes, diced<br>
        - 4 eggs<br>
        - 1/4 onion, diced<br>
        - 1 clove garlic, minced<br>
        - 2 tablespoons oil<br>
        - Salt and pepper to taste<br><br>
        - Optional toppings: cheese, spring onions <br>
        Preparation:<br>
        - Heat oil in skillet over medium heat.<br>
        - Cook potatoes until browned and crispy, 10-12 mins.<br>
        - Add onion and garlic and cook until softened, 2-3 mins.<br>
        - Beat eggs, season with salt and pepper.<br>
        - Pour eggs into skillet with potatoes and onions.<br>
        - Cook until eggs are set, stirring occasionally, 5-7 mins.<br> ''',
         'd2':'https://www.the-girl-who-ate-everything.com/wp-content/uploads/2018/09/bacon-egg-potato-breakfast-skillet.jpg',},

        {'skill': 'Finger Millet(Ragi) Soup',
         'd1':'''
        Ingredients:<br>
        - carrot/beets, tomato, onions, ginger, garlic, beans<br>
        - Finger millet powder and optional Add-On<br><br>
        Add-Ons:<br>
        - Great millet(Jonna), pearl millet(Sajja),foxtail millet(Korra) <br>
        - Little millet(Sama), Kodo millet(Arika)<br><br>
        Preparation:<br>
        - Boil all the veggies <br>
        - add 1 cup water to veggies<br>
        - add Finger millet slurry<br>
        - cook for 5-7 minutes<br>
        - seve hot!<br>
        ''',
         'd2':"https://i.pinimg.com/564x/01/95/7e/01957e661bc58b539a442eed1a8c1310.jpg"},

        {'skill': 'Egg Veggies Wrap',
         'd1':'',
         'd2':"https://skinnyms.com/wp-content/uploads/2021/07/Simple-Egg-and-Veggie-Breakfast-Wraps-Breakfast-Recipe-2-1200x800.jpg",},

    ]

    # Print each qualification as a block with different color
    colors = ['rgba(255, 102, 102,0.1)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgb(0, 102, 255,0.1)', 'rgba(37, 121, 140, 0.1)', 'rgba(0, 255, 153,0.1)']
    colors1 = ['#cc6699', '#ffa31a', '#42bdbd', '#6699cc', '#7575a3', '#39ac73']

    for i, skill in enumerate(skills):                
                create_block(f"{skill['d1']}", f"{skill['skill']}",f"{skill['d2']}", colors1[i % len(colors)])
