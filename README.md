Option 1: UI-based Constrained Agent
Project: Internship Application Pre-Check-Tracker
OVERVIEW
This project is a UI-based task assistant designed to help internship applicants through a structured pre-check process before submitting an application to ensure they submitted all the required details and documents.
The system uses a state-driven agent whose behaviour is constrained by the UI rather than free-form chat. The agent provides short feedback based on the current task state and user inputs.
ARCHITECTURE OVERVIEW
COMPONENTS
-UI
The user interface is on hosted on streamlit and it collects user input and controls progression between steps.
-Agent
Listed as "agent.py" on files, it performs validation and decision logic per task state.
-State model
Listed as "state.py" on files, it defines the allowed progression of the task.

STATE FLOW
Collect profile > Collect documents > Validation > Review > Submission
The users cannot skip any steps.

UI vs AGENT vs MEMORY
-UI
Provides input fields
Enables or disables progression depending on the information provided by the user
The agents feedback and confidence is displayed
Handles backtracking

-AGENT
Recieves current state and collected data
A confidence indicator based on user input(Low\Medium\High)
A boolean decision(can_continue)

-MEMORY
Stored in st.session_state
It holds the current task state and the application data supplied by the user
It also prevents the loss of progress in between the steps

WHAT WOULD BREAK IF THIS WAS IMPLEMENTED AS PLAIN TEXT CHAT
If this was free-form chat;
Users would skip the required fields
Validation would be implicit and unclear
Recovery from error would be ambigious
Agent outputs would be harder to control

CONSTRAINING THE AGENT VIA UI
The agent cannot hallucinate actions
User actions are predictable
Validation is explicit
Failure and recovery is visible and controlled

FAILURE SCENARIO
The user selects software engineering as a role but does not provide a portfolio link.
-How the system responds:
The agent blocks progression at the collect documents step, tells user what is missing and the continue button will remain disabled.
RECOVERY
The user can add the portfolio link, the agent re-evaluates the state and progression becomes available the continue button is enabled without restarting the task.
This shows partial task completion and recovery, not a reset.

HOW TO RUN THE APPLICATION LOCALLY
REQUIREMENTS
Python 3.12+
Streamlit

SETUP(terminal)
python -m venv venv
venv\Scripts\activate (windows)
pip install streamlit

RUN(terminal)
streamlit run app.py
