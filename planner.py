import os
os.environ[ "STREAMLIT_SERVER_RUN_ON_SAVE" ] = "false"

import streamlit as st
import google.generativeai as gg
import streamlit_option_menu as smom

st.set_page_config( layout = "wide" )

gg.configure( api_key = "YOUR_API_KEY_HERE" )
model = gg.GenerativeModel( "gemini-1.5-pro" )

option = smom.option_menu(
    "Menu",
    [ "Describe Mode", "Select Mode" ],
    icons = [ "chat", "list" ],
    menu_icon = "cast"
)

if option == "Describe Mode":
    st.title( "Meal Planner || Describe Mode" )
    st.write( "Please describe what you want to eat in a few sentences. Be specific." )

    meal_description = st.text_area( "What do you want to eat?" )

    if st.button( "Submit" ) and meal_description.strip():
        prompt = f"""
        Find a complete recipe based on the following meal description.
        Include ingredients, step-by-step instructions, and estimated prep time.

        Meal description:
        {meal_description}
        """

        response = model.generate_content( [ prompt ] )

        st.subheader( "Here is the meal plan" )
        st.write( response.text )

elif option == "Select Mode":
    st.title( "Meal Planner || Select Mode" )

    country = st.text_input( "What country do you want the recipe from?" )
    prep_time = st.slider( "Preparation time (minutes)", 5, 300 )
    people_served = st.slider( "Number of people served", 1, 10 )
    dietary_restrictions = st.multiselect(
        "Dietary restrictions",
        [ "vegetarian", "vegan", "gluten free", "dairy free", "nut free", "soy free" ]
    )
    ingredients = st.text_input( "Ingredients you want to include" )

    if st.button( "Submit" ):
        prompt = f"""
        Create a detailed recipe with the following constraints:

        Cuisine country: {country}
        Preparation time: {prep_time} minutes
        Serves: {people_served} people
        Dietary restrictions: {", ".join( dietary_restrictions ) if dietary_restrictions else "none"}
        Ingredients to include: {ingredients}

        Include ingredients list, step-by-step cooking instructions, and tips.
        """

        response = model.generate_content( [ prompt ] )

        st.subheader( "Here is the meal plan" )
        st.write( response.text )

