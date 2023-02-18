import streamlit;
import requests
import pandas
import snowflake.connector
from urllib.error import URLError


streamlit.title('My parents New Healthy Diner')

streamlit.header('BreakFast Favourites🍕🍟🍔 ')
streamlit.text('pizza 🍕')
streamlit.text('Egg 🥚')
streamlit.text('Hot dog 🌭')
streamlit.text('Avacado toast 🥑🥪')

streamlit.header('🍓🍌🍎 making my own smoothie 🍹🥤🧃')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a picklist
fruit_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index), ['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvise Fruit Advice')
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?','kiwi')
  if not fruit_choice:
       streamlit.error("please select fruit to get information.")
  else:
      #display API response
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)

except URLError as e:
     streamlit.error()

#dont run anything till here
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("fruit load list contain:")
streamlit.dataframe(my_data_row)

item = streamlit.text_input('What fruit would u like to enter?',"");
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
streamlit.write('Thanks for adding', item)



 
 
 
