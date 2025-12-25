import streamlit as st
import google.generativeai as gg
import streamlit_option_menu as smom

st.set_page_config( layout = "wide" )
option = smom.option_menu( "Menu", [ "Describe Mode", "Select Mode" ] )

gg.configure( api_key = "AIzaSyA4O1-zyvh5PdWvQUt4hjTd1R5z6xI5A9w" )
model = gg.GenerativeModel( "gemini-1.5-pro" )

if option == "Describe Mode":
    st.title( "Meal Planner || Describe Mode" )
    st.write( "Please tell our experts what you want to eat. In a few sentences. Please be specific." )
    meal_description = st.text_area( "What do you want to eat?" )

    if st.button( "Submit" ):
        prompt = f"please find a recipie for the following meal description {meal_description}"
        model.generate_content( [ prompt ] )
        st.write( "Here is the meal plan" )
        st.write( model.generate_content( [ prompt ] ).text )

elif option == "Select Mode":
    st.title( "Meal Planner || Select Mode" )
    
    country = st.text_input( "What country do you want to find a recipie from?" )
    prep_time = st.slider( "How long should it take to prepare the meal( in minutes ) ?", 5, 300 )
    people_served = st.slider( "How many people will be served?", 1, 5 )
    dietary_restrictions = st.multiselect( "What are the dietary restrictions?", [ "vegetarian", "vegan", "gluten free", "dairy free", "nut free", "soy free" ] )
    ingrediants = st.text_input( "What some ingredients you want to include in the meal?" )

    if st.button( "Submit" ):
        prompt = f"""please find a recipie for a {country} meal that takes {prep_time} minutes to prepare
          and serves {people_served} people. The meal should have the following dietary restrictions {dietary_restrictions}
            and include the following ingredients {ingrediants}"""
        responce = model.generate_content( [ prompt ] )
        st.write( "Here is the meal plan" )
        st.write( responce.text )

