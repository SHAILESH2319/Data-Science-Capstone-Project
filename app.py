import streamlit as st
import pandas as pd
import pickle
import numpy as np

model=pickle.load(open('lr (1).pkl','rb'))

def main():
     # Set page config
    st.set_page_config(
        page_title="🚗car price prediction🚗",
        page_icon=":car:",
        layout="centered",
        #background_color="#FFA500" # Orange background color
        )
  


    df=pd.read_csv('CAR DETAILS.csv')
    cars=(df['name'].unique())
    transmission=(df['transmission'].unique())
    seller=(df['seller_type'].unique())
    owner=(df['owner'].unique())
    fuel=(df['fuel'].unique())

    p2=st.slider('Model Year',2005,2020,2005)
    p3=(st.slider('KM Driven',500,10000000,500))

    p4=st.selectbox('Seller Type',seller)
    if p4=='Individual':
        p4=1
    elif p4=='Dealer':
        p4=0
    elif p4=='Trustmark Dealer':
        p4=2

    p5=st.selectbox('Owner Type',owner)
    if p5=='First Owner':
        p5=0
    elif p5=='Second Owner':
        p5=2
    elif p5=='Third Owner':
        p5=4
    elif p5=='Fourth & Above Owner':
        p5=1
    elif p5=='Test Drive Car':
        p5=3

    p6=st.selectbox('Transmission Type',transmission)
    if p6=='Manual':
        p6=1
    elif p6=='Automatic':
        p6=0

    p7=st.selectbox('Fuel Type',fuel)
    if p7=='Petrol':
        p7=4
    elif p7=='Diesel':
        p7=1
    elif p7=='CNG':
        p7=0
    elif p7=='LPG':
        p7=3
    elif p7=='Electric':
        p7=2

    

    x=pd.DataFrame({'year':[p2],'km_driven':[p7],'fuel':[p6],'seller_type':[p3],
                    'transmission':[p5],'owner':[p4]})
    final=st.button('Predict Car Price')
    if final:
        prediction=model.predict(x)
        prediction=model.predict(x)
        st.success('Predicted Car Price:'+str( prediction) +'Rupees')
     

if __name__=='__main__':
    main()
