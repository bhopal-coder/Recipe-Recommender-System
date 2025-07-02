import streamlit as st
import pandas as pd
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
df=pd.read_csv("ifood_new.csv")
st.markdown(
    """
    <style>
    /* Change Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        padding: 20px;
    }

    /* Increase size of Sidebar Title */
    .sidebar-title {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        color: #FF5733;
    }

    /* Increase size of Sidebar Radio Button Options */
    section[data-testid="stSidebar"] label {
        font-size: 24px !important;
        font-weight: bold;
    }

    /* Increase spacing between radio options */
    div[data-testid="stRadio"] > div {
        gap: 20px !important;
    }

    /* Increase size of Sidebar Selectbox */
    div[data-testid="stSelectbox"] label {
        font-size: 24px !important;
        font-weight: bold;
    }
    div[data-testid="stSelectbox"] select {
        font-size: 22px !important;
        padding: 10px;
    }

    /* Make Sidebar Buttons Larger */
    .big-button {
        width: 100%;
        height: 70px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #FF5733;
        color: white;
        border: none;
    }
    .big-button:hover {
        background-color: #E14D2A;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Title

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://as2.ftcdn.net/jpg/02/62/69/89/1000_F_262698994_fCURbbW76EHXZu7P17CsU4lc6XnsVRs0.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""                           
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #63dbeb;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;        
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 20px; /* Set font size to 50px */
    }
    
    
    .custom-button:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }

    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #f56b53;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 2px 2px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 20px; /* Increase font size for larger text */
        width: 170px;
        height: 60px;
    }

    div.stButton > button:first-child:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-title'>🍴 FlavourMania</p>", unsafe_allow_html=True)
if "refresh_triggered" not in st.session_state:
    st.session_state.refresh_triggered = False

# if "current_page" not in st.session_state:
#     st.session_state.current_page = "option"
# if "selected_category" not in st.session_state:
#     st.session_state.selected_category = "Desserts"
# if "selected_recipe" not in st.session_state:
#     st.session_state.selected_recipe = None
# Bigger Sidebar Radio Button Options
options =(
    
    "🏠 Home","🍛 Main Course", "🍕 Snacks", "🍰 Desserts", "🍹 Shakes"
)
option=st.sidebar.radio("What you want to explore?:",options)
if not st.session_state.refresh_triggered:
    st.session_state.refresh_triggered = True
    st.rerun()
# if option != st.session_state.selected_category:
#     st.session_state.selected_category = option
#     st.session_state.current_page = "option"

recipe_name = st.session_state.get("recipe_name", None)
ing=st.session_state.get("ing_name", None)

if not recipe_name:
    st.warning("No recipe selected.")
    st.switch_page("home.py")

recipe_data = df[df['name'] == recipe_name].iloc[0]
ing_data=df[df['ingredients'] == ing].iloc[0]
# dess=df[df==dess].iloc[0]
# Show recipe and ingr
st.title(f":blue[{recipe_data['name']}]")
st.subheader(":red[Ingredients Required:]")
st.write(ing_data['ingredients'])
st.subheader(f":red[Recipe:]")
st.write(recipe_data['procedure'])

st.session_state.navigated = False
# if st.button("⬅️ Back to Recipes"):
#         st.session_state.current_page="category"
if option=='🍰 Desserts':
#   st.rerun()
  st.subheader(":red[Cakes And Sweet Dishes:]")
  options=['Milk','Maida','Sugar','Dark Chocolate','Cocoa Powder','Baking Soda','Strawberry']
  if "selected_ingredients" not in st.session_state:
    st.session_state.selected_ingredients = set()
  cols = st.columns(3)  # Adjust the number of columns based on preference

  for index, ingredient in enumerate(options):
        with cols[index % 3]:  # Distribute ingredients across columns
            is_selected = ingredient in st.session_state.selected_ingredients
            button_style = f"""           
            <style>
                div[data-testid="stButton"] button {{
                    width: 100%;
                    padding: 10px;
                    margin: 5px 0;
                    border-radius: 5px;
                    font-size: 16px;
                    font-weight: bold;
                    cursor: pointer;
                    background-color: {'red' if is_selected else 'white'};
                    color: {'#11c2f7' if is_selected else 'black'};
                    border: 2px solid #11c2f7;
                    transition: background 0.3s, color 0.3s;
                }}
            </style>
        """
            st.markdown(button_style, unsafe_allow_html=True)

            if st.button(
            f"{'✔ ' if ingredient in st.session_state.selected_ingredients else ''}{ingredient}",
            key=ingredient,
            help="Click to select/deselect", 
            
           ):
              if ingredient in st.session_state.selected_ingredients:
                st.session_state.selected_ingredients.remove(ingredient)  # Deselect
              else:
                st.session_state.selected_ingredients.add(ingredient) 
  # st.subheader(f":red[{st.session_state.selected_ingredients}]")
  dfd=df[df['course']=='dessert']
  ing=st.session_state.selected_ingredients
  vectorizer=TfidfVectorizer()
  ing_matrix=vectorizer.fit_transform(dfd['ingredients'])
  model=NearestNeighbors(n_neighbors=5,metric='cosine')
  model.fit(ing_matrix)
  def recommend_recipesd(user_ingredients,dfd,model,vectorizer):
    input=" ".join(sorted(user_ingredients))
    vector=vectorizer.transform([input])
    distances, indices=model.kneighbors(vector)
    recommended_recipes = dfd.iloc[indices[0]]
    recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
    # return recommended_recipes.sort_values(by='Similarity', ascending=False)
    return recommended_recipes.sample(frac=1, random_state=None)
   

  user_ingredients=ing
  rec = recommend_recipesd(user_ingredients, dfd, model, vectorizer)
  print(rec)

  
  if user_ingredients:
    
      for index, row in rec.iterrows():
        l,r=st.columns(2)
        with l:
          name=row['name']
          st.subheader(f":red[{name}]")
          st.image(row['img_url'], width=170)
          ingr=row['ingredients']
        with r:
          if st.button("Show Recipe:",key=f"rec_dess{index}"):
              st.session_state.recipe_name =name
              st.session_state.ing_name=ingr
              st.session_state.dess=row
              st.session_state.navigated = True
              st.switch_page("pages/recipe.py") 
            #   if option=='🍰 Desserts':
        #   if st.button("Back to Home",key='back'):
        #         st.session_state.navigated = False
        #         st.switch_page("main.py")
elif option=='🍹 Shakes':
  st.rerun()
  st.subheader(":red[Shakes And Drinks:]")
# options=['Mango','Milk','Sugar','Dark Chocolate','Banana','nuts','Pineapple','Lemon','Apple','Orange','Cocoa Powder','Baking Soda','Strawberry']
  categories = {
      "Fruits": ["Pineapple","Strawberry","Banana","Apple","Orange","Mango","Lemon","Nuts"],
      "Essentials":['Milk','Sugar','Dark Chocolate','Cocoa Powder','Soda']
  }
  if "selected_ingredients" not in st.session_state:
      st.session_state.selected_ingredients = set()

  for category, options in categories.items():
      st.subheader(category)
      cols = st.columns(3)


      for index, ingredient in enumerate(options):
          with cols[index % 3]:
              is_selected = ingredient in st.session_state.selected_ingredients
              button_key = f"{category}-{ingredient}"

            # Apply styling
              button_style = f"""
                <style>
                    div[data-testid="stButton"][id="{button_key}"] >  button {{
                        width: 100%;
                        padding: 10px;
                        margin: 5px 0;
                        border-radius: 5px;
                        font-size: 16px;
                        font-weight: bold;
                        cursor: pointer;
                        background-color: {'red' if is_selected else 'white'};
                        color: {'#11c2f7' if is_selected else 'black'};
                        border: 2px solid #11c2f7;
                        transition: background 0.3s, color 0.3s;
                    }}
                </style>
            """
              st.markdown(button_style, unsafe_allow_html=True)

              if st.button(
                f"{'✔ ' if is_selected else ''}{ingredient}",
                key=button_key,
                help="Click to select/deselect"
               ):
                if is_selected:
                    st.session_state.selected_ingredients.remove(ingredient)
                else:
                    st.session_state.selected_ingredients.add(ingredient)
  dfs=df[df['course']=='shakes']
  ing=st.session_state.selected_ingredients
  vectorizer=TfidfVectorizer()
  ing_matrix=vectorizer.fit_transform(dfs['ingredients'])
  model=NearestNeighbors(n_neighbors=3,metric='cosine')
  model.fit(ing_matrix)
  def recommend_recipesd(user_ingredientss,dfs,model,vectorizer):
    input=" ".join(sorted(user_ingredientss))
    vector=vectorizer.transform([input])
    distances, indices=model.kneighbors(vector)
    recommended_recipes = dfs.iloc[indices[0]]
    recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
    # return recommended_recipes.sort_values(by='Similarity', ascending=False)
    # return recommended_recipes.sample(frac=1, random_state=None)
    return recommended_recipes.sort_values(by='Similarity', ascending=False)
   
  st.markdown("""                           
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #63dbeb;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;        
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 20px; /* Set font size to 50px */
    }
    
    
    .custom-button:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }

    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #f56b53;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 2px 2px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 20px; /* Increase font size for larger text */
        width: 170px;
        height: 60px;
    }

    div.stButton > button:first-child:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)
  user_ingredientss=ing
  rec = recommend_recipesd(user_ingredientss, dfs, model, vectorizer)
  print(rec)

  if user_ingredientss:
    
      for index, row in rec.iterrows():
        l,r=st.columns(2)
        with l:
          name=row['name']
          st.subheader(f":red[{name}]")
          st.image(row['img_url'], width=170)
          ingr=row['ingredients']
        with r:
          if st.button("Show Recipe:",key=f"rec_dess{index}"):
              st.session_state.recipe_name =name
              st.session_state.ing_name=ingr
            #   st.session_state.dess=row
              st.session_state.navigated = True
              st.switch_page("pages/recipe.py") 
       
  else:
      st.write(" ")
