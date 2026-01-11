Option 1: UI-based Constrained Agent
Project: Internship Application Pre-Check-Tracker
OVERVIEW
This project is a UI-based task assistant built with python and runs on streamlit. It is designed to help internship applicants through a structured pre-check process before submitting an application to ensure they submitted all the required details and documents.
The system uses a state-driven agent whose behaviour is constrained by the UI rather than free-form chat. The agent provides short feedback based on the current task state and user inputs.

DESIGN OVERVIEW
COMPONENTS
-UI
The UI runs on streamlit and it collects user details through input and controls progression between steps.
-Agent
Listed as "agent.py" on files, it performs validation and decision logic per task state.
-State model
Listed as "state.py" on files, it defines the allowed progression of the task.

STATE FLOW
Collect profile > Collect documents > Validation > Review > Submission
The users cannot skip any steps.

UI vs AGENT vs MEMORY
-UI
Provides input fields for the user
Enables or disables progression depending on the information provided by the user
The agents feedback and confidence is displayed
Handles backtracking in case of a violation in the required steps

-AGENT
Recieves current state and collected data
A confidence indicator based on user input(Low\Medium\High)
A boolean decision(can_continue) progresses to the next step if requirements are met but does not if they are not met

-MEMORY
Stored in st.session_state
It holds the current task state and the application data supplied by the user
It also prevents the loss of progress in between the steps

WHAT WOULD BREAK IF THIS WAS IMPLEMENTED AS PLAIN TEXT CHAT
If this was free-form chat;
-Users would skip the required fields
-Validation would be indirect and unclear
-Recovery from error would be multiple possible outcomes
-Agent outputs would be harder to control

CONSTRAINING THE AGENT VIA UI
The agent cannot hallucinate actions
User actions are predictable
Validation is clear and direct
Failure and recovery is visible and controlled

FAILURE SCENARIO
The user selects software engineering as a role but does not provide a portfolio link.
-How the system responds:
The agent blocks progression at the collect documents step, tells user what is missing and the continue button will remain disabled.
RECOVERY
The user can add the portfolio link, the agent re-evaluates the state and progression becomes available the continue button is enabled without restarting the task.

HOW TO RUN THE APPLICATION LOCALLY
REQUIREMENTS
Python 3.12+
Streamlit (to be installed in the terminal of vs code on the SETUP phase)

SETUP(type in the terminal step by step)
Step 1: python -m venv venv
Step 2: venv\Scripts\activate (windows)
Step 3: pip install streamlit

RUN(type in the terminal)
streamlit run app.py

![System Flow Diagram](diagrams/system%20flow.png)

# STEP 1: COLLECT PROFILE

![Step 1](screenshots/Applicant%20Profile%20Step%201.png)

# STEP 2: COLLECT DOCUMENTS

![Step 2](screenshots/Required%20Documents%20Step%202.png)

# STEP 3: VALIDATION

![Step 3](screenshots/Validation%20Step%203.png)

# STEP 4: REVIEW

![Step 4](screenshots/Review%20Step%204.png)

# STEP 5: FINAL SUBMISSION

![Step 5](screenshots/Final%20Submission%20Step%205.png)

# FAILURE SCENARIO

The system does not allow progression when required fields are missing. When a user selects Software engineering as their role, a portfolio link is required, should user not provide one the agent will disable continue button therefore the user cannot progress to the next step.
![Failure Scenario](screenshots/Failed%20Scenario.png)
