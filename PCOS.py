import streamlit as st

# Title and introduction
st.title('PCOS Diagnosis and Treatment Recommendation System')
st.write('Please answer the following questions to receive a preliminary risk assessment for PCOS.')

# User input for symptoms and factors
age = st.slider('What is your age?', 10, 100)
BMI = st.slider('What is your BMI?', 15, 50)  # Set a more typical BMI range
cycles = st.slider('How many menstrual cycles do you have in a year?', 0, 25)  # 0-12 cycles per year for reasonable assessment
acne = st.selectbox('Do you have acne?', ('Yes', 'No'))
hair_growth = st.selectbox('Do you have excessive hair growth?', ('Yes', 'No'))
weight_gain = st.selectbox('Have you experienced unexplained weight gain?', ('Yes', 'No'))
male_balding = st.selectbox('Have you experienced male-pattern balding?', ('Yes', 'No'))

# Define a function to calculate risk percentage
def calculate_pcos_risk():
    risk_score = 0

    # Assign weights to each factor for PCOS risk assessment
    if cycles < 8:
        risk_score += 40  # Irregular cycles contribute significantly to risk
    if BMI > 30:
        risk_score += 20  # Higher BMI is a known risk factor
    if acne == 'Yes':
        risk_score += 10
    if hair_growth == 'Yes':
        risk_score += 10
    if weight_gain == 'Yes':
        risk_score += 10
    if male_balding == 'Yes':
        risk_score += 10

    # Cap the risk percentage at 100%
    return min(risk_score, 100)

# Button to check the results
if st.button('Check PCOS Risk'):
    risk_percentage = calculate_pcos_risk()
    
    # Display risk assessment
    st.write(f'**PCOS Risk Assessment:** {risk_percentage}%')
    
    # Display diagnosis suggestion based on risk percentage
    if risk_percentage >= 50:
        st.write('Based on your responses, there is a higher risk that you may have PCOS. We recommend scheduling an appointment with your doctor for further testing and evaluation.')
        
        # Medical test recommendations
        st.write('We recommend the following medical tests and screenings to help diagnose PCOS:')
        st.write('- Blood tests to check hormone levels')
        st.write('- Ultrasound to examine your ovaries')
        st.write('- Glucose tolerance test to check for diabetes')
        st.write('- Lipid profile to check for high cholesterol')
        
        # Treatment recommendations
        st.write('The following treatments may be recommended based on your individual condition and medical history:')
        st.write('- Birth control pills to regulate menstrual cycles')
        st.write('- Metformin to regulate insulin levels')
        st.write('- Spironolactone to reduce acne and excess hair growth')
        st.write('- Clomiphene citrate to induce ovulation')
    else:
        st.write('Based on your responses, it is unlikely that you have PCOS. However, we recommend speaking with your doctor if you have concerns about your menstrual cycle or other symptoms.')

# Lifestyle change recommendations
st.write('In addition to medical treatments, lifestyle changes may help manage symptoms of PCOS and prevent recurrence:')
st.write('- Eating a healthy, balanced diet')
st.write('- Engaging in regular physical activity')
st.write('- Maintaining a healthy weight')
st.write('- Managing stress levels')

# Disclaimer
st.write('This PCOS Diagnosis and Treatment Recommendation System provides preliminary insights but is not a substitute for professional medical advice and evaluation.')
