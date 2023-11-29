import streamlit as st
from handler import *

st.title("Computer Graphics Algorithms")

st.subheader("Choose your algorithm: ")
option = st.selectbox(
    'Select One',
    ('DDA', 'Bresenham', 'Mid Point Circle', 'Mid Point Ellipse', 'Rotation', 'Scaling', 'Translation'))

button1 = st.button('Lets Go!')
if st.session_state.get('button') != True:

    st.session_state['button'] = button1

if (st.session_state['button'] == True):
    if option=="DDA":
        number1 = st.number_input('Input x1', key='__first__', min_value=0, step=1)
        number2 = st.number_input('Input y1', key='__second__', min_value=0, step=1)
        number3 = st.number_input('Input x2', key='__third__', min_value=0, step=1)
        number4 = st.number_input('Input y2', key='__fourth__', min_value=0, step=1)

        if st.button('Run!'):
            handle_request.handle_DDA(number1, number2, number3, number4)
        
    elif option == "Bresenham":
        number1 = st.number_input('Input x1', key='__bre_first__', min_value=0, step=1)
        number2 = st.number_input('Input y1', key='__bre_second__', min_value=0, step=1)
        number3 = st.number_input('Input x2', key='__bre_third__', min_value=0, step=1)
        number4 = st.number_input('Input y2', key='__bre_fourth__', min_value=0, step=1)

        if st.button('Run!'):
            handle_request.handle_Bresenham(number1, number2, number3, number4)

    elif option == 'Mid Point Circle':
        number1 = st.number_input("x-coordinate of the center: ", min_value=0, step=1)
        number2 = st.number_input("y-coordinate of the center: ", min_value=0, step=1)
        number3 = st.number_input("Radius of the center: ", min_value=0, step=1)
        if st.button('Run!'):
            handle_request.handle_circle(number1, number2, number3)
