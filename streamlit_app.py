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
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index), ['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
 
 
 
