import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
# df=pd.read_csv('ifood_new.csv')
st.set_page_config(page_title='FlavourMania',page_icon='🍴')
# st.header(":blue[FlavourMania]🍴")
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
        background-color: #f5f1f0;
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
st.sidebar.markdown("<p class='sidebar-title'>🍴 FlavourMania</p>", unsafe_allow_html=True)

# Bigger Sidebar Radio Button Options
options =(
    
    "🏠 Home","🍛 Main Course", "🍕 Snacks", "🍰 Desserts", "🍹 Shakes"
)
option=st.sidebar.radio("What you want to explore?:",options)

# def load_lottie_file(filepath):
#     with open(filepath, "r") as f:
#         return json.load(f)

# # Load the downloaded animation
# lottie_animation = load_lottie_file("animation.json")

# # Display animation
# st_lottie(lottie_animation, speed=1, width=900, height=800, key="local_animation")
if option=="🏠 Home":
 left, right=st.columns(2)
 with left:
   def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the downloaded animation
   lottie_animation = load_lottie_file("animation.json")

# Display animation
   st_lottie(lottie_animation, speed=1, width=300, height=400, key="local_animation")
 
 
 with right:
  search_query = st.text_input("Search for a dish",placeholder="🔍 Search here...",key="search")
  if search_query:
    fil_df=df[df.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
    if len(search_query)>=4:
    #  fil_df=df[df.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
     if not fil_df.empty:
      st.subheader("Search Results:")
      if len(fil_df)==1:
    #  st.write(fil_df)
    #   img=fil_df['poster'].iloc[0]
       img=fil_df['img_url'].iloc[0]
       st.image(img,width=200)
       name=fil_df['name'].iloc[0]
       st.write(name)  
       recipe=fil_df['procedure'].iloc[0]
       if st.button("Show recipe:",key='rec_left'):
         st.write(recipe)
      else:
       lef, mid = st.columns(2)
       img1=fil_df['img_url'].iloc[0]
       img2=fil_df['img_url'].iloc[1]
      
      
       n1=fil_df['name'].iloc[0]
       n2=fil_df['name'].iloc[1]
       r1=fil_df['procedure'].iloc[0]
       r2=fil_df['procedure'].iloc[1]
       lef.image(img1)
       with lef:
        st.write(n1)
        if st.button("Show recipe:",key="rec_lef"):
          st.write(r1)
       mid.image(img2)
       with mid:
        st.write(n2)
        if st.button("show recipe:",key="rec_mid"):
          st.write(r2)
     else:
       st.write("No results Found!")
    else:
      st.write("No Results!")
  else:
   st.write("")
 st.subheader(":red[Some Vegetarian dishes:]")
 l,m,r=st.columns(3)
 veg=df[df['diet']=='vegetarian']
 ra1=veg.sample(n=1)
#  st.write(rand_veg)
 r1=ra1['img_url'].iloc[0]
 na1=ra1['name'].iloc[0]
 l.image(r1,width=200)
 with l:
   st.write(na1)
   if st.button("Show Recipe:",key='rec_l'):
     st.write("")
 ra2=veg.sample(n=1)
 r2=ra2['img_url'].iloc[0]
 na2=ra2['name'].iloc[0]
 m.image(r2,width=200)
 with m:
   st.write(na2)
   if st.button("Show Recipe:",key='rec_m'):
     st.write("")
 ra3=veg.sample(n=1)
 r3=ra3['img_url'].iloc[0]
 na3=ra3['name'].iloc[0]
 r.image(r3,width=200)
 with r:
   st.write(na3)
   if st.button("Show Recipe:",key='rec_r'):
     st.write("")
 st.subheader(":red[Some Non-Vegetarian Dishes:]")
 le,me,re=st.columns(3)
 nonveg=df[df['diet']=='non vegetarian']
 ra4=nonveg.sample(n=1)
#  st.write(rand_veg)
 r4=ra4['img_url'].iloc[0]
 na4=ra4['name'].iloc[0]
 le.image(r4,width=200)
 with le:
   st.write(na4)
   if st.button("Show Recipe:",key='rec_le'):
     st.write("")
 ra5=nonveg.sample(n=1)
 r5=ra5['img_url'].iloc[0]
 na5=ra5['name'].iloc[0]
 me.image(r5,width=200)
 with me:
   st.write(na5)
   if st.button("Show Recipe:",key='rec_me'):
     st.write("")
 ra6=nonveg.sample(n=1)
 r6=ra6['img_url'].iloc[0]
 na6=ra6['name'].iloc[0]
 re.image(r6,width=200)
 with re:
   st.write(na6)
   if st.button("Show Recipe:",key='rec_re'):
     st.write("")
# if 'art_button_clicked' not in st.session_state:
#     st.session_state.art_button_clicked=False


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
if option=='🍰 Desserts':
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
    l,r=st.columns(2)
    with l:
      for index, row in rec.iterrows():
        st.subheader(f":red[{row['name']}]")
        st.image(row['img_url'], width=170)
    with m:
      if st.button("Show Recipe:"):
        st.write("")