elif option=='🍕 Snacks':
  st.subheader(":red[Snacks:]")
  if 'selected_snacks_category' not in st.session_state:
      st.session_state.selected_snacks_category = "Vegetarian"
  pref=st.selectbox("Select prefences:",options=['Vegetarian','Non-Vegetarian'], index=["Vegetarian", "Non-Vegetarian"].index(st.session_state.selected_snacks_category))
  st.session_state.selected_snacks_category =pref
  if pref=='Vegetarian':


# options=['Mango','Milk','Sugar','Dark Chocolate','Banana','nuts','Pineapple','Lemon','Apple','Orange','Cocoa Powder','Baking Soda','Strawberry']
    categories = {
        "Vegetables":['Onion','Tomato','Potato','Garlic','Mushrooms','Paneer','Cheese','Carrot','Capsicum','Cabbage','Lettuce','Peas','Beans'],
        "Lentils":['Urad Daal','Chana Daal','Black Chana','Sweet Corn'],
        "Flour":['Chickpea Flour','Makki Atta','Rice Flour','Gram Flour','Wheat Flour','Moong Daal'],
        "Others":['Rava','Yoghurt','Coconut','Poha','Curd','Bread','Rice','Semolina','Nuts','Butter','Noodles','Lemon','Sabudana','Oregano','Olives','Chilli'],
        "Sauce":['Chilli Sauce','Soy Sauce','Tomato Ketchup']
    }
    if "selected_ingredients" not in st.session_state:
        st.session_state.selected_ingredients = set()

    for category, options in categories.items():
        st.subheader(category)
        cols = st.columns(3)


        for index, ingredient in enumerate(options):
            with cols[index % 3]:
                is_selected = ingredient in st.session_state.selected_ingredients
                button_keyv = f"{category}-{ingredient}"

