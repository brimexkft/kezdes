import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Kép hozzáadása a főképernyőn
st.sidebar.image(r"C:\Digit nagyker\kepek\ED_nagy.jpg")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu(
        "Vezérlőpult", 
        ["Kezdőlap", 'Árlisták', "Kukucska", "Árajánlatok", "Garanciajegyek", "UNAS rendelések", "Árazó program", "Digit webshop frissítése"], 
        icons=['house', 'card-list', 'binoculars', 'newspaper', 'gear'], 
        menu_icon="cast", 
        default_index=1,
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#018bd4"},
        }
    )

# Fájlok betöltése a kiválasztás alapján
if selected == "Kezdőlap":
    st.title("Üdvözöllek a Kezdőlapon!")
elif selected == "Árlisták":
    #st.title("Itt találhatók az Árlisták")
    exec(open("C:/Digit nagyker/arukereso4.py", encoding="utf-8").read())
elif selected == "Kukucska":
    #st.title("Kukucska tartalom")
    exec(open("C:/Digit nagyker/arukereso4.py", encoding="utf-8").read())
elif selected == "Árajánlatok":
    # Az Árajánlat.py fájl tartalmának betöltése
    exec(open("C:/Digit nagyker/arajanlat1.py", encoding="utf-8").read())
elif selected == "Garanciajegyek":
    # Az Árajánlat.py fájl tartalmának betöltése
    exec(open("C:/Digit nagyker/egyesites_modified_4.py", encoding="utf-8").read())
elif selected == "UNAS rendelések":
    # Az Árajánlat.py fájl tartalmának betöltése
    exec(open("C:/Digit nagyker/UNAS_arazas.py", encoding="utf-8").read())    
elif selected == "Árazó program":
    # Az Árajánlat.py fájl tartalmának betöltése
    exec(open("C:/Digit nagyker/arcimke_3_6.py", encoding="utf-8").read())
elif selected == "Digit webshop frissítése":
    # Az Árajánlat.py fájl tartalmának betöltése
    exec(open("C:/Digit nagyker/digit webshop frissites.py", encoding="utf-8").read())


