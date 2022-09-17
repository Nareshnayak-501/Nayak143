import streanlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')
ip = st.text_input('Enter Your Message')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