#             # Apply styling
                button_style = f"""
                    <style>
                        div[data-testid="stButton"][id="{button_keyv}"] > button {{
                            width: 100%;
                            padding: 10px;
                            margin: 5px 0;
                            border-radius: 5px;
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                            background-color: {'red' if is_selected else 'white'};
                            color: {'#11c2f7' if is_selected else 'black'};
                            border: 2px solid #11c2f7;
                            transition: background 0.3s, color 0.3s;
                        }}
                    </style>
                """
                st.markdown(button_style, unsafe_allow_html=True)

                if st.button(
                    f"{'✔ ' if is_selected else ''}{ingredient}",
                    key=button_keyv,
                    help="Click to select/deselect"
                ):
                    if is_selected:
                        st.session_state.selected_ingredients.remove(ingredient)
                    else:
                        st.session_state.selected_ingredients.add(ingredient)
    dfs=df[df['course']=='snack']
    dfve=dfs[dfs['diet']=='vegetarian']
    ing=st.session_state.selected_ingredients
    vectorizer=TfidfVectorizer()
    ing_matrix=vectorizer.fit_transform(dfve['ingredients'])
    model=NearestNeighbors(n_neighbors=5,metric='cosine')
    model.fit(ing_matrix)
    def recommend_recipesv(user_ingredientsve,dfve,model,vectorizer):
        input=" ".join(sorted(user_ingredientsve))
        vector=vectorizer.transform([input])
        distances, indices=model.kneighbors(vector)
        recommended_recipes = dfve.iloc[indices[0]]
        recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
        # return recommended_recipes.sort_values(by='Similarity', ascending=False)
        return recommended_recipes.sort_values(by='Similarity', ascending=False)
    
    st.markdown("""                           
        <style>
        /* Custom button styling */
        .custom-button {
            background-color: #63dbeb;
            color: white;
            font-weight: bold;
            border: 2px solid #ffa500;        
            border-radius: 12px;
            padding: 1em 2em; /* Larger padding for bigger button */
            margin: 10px 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px; /* Set font size to 50px */
        }
        
        
        .custom-button:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
        }

        /* Streamlit button styling */
        div.stButton > button:first-child {
            background-color: #f56b53;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            padding: 2px 2px; /* Larger padding for bigger button */
            margin: 5px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            font-size: 20px; /* Increase font size for larger text */
            width: 140px;
            height: 60px;
        }

        div.stButton > button:first-child:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
        }
        .st-emotion-cache-atejua egexzqm0>{
        font-size:100px;
                }
        </style>
    """, unsafe_allow_html=True)
    user_ingredientsve=ing
    recv = recommend_recipesv(user_ingredientsve, dfve, model, vectorizer)
    print(recv)

    if user_ingredientsve:
    
        for index, row in recv.iterrows():
            l,r=st.columns(2)
            with l:
                name=row['name']
                st.subheader(f":red[{name}]")
                st.image(row['img_url'], width=170)
                ingr=row['ingredients']
            with r:
                if st.button("Show Recipe:",key=f"rec_dess{index}"):
                    st.session_state.recipe_name =name
                    st.session_state.ing_name=ingr
                    #   st.session_state.dess=row
                    st.session_state.navigated = True
                    st.switch_page("pages/recipe.py") 
        
   
  elif pref=='Non-Vegetarian':
    categories = {
        "Meat":['Fish','Mutton','Chicken','Prawns'],
        "Vegetables":['Tomato','Onion','Garlic','Paneer'],
        "Others":['Rava','Yoghurt','Curd','Rice','Coriander','nuts','Bread','Oregano','Chilli'],
        "Sauce":['red sauce','green chilli sauce','soya sauce']
    }
    if "selected_ingredients" not in st.session_state:
        st.session_state.selected_ingredients = set()

    for category, options in categories.items():
        st.subheader(category)
        cols = st.columns(3)


        for index, ingredient in enumerate(options):
            with cols[index % 3]:
                is_selected = ingredient in st.session_state.selected_ingredients
                button_keynv = f"{category}-{ingredient}"

    # Apply styling
                button_style = f"""
                    <style>
                        div[data-testid="stButton"] [id="{button_keynv}"] >button {{
                            width: 100%;
                            padding: 10px;
                            margin: 5px 0;
                            border-radius: 5px;
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                            background-color: {'red' if is_selected else 'white'};
                            color: {'#11c2f7' if is_selected else 'black'};
                            border: 2px solid #11c2f7;
                            transition: background 0.3s, color 0.3s;
                        }}
                    </style>
                """
                st.markdown(button_style, unsafe_allow_html=True)

                if st.button(
                    f"{'✔ ' if is_selected else ''}{ingredient}",
                    key=button_keynv,
                    help="Click to select/deselect"
                ):
                    if is_selected:
                        st.session_state.selected_ingredients.remove(ingredient)
                    else:
                        st.session_state.selected_ingredients.add(ingredient)
    dfsn=df[df['course']=='snack']
    dfnve=dfsn[dfsn['diet']=='non-vegetarian']
    ing=st.session_state.selected_ingredients
    vectorizer=TfidfVectorizer()
    ing_matrix=vectorizer.fit_transform(dfnve['ingredients'])
    model=NearestNeighbors(n_neighbors=5,metric='cosine')
    model.fit(ing_matrix)
    def recommend_recipesnv(user_ingredientsnve,dfnve,model,vectorizer):
        input=" ".join(sorted(user_ingredientsnve))
        vector=vectorizer.transform([input])
        distances, indices=model.kneighbors(vector)
        recommended_recipes = dfnve.iloc[indices[0]]
        recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
        # return recommended_recipes.sort_values(by='Similarity', ascending=False)
        return recommended_recipes.sort_values(by='Similarity', ascending=False)
    
    st.markdown("""                           
        <style>
        /* Custom button styling */
        .custom-button {
            background-color: #63dbeb;
            color: white;
            font-weight: bold;
            border: 2px solid #ffa500;        
            border-radius: 12px;
            padding: 1em 2em; /* Larger padding for bigger button */
            margin: 10px 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px; /* Set font size to 50px */
        }
        
        
        .custom-button:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
        }

        /* Streamlit button styling */
        div.stButton > button:first-child {
            background-color: #f56b53;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            padding: 2px 2px; /* Larger padding for bigger button */
            margin: 5px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            font-size: 20px; /* Increase font size for larger text */
            width: 140px;
            height: 60px;
        }

        div.stButton > button:first-child:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
        }
        .st-emotion-cache-atejua egexzqm0>{
        font-size:100px;
                }
        </style>
    """, unsafe_allow_html=True)
    user_ingredientsnve=ing
    recv = recommend_recipesnv(user_ingredientsnve, dfnve, model, vectorizer)
    print(recv)

    if user_ingredientsnve:
    
        for index, row in recv.iterrows():
            l,r=st.columns(2)
            with l:
                name=row['name']
                st.subheader(f":red[{name}]")
                st.image(row['img_url'], width=170)
                ingr=row['ingredients']
            with r:
                if st.button("Show Recipe:",key=f"rec_dess{index}"):
                    st.session_state.recipe_name =name
                    st.session_state.ing_name=ingr
                    #   st.session_state.dess=row
                    st.session_state.navigated = True
                    st.switch_page("pages/recipe.py") 
