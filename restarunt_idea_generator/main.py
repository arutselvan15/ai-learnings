import streamlit as st
import langchain_helper as lh
from dotenv import load_dotenv


def main():
    load_dotenv()

    st.title("Restaurant Name Generator")

    cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American", "Arabic"))

    if cuisine:
        response = lh.generate_restaurant_name_and_items(cuisine)

        st.header(response["restaurant_name"].strip())
        menu_items = response["menu_items"].strip().split(",")
        st.write("**Menu Items**")

        for item in menu_items:
            st.write(item)


if __name__ == '__main__':
    main()
