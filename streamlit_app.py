import streamlit;
import pandas


streamlit.title('My parents New Healthy Diner')

streamlit.header('BreakFast Favourites🍕🍟🍔 ')
streamlit.text('pizza 🍕')
streamlit.text('Egg 🥚')
streamlit.text('Hot dog 🌭')
streamlit.text('Avacado toast 🥑🥪')

streamlit.header('🍓🍌🍎 making my own smoothie 🍹🥤🧃')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
 
 
 
