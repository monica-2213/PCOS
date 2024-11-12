import streamlit as st

# Page configuration
st.set_page_config(page_title='PCOS Diagnosis', page_icon=':stethoscope:', layout="centered")

# Title and introduction with background color
st.markdown("<h1 style='text-align: center; color: #8A2BE2;'>PCOS Diagnosis and Treatment Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B0082;'>Answer the questions below to receive a preliminary assessment for PCOS risk.</p>", unsafe_allow_html=True)

# Collecting user information with sections and subtle colors
st.markdown("<h2 style='color: #8B0000;'>Personal Information</h2>", unsafe_allow_html=True)
age = st.slider('What is your age?', 10, 100)
BMI = st.slider('What is your BMI?', 15, 50)

# Section for symptoms and related questions with organized layout
st.markdown("<h2 style='color: #8B0000;'>Symptoms and Lifestyle Factors</h2>", unsafe_allow_html=True)
cycles = st.slider('How many menstrual cycles do you have in a year?', 0, 12)
acne = st.selectbox('Do you have acne?', ('Yes', 'No'))
hair_growth = st.selectbox('Do you have excessive hair growth?', ('Yes', 'No'))
weight_gain = st.selectbox('Have you experienced unexplained weight gain?', ('Yes', 'No'))
male_balding = st.selectbox('Have you experienced male-pattern balding?', ('Yes', 'No'))

# Function to calculate risk percentage for PCOS
def calculate_pcos_risk():
    risk_score = 0
    if cycles < 8:
        risk_score += 40
    if BMI > 30:
        risk_score += 20
    if acne == 'Yes':
        risk_score += 10
    if hair_growth == 'Yes':
        risk_score += 10
    if weight_gain == 'Yes':
        risk_score += 10
    if male_balding == 'Yes':
        risk_score += 10
    return min(risk_score, 100)

# Button to check results
if st.button('Check PCOS Risk'):
    risk_percentage = calculate_pcos_risk()
    
    # Display risk assessment
    st.markdown(f"<h3 style='color: #FF4500;'>PCOS Risk Assessment: {risk_percentage}%</h3>", unsafe_allow_html=True)
    
    # Display diagnosis suggestion based on risk percentage
    if risk_percentage >= 50:
        st.markdown("<p style='color: #B22222;'>There is a higher risk that you may have PCOS. We recommend scheduling an appointment with your doctor for further testing and evaluation.</p>", unsafe_allow_html=True)
        
        # Medical test recommendations
        st.markdown("<h3 style='color: #8A2BE2;'>Recommended Medical Tests:</h3>", unsafe_allow_html=True)
        st.write('- Blood tests to check hormone levels')
        st.write('- Ultrasound to examine your ovaries')
        st.write('- Glucose tolerance test to check for diabetes')
        st.write('- Lipid profile to check for high cholesterol')
        
        # Treatment recommendations
        st.markdown("<h3 style='color: #8A2BE2;'>Recommended Treatments:</h3>", unsafe_allow_html=True)
        st.write('- Birth control pills to regulate menstrual cycles')
        st.write('- Metformin to regulate insulin levels')
        st.write('- Spironolactone to reduce acne and excess hair growth')
        st.write('- Clomiphene citrate to induce ovulation')
    else:
        st.markdown("<p style='color: #006400;'>Based on your responses, it is unlikely that you have PCOS. However, we recommend speaking with your doctor if you have concerns about your menstrual cycle or other symptoms.</p>", unsafe_allow_html=True)

# Lifestyle change recommendations
st.markdown("<h3 style='color: #8A2BE2;'>Lifestyle Changes to Manage PCOS:</h3>", unsafe_allow_html=True)
st.write('- Eating a healthy, balanced diet')
st.write('- Engaging in regular physical activity')
st.write('- Maintaining a healthy weight')
st.write('- Managing stress levels')

# Disclaimer
st.markdown("<p style='color: #808080;'>This PCOS Diagnosis and Treatment Recommendation System is designed to provide preliminary insights and is not a substitute for professional medical advice and evaluation.</p>", unsafe_allow_html=True)
