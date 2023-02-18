import streamlit;
import requests
import pandas
import snowflake.connector


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
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvise Fruit Advice')
fruit_choice = streamlit.text_input('what fruit would you like information about?','kiwi')

streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])


item = streamlit.text_area('Enter fruit',"");
streamlit.write('The user entered', item);
my_cur = my_cnx.cursor()
my_cur.execute("INSERT INTO fruit_load_list(item) VALUES (%s)", (item,))
my_cur.commit()

my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("fruit load list contain:")
streamlit.dataframe(my_data_row)
 
 
 
