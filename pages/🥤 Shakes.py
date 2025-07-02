import streamlit as st
import pandas as pd
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
# df=pd.read_csv('ifood_new.csv')
# st.set_page_config(page_title='FlavourMania',page_icon='🍴')
# st.header(":blue[FlavourMania]🍴")
df=pd.read_csv("ifood_new.csv")
# https://www.shutterstock.com/image-photo/strawberry-banana-smoothie-splash-copy-260nw-252166555.jpg
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-fruit-smoothies-for-good-health-image_2898573.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)

st.subheader(":red[Shakes And Drinks:]")
# options=['Mango','Milk','Sugar','Dark Chocolate','Banana','nuts','Pineapple','Lemon','Apple','Orange','Cocoa Powder','Baking Soda','Strawberry']
categories = {
    "Fruits": ["Pineapple","Strawberry","Banana","Apple","Orange","Mango","Lemon","Nuts"],
    "Essentials":['Milk','Sugar','Chocolate','Cocoa Powder','Soda']
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
                st.rerun()
import re
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
    pattern = r'(' + r'|'.join(re.escape(ui) for ui in user_ingredientss) + r')'

# filter by whether the ingredients string contains any of them, case-insensitive
    recommended_recipes = recommended_recipes[
            recommended_recipes['ingredients']
                .str.contains(pattern, case=False, regex=True)
        ]
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

        