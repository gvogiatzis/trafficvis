import streamlit as st
from streamlit_option_menu import option_menu
from apps import page1, page2
from PIL import Image
import streamlit as st  # pip install streamlit

# import streamlit_authenticator as stauth  # pip install streamlit-authenticator
st.set_page_config(page_title="Streamlit Geospatial", layout="wide")
image = Image.open(
    r"images-removebg-preview.png"
)
# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    # {"func": home.app, "title": "Home", "icon": "house"},
    {"func": page1.app, "title": "Traffic Analytics Tool", "icon": ""},
    {"func": page2.app, "title": "AI Traffic Controller", "icon": ""},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    st.image(image)
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    # st.sidebar.title("About")
    # st.sidebar.info(
    #     """
    #     This web [app](https://share.streamlit.io/giswqs/streamlit-template) is maintained by [Qiusheng Wu](https://wetlands.io). You can follow me on social media:
    #         [GitHub](https://github.com/giswqs) | [Twitter](https://twitter.com/giswqs) | [YouTube](https://www.youtube.com/c/QiushengWu) | [LinkedIn](https://www.linkedin.com/in/qiushengwu).
        
    #     Source code: <https://github.com/giswqs/streamlit-template>

    #     More menu icons: <https://icons.getbootstrap.com>
    # """
    # )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break


