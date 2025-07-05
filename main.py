import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from  sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.neighbors import NearestNeighbors
# df=pd.read_csv('ifood_new.csv')
st.set_page_config(page_title='FlavourMania',page_icon='🍴')
# st.header(":blue[FlavourMania]🍴")
df=pd.read_csv("ifood_new.csv")

# st.sidebar.markdown("<p class='sidebar-title'>🍴 FlavourMania</p>", unsafe_allow_html=True)

st.markdown("""
    <style>
        #custom-header {
            position: absolute;
            top: 30px;     /* Y-axis */
            left: 40px;   /* X-axis */
            color: red;
            font-size: 36px;
            font-weight: bold;
            z-index: 10000;
        }
    </style>

    <div id="custom-header">🍴 FlavourMania</div>
""", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: red;'>🍴 FlavourMania</h1>", unsafe_allow_html=True)

# Sidebar Title
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the downloaded animation
lottie_animation = load_lottie_file("animation.json")

# Display animation
# st_lottie(lottie_animation, speed=1, width=900, height=800, key="local_animation")
# if option=="🏠 Home":
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
       fil_df=df[df.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
       img=fil_df['img_url'].iloc[0]
       st.image(img,width=200)
       name=fil_df['name'].iloc[0]
       recipe=fil_df['procedure'].iloc[0]
       ing=fil_df['ingredients'].iloc[0]
       st.write(name)
       if "navigated" not in st.session_state:
         st.session_state.navigated = False
      #  recipe=fil_df['procedure'].iloc[0]
       if st.button("Show recipe:",key='rec_left'):
          st.session_state.recipe_name = name
          st.session_state.ing_name =ing
          st.session_state.navigated = True
          st.switch_page("pages/recipe.py")
      else:
       lef, mid = st.columns(2)
       img1=fil_df['img_url'].iloc[0]
       img2=fil_df['img_url'].iloc[1]
      
      
       n1=fil_df['name'].iloc[0]
       n2=fil_df['name'].iloc[1]

       r1=fil_df['procedure'].iloc[0]
       r2=fil_df['procedure'].iloc[1]

       i1=fil_df['ingredients'].iloc[0]
       i2=fil_df['ingredients'].iloc[1]
       lef.image(img1)
       with lef:
        st.write(n1)
        if "navigated" not in st.session_state:
         st.session_state.navigated = False
        if st.button("Show recipe:",key="rec_lef"):
          st.session_state.recipe_name =n1
          st.session_state.ing_name=i1
          st.session_state.navigated = True
          st.switch_page("pages/recipe.py")
       mid.image(img2)
       with mid:
         st.write(n2)
         if "navigated" not in st.session_state:
            st.session_state.navigated = False
         if st.button("Show recipe:",key="rec_mid"):
            st.session_state.recipe_name =n2
            
            st.session_state.ing_name=i2
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
     else:
       st.write("No results Found!")
    else:
      st.write("No Results!")
  else:
   st.write("")
st.subheader(":red[Some Vegetarian dishes:]")
l,m,r=st.columns(3)
veg=df[df['diet']=='vegetarian']
 
if "random_dish1" not in st.session_state:
    ra1 = veg.sample(n=1)
    st.session_state.random_dish1 = {
        "img_url": ra1['img_url'].iloc[0],
        "name": ra1['name'].iloc[0],
        "ingredients":ra1['ingredients'].iloc[0]
    }  

r1 = st.session_state.random_dish1["img_url"]
na1 = st.session_state.random_dish1["name"]
in1=st.session_state.random_dish1["ingredients"]


l.image(r1,width=200)
with l:
   st.write(na1)                          
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_l"):
            st.session_state.recipe_name =na1
            st.session_state.ing_name=in1
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
            # 2nd veg
if "random_dish2" not in st.session_state:
    ra2 = veg.sample(n=1)
    st.session_state.random_dish2 = {
        "img_url": ra2['img_url'].iloc[0],
        "name": ra2['name'].iloc[0],
        "ingredients":ra2['ingredients'].iloc[0]
    }  

r2 = st.session_state.random_dish2["img_url"]
na2 = st.session_state.random_dish2["name"]
in2=st.session_state.random_dish2["ingredients"]

m.image(r2,width=200)
with m:
   st.write(na2)
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_m"):
            st.session_state.recipe_name =na2
            st.session_state.ing_name=in2
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
            # 3rd veg 
if "random_dish3" not in st.session_state:
    ra3 = veg.sample(n=1)
    st.session_state.random_dish3 = {
        "img_url": ra3['img_url'].iloc[0],
        "name": ra3['name'].iloc[0],
         "ingredients":ra3['ingredients'].iloc[0]
    }  

r3 = st.session_state.random_dish3["img_url"]
na3 = st.session_state.random_dish3["name"]
in3=st.session_state.random_dish3["ingredients"]
r.image(r3,width=200)
with r:
   st.write(na3)
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_r"):
            st.session_state.recipe_name =na3
            st.session_state.ing_name=in3
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
st.subheader(":red[Some Non-Vegetarian Dishes:]")
le,me,re=st.columns(3)
nonveg=df[df['diet']=='non vegetarian']
# 1st non veg
if "random_dish4" not in st.session_state:
    ra4 = nonveg.sample(n=1)
    st.session_state.random_dish4 = {
        "img_url": ra4['img_url'].iloc[0],
        "name": ra4['name'].iloc[0],
        "ingredients":ra4['ingredients'].iloc[0]
    }  

ri4 = st.session_state.random_dish4["img_url"]
non4= st.session_state.random_dish4["name"]
in4=st.session_state.random_dish4["ingredients"]
le.image(ri4,width=200)
with le:
   st.write(non4)
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_le"):
            st.session_state.recipe_name =non4
            st.session_state.ing_name=in4
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
            # 2nd non veg
if "random_dish5" not in st.session_state:
    ra5 = nonveg.sample(n=1)
    st.session_state.random_dish5 = {
        "img_url": ra5['img_url'].iloc[0],
        "name": ra5['name'].iloc[0],
         "ingredients":ra5['ingredients'].iloc[0]
    }  

ri5 = st.session_state.random_dish5["img_url"]
non5 = st.session_state.random_dish5["name"]
in5=st.session_state.random_dish5["ingredients"]
me.image(ri5,width=200)
with me:
   st.write(non5)
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_me"):
            st.session_state.recipe_name =non5
            st.session_state.ing_name=in5
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
            # 3rd non veg
 
if "random_dish6" not in st.session_state:
    ra6 = nonveg.sample(n=1)
    st.session_state.random_dish6 = {
        "img_url": ra6['img_url'].iloc[0],
        "name": ra6['name'].iloc[0],
         "ingredients":ra6['ingredients'].iloc[0]
    }  

ri6 = st.session_state.random_dish6["img_url"]
non6 = st.session_state.random_dish6["name"]
in6=st.session_state.random_dish6["ingredients"]
re.image(ri6,width=200)
with re:
   st.write(non6)
   if "navigated" not in st.session_state:
            st.session_state.navigated = False
   if st.button("Show recipe:",key="rec_re"):
            st.session_state.recipe_name =non6
            st.session_state.ing_name=in6
            st.session_state.navigated = True
            st.switch_page("pages/recipe.py")
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