elif option=='🍛 Main Course':
  st.subheader(":red[MainCourse:]")
  if 'selected_main_category' not in st.session_state:
      st.session_state.selected_main_category = "Vegetarian"
  pref=st.selectbox("Select prefences:",options=['Vegetarian','Non-Vegetarian'],index=["Vegetarian", "Non-Vegetarian"].index(st.session_state.selected_main_category))
  st.session_state.selected_main_category =pref
  if pref=='Vegetarian':
# options=['Mango','Milk','Sugar','Dark Chocolate','Banana','nuts','Pineapple','Lemon','Apple','Orange','Cocoa Powder','Baking Soda','Strawberry']
    categories = {
        "Vegetables":['Cauliflower','Potato','Tomato','Garlic','Onion','Beans','Paneer','Peas','Lady Finger','Mushroom','Palak','Carrot','Cabbage','Capsicum'],
        "Lentils":['Urad Daal','Masoor Daal','Kidney Beans','Moong Daal','Chana Daal','Chole'],
        "Flour":['Makki Atta','Rice Flour','Wheat Flour'],
        "Others":['Rava','Yoghurt','Rice','Nuts','Butter']
    }
    if "selected_ingredients" not in st.session_state:
        st.session_state.selected_ingredients = set()

    for category, options in categories.items():
        st.subheader(category)
        cols = st.columns(3)


        for index, ingredient in enumerate(options):
            with cols[index % 3]:
                is_selected = ingredient in st.session_state.selected_ingredients
                button_keyv = f"{category}-{ingredient}"
