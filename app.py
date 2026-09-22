import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title='Employee Salary Prediction', page_icon='💼')
st.title('Employee Salary Prediction')
st.write('Enter employee details to predict salary.')

model = joblib.load('employee_salary_model.joblib')

departments = ['Engineering', 'Finance', 'HR', 'Marketing', 'Sales', 'Support']
cities = ['Bhaktapur', 'Biratnagar', 'Butwal', 'Dharan', 'Hetauda', 'Kathmandu', 'Lalitpur', 'Pokhara']

age = st.number_input('Age', min_value=21.0, max_value=45.0, value=30.0)
department = st.selectbox('Department', departments)
city = st.selectbox('City', cities)
score = st.number_input('Score', min_value=60.0, max_value=95.0, value=75.0)

if st.button('Predict Salary'):
    input_data = pd.DataFrame([{
        'age': age,
        'department': department,
        'city': city,
        'score': score,
    }])
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Salary: {prediction:,.2f}')