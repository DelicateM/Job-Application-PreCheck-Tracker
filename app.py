import streamlit as st
from state import TaskState
from agent import agent_decide

st.set_page_config(
    page_title="Internship Application Pre-Check Assistant",
    layout="centered"
)

st.title("Internship Application Pre-Check Assistant")

#State
if "task_state" not in st.session_state:
    st.session_state.task_state = TaskState.COLLECT_PROFILE
if "data" not in st.session_state:
    st.session_state.data = {}

current_state = st.session_state.task_state.value
current_step_index = list(TaskState).index(st.session_state.task_state)
total_steps = len(TaskState) - 1
progress_value = current_step_index / total_steps
st.progress(progress_value)

#Collect profile
if current_state == "collect_profile":
    st.subheader("Step 1: Applicant Profile")
    st.session_state.data["name"] = st.text_input("Full Name")
    st.session_state.data["degree"] = st.text_input("Degree or Qualification")
    st.session_state.data["year"] = st.selectbox("Year of Study", ["", "1", "2", "3", "4"])
    st.session_state.data["role"] = st.selectbox(
        "Target Internship Role", ["", "Software Engineering", "Business Analyst"]
    )
    message, confidence, can_continue = agent_decide(current_state, st.session_state.data)
    st.info(message)
    st.write("Agent Confidence:", confidence)

    if st.button("Continue", disabled=not can_continue):
        st.session_state.task_state = TaskState.COLLECT_DOCUMENTS
        st.rerun()

#Collect documents
elif current_state == "collect_documents":
    st.subheader("Step 2: Required Documents")
    st.session_state.data["cv_uploaded"] = st.checkbox("CV uploaded")
    st.session_state.data["portfolio"] = st.text_input(
        "Portfolio Link (required for Software Engineering roles)"
    )
    message, confidence, can_continue = agent_decide(current_state, st.session_state.data)
    st.info(message)
    st.write("Agent Confidence:", confidence)

    back_col, continue_col = st.columns(2)
    with back_col:
        if st.button("Back"):
            st.session_state.task_state = TaskState.COLLECT_PROFILE
            st.rerun()
    with continue_col:
        if st.button("Continue", disabled=not can_continue):
            st.session_state.task_state = TaskState.VALIDATE
            st.rerun()

#Validation
elif current_state == "validate":
    st.subheader("Step 3: Application Validation")
    message, confidence, can_continue = agent_decide(current_state, st.session_state.data)
    
    if can_continue:
        st.success(message)
    else:
        st.warning(message)
    
    st.write("Agent Confidence:", confidence)
    
    back_col, continue_col = st.columns(2)
    with back_col:
        if st.button("Fix Issues"):
            st.session_state.task_state = TaskState.COLLECT_DOCUMENTS
            st.rerun()
    with continue_col:
        if st.button("Proceed to Review", disabled=not can_continue):
            st.session_state.task_state = TaskState.REVIEW
            st.rerun()

#Review
elif current_state == "review":
    st.subheader("Step 4: Review Summary")
    st.json(st.session_state.data)
    if st.button("Submit for final check"):
        st.session_state.task_state = TaskState.COMPLETE
        st.rerun()

elif current_state == "complete":
    st.subheader("Final Status")
    st.success("Your application is ready for submission.")