#             # Apply styling
                button_style = f"""
                    <style>
                        div[data-testid="stButton"][id="{button_keyv}"] > button {{
                            width: 100%;
                            padding: 10px;
                            margin: 5px 0;
                            border-radius: 5px;
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                            background-color: {'red' if is_selected else 'white'};
                            color: {'#11c2f7' if is_selected else 'black'};
                            border: 2px solid #11c2f7;
                            transition: background 0.3s, color 0.3s;
                        }}
                    </style>
                """
                st.markdown(button_style, unsafe_allow_html=True)

                if st.button(
                    f"{'✔ ' if is_selected else ''}{ingredient}",
                    key=button_keyv,
                    help="Click to select/deselect"
                ):
                    if is_selected:
                        st.session_state.selected_ingredients.remove(ingredient)
                    else:
                        st.session_state.selected_ingredients.add(ingredient)
    dfm=df[df['course']=='main course']
    dfv=dfm[dfm['diet']=='vegetarian']
    ing=st.session_state.selected_ingredients
    vectorizer=TfidfVectorizer()
    ing_matrix=vectorizer.fit_transform(dfv['ingredients'])
    model=NearestNeighbors(n_neighbors=5,metric='cosine')
    model.fit(ing_matrix)
    def recommend_recipesv(user_ingredientsv,dfv,model,vectorizer):
        input=" ".join(sorted(user_ingredientsv))
        vector=vectorizer.transform([input])
        distances, indices=model.kneighbors(vector)
        recommended_recipes = dfv.iloc[indices[0]]
        recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
        # return recommended_recipes.sort_values(by='Similarity', ascending=False)
        return recommended_recipes.sort_values(by='Similarity', ascending=False)
    
    st.markdown("""                           
        <style>
        /* Custom button styling */
        .custom-button {
            background-color: #63dbeb;
            color: white;
            font-weight: bold;
            border: 2px solid #ffa500;        
            border-radius: 12px;
            padding: 1em 2em; /* Larger padding for bigger button */
            margin: 10px 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px; /* Set font size to 50px */
        }
        
        
        .custom-button:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
        }
 
        /* Streamlit button styling */
        div.stButton > button:first-child {
            background-color: #f56b53;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            padding: 2px 2px; /* Larger padding for bigger button */
            margin: 5px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            font-size: 20px; /* Increase font size for larger text */
            width: 140px;
            height: 60px;
        }

        div.stButton > button:first-child:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
        }
        .st-emotion-cache-atejua egexzqm0>{
        font-size:100px;
                }
        </style>
    """, unsafe_allow_html=True)
    user_ingredientsv=ing
    recv = recommend_recipesv(user_ingredientsv, dfv, model, vectorizer)
    print(recv)

    if user_ingredientsv:
    
        for index, row in recv.iterrows():
            l,r=st.columns(2)
            with l:
                name=row['name']
                st.subheader(f":red[{name}]")
                st.image(row['img_url'], width=170)
                ingr=row['ingredients']
            with r:
                if st.button("Show Recipe:",key=f"rec_dess{index}"):
                    st.session_state.recipe_name =name
                    st.session_state.ing_name=ingr
                    #   st.session_state.dess=row
                    st.session_state.navigated = True
                    st.switch_page("pages/recipe.py") 
        
   
  elif pref=='Non-Vegetarian':
    categories = {
        "Meat":['Fish','Mutton','Chicken','Prawns'],
        "Vegetables":['Tomato','Onion','Garlic'],
        "Others":['Rava','Yoghurt','Rice','Coriander','nuts','red sauce','green chilli sauce','soya sauce']
    }
    if "selected_ingredients" not in st.session_state:
        st.session_state.selected_ingredients = set()

    for category, options in categories.items():
        st.subheader(category)
        cols = st.columns(3)


        for index, ingredient in enumerate(options):
            with cols[index % 3]:
                is_selected = ingredient in st.session_state.selected_ingredients
                button_keynv = f"{category}-{ingredient}"

