# Default 
from numpy import empty
import streamlit as st 
st.set_page_config(layout="wide")
page = st.sidebar.selectbox("Choose your page", ["Home", "About", "Rate Subjects"]) 

# --- - - - - - Logic Part --- - - - - -
department = {
    "Information Technology" : {},
    "Artificial Intelligence and Data Science" : {},
    "Electronics and Communication Engineering" : {},
    "Mechanical Engineering" : {},
    "Computer Science Engineering" : {},
    "Computer Science and Business System" : {}
    }


# --- - - - - - Home Page --- - - - - -
if page == "Home":
    st.markdown("<h2 style='text-align: center; color: #ccc; margin-top : -50px; margin-bottom: 20px'>Welcome Student</h2>", unsafe_allow_html=True)
    # Name columns
    name_col,roll_col,depart_col = st.columns(3)
    with name_col:
        student_name = st.text_input("Enter your name : ")
    with roll_col:
        student_rollno = st.text_input("Enter your roll no : ")
    with depart_col:
        student_department = st.selectbox("What's your Department : ",("Information Technology", "Artificial Intelligence and Data Science", "Computer Science Engineering", "Electronics and Communication Engineering", "Computer Science and Business System", "Mechanical Engineering"))
    submit_details = st.button("Submit")
    
    if submit_details:
        st.success("Submitted!")
        st.success(f"""
                Name : {student_name}\n
                Rollno : {student_rollno}\n
                Department : {student_department}
                """)


# --- - - - - - About Page --- - - - - -
elif page == "About":
    st.markdown("<h2 style='text-align: center; color: #ccc; margin-top : -50px; margin-bottom: 20px'>About Us</h2>", unsafe_allow_html=True)


# --- - - - - - Rate System Page --- - - - - -
elif page == "Rate Subjects":
    st.markdown("<h2 style='text-align: center; color: #ccc; margin-top : -50px; margin-bottom: 20px'>Student Feedback System</h2>", unsafe_allow_html=True)
    # Rate System Page
    sub_coloum,emp1 = st.columns([3,4])
    with sub_coloum:
        subject_selection =  st.selectbox("Select a subject which you want to rate",("Professional English","Engineering Physics","Engineering Chemistry","Matrices and Calculus", "Python Programming and Problem Solving"))
    with emp1:
        st.markdown(f"<h6 style='text-align: center; color: #4BB543; margin-top : 40px'>You selected {subject_selection}</h6>", unsafe_allow_html=True)
    
    st.markdown("<h3 style ='margin-top : 30px'>Questions</h3>", unsafe_allow_html=True)
    rate_select,emp3 = st.columns([3,2])
    if subject_selection == "Professional English":
        with rate_select:
            ques_1 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            ques_2 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_3 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_4 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_5 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_6 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_7 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_8 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_9 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_10 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_11 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_12 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_13 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            # ques_14 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
            # ques_15 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
        with emp3:
            st.empty()
    if subject_selection == "Python Programming and Problem Solving":
        with rate_select:
            ques_1 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            ques_2 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
        with emp3:
            st.empty()
    if subject_selection == "Engineering Chemistry":
        with rate_select:
            ques_1 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            ques_2 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
        with emp3:
            st.empty()
    if subject_selection == "Matrices and Calculus":
        with rate_select:
            ques_1 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            ques_2 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
        with emp3:
            st.empty()
    if subject_selection == "Engineering Physics":
        with rate_select:
            ques_1 = st.selectbox("How's your teacher explains in core subjects?",("Not so good","Avearage","Good","Excellent"))
            ques_2 = st.selectbox("How to do that",("Not so good","Avearage","Good","Excellent"))
        with emp3:
            st.empty()
