import streamlit;
import requests
import pandas
import snowflake.connector
from urllib.error import URLError


streamlit.title('My parents New Healthy Diner')

streamlit.header('BreakFast Favouritesπππ ')
streamlit.text('pizza π')
streamlit.text('Egg π₯')
streamlit.text('Hot dog π­')
streamlit.text('Avacado toast π₯π₯ͺ')

streamlit.header('πππ making my own smoothie πΉπ₯€π§')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a picklist
fruit_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index), ['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvise Fruit Advice')
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("please select fruit to get information.")
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)

except URLError as e:
     streamlit.error()

#dont run anything till here
# streamlit.stop()

streamlit.header('The fruitlist contain:')

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()
    
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
      return "Thanks for adding" + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would u like to enter?',"");

if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  bac_from_button = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(bac_from_button)
 
 