#             # Apply styling
                button_style = f"""
                    <style>
                        div[data-testid="stButton"][id="{button_keynv}"] > button {{
                            width: 100%;
                            padding: 10px;
                            margin: 5px 0;
                            border-radius: 5px;
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                            background-color: {'red' if is_selected else 'white'};
                            color: {'#11c2f7' if is_selected else 'black'};
                            border: 2px solid #11c2f7;
                            transition: background 0.3s, color 0.3s;
                        }}
                    </style>
                """
                st.markdown(button_style, unsafe_allow_html=True)

                if st.button(
                    f"{'✔ ' if is_selected else ''}{ingredient}",
                    key=button_keynv,
                    help="Click to select/deselect"
                ):
                    if is_selected:
                        st.session_state.selected_ingredients.remove(ingredient)
                    else:
                        st.session_state.selected_ingredients.add(ingredient)
    dfm=df[df['course']=='main course']
    dfnv=dfm[dfm['diet']=='non vegetarian']
    ing=st.session_state.selected_ingredients
    vectorizer=TfidfVectorizer()
    ing_matrix=vectorizer.fit_transform(dfnv['ingredients'])
    model=NearestNeighbors(n_neighbors=5,metric='cosine')
    model.fit(ing_matrix)
    def recommend_recipesnv(user_ingredientsnv,dfnv,model,vectorizer):
        input=" ".join(sorted(user_ingredientsnv))
        vector=vectorizer.transform([input])
        distances, indices=model.kneighbors(vector)
        recommended_recipes = dfnv.iloc[indices[0]]
        recommended_recipes['Similarity'] = 1 - distances[0]  # Convert distance to similarity score
        # return recommended_recipes.sort_values(by='Similarity', ascending=False)
        return recommended_recipes.sort_values(by='Similarity', ascending=False)
    
    st.markdown("""                           
        <style>
        /* Custom button styling */
        .custom-button {
            background-color: #63dbeb;
            color: white;
            font-weight: bold;
            border: 2px solid #ffa500;        
            border-radius: 12px;
            padding: 1em 2em; /* Larger padding for bigger button */
            margin: 10px 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px; /* Set font size to 50px */
        }
        
        
        .custom-button:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
        }

        /* Streamlit button styling */
        div.stButton > button:first-child {
            background-color: #f56b53;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            padding: 2px 2px; /* Larger padding for bigger button */
            margin: 5px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            font-size: 20px; /* Increase font size for larger text */
            width: 140px;
            height: 60px;
        }

        div.stButton > button:first-child:hover {
            background-color: #63dbeb;
            color: white;
            box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
        }
        .st-emotion-cache-atejua egexzqm0>{
        font-size:100px;
                }
        </style>
    """, unsafe_allow_html=True)
    user_ingredientsnv=ing
    recv = recommend_recipesnv(user_ingredientsnv, dfnv, model, vectorizer)
    print(recv)

    if user_ingredientsnv:
    
        for index, row in recv.iterrows():
            l,r=st.columns(2)
            with l:
                name=row['name']
                st.subheader(f":red[{name}]")
                st.image(row['img_url'], width=170)
                ingr=row['ingredients']
            with r:
                if st.button("Show Recipe:",key=f"rec_dess{index}"):
                    st.session_state.recipe_name =name
                    st.session_state.ing_name=ingr
                    #   st.session_state.dess=row
                    st.session_state.navigated = True
                    st.switch_page("pages/recipe.py") 
else:
    st.write("")    

        
   
       