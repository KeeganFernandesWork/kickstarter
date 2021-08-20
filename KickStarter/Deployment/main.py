import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

category = ['Publishing', 'Film & Video' ,'Music' ,'Food', 'Design' ,'Crafts' ,'Games',
 'Comics' ,'Fashion' ,'Theater', 'Art', 'Photography', 'Technology', 'Dance',
 'Journalism']
currency = ['GBP', 'USD' ,'CAD', 'AUD' ,'NOK' ,'EUR', 'MXN' ,'SEK' ,'NZD', 'CHF' ,'DKK' ,'HKD',
 'SGD' ,'JPY']
state = ['failed' ,'canceled', 'successful', 'live' ,'undefined', 'suspended']
country = ['GB', 'US' ,'CA', 'AU' ,'NO' ,'IT', 'DE', 'IE', 'MX', 'ES', 'N,0"', 'SE' ,'FR', 'NL',
 'NZ' ,'CH', 'AT', 'DK' ,'BE' ,'HK' ,'LU', 'SG', 'JP']



le = LabelEncoder()
model = pickle.load(open("../Models/model.sav", "rb"))
cat= []



st.title("KickStarter Project Future")
#categorical
cat.append(st.selectbox("category", options=category))
cat.append(st.selectbox("currency" , options = currency))
cat.append(st.selectbox("country" , options = country))

#Numerical
goal = st.text_input("Goal" , value = 50000)
pledged = st.text_input("Pledged" , value = 10000)
backers = st.text_input("Backers" , value = 100)
days_apart = st.text_input("Days Apart" , value = 30)


i = 0
if st.button("Submit"):
 for x in [category,currency,country]:
  le.fit(x)
  cat[i] = le.transform([cat[i]])
  i = i +1
 df = pd.DataFrame({
  "main_category": [cat[0]],
  "currency":[cat[1]],
  "country":[cat[2]],
  "goal":[goal],
  "pledged":[pledged],
  "backers":[backers],
  "days_apart":[days_apart]
 })
 le.fit(state)
 prediction = model.predict(df)

 st.write(le.inverse_transform([prediction]))


