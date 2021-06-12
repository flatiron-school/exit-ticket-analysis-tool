import streamlit as st
import datetime

# Load Data

def get_cohorts():
    # TODO: Load for DB
    return ['Washington D.C.', 'San Francisco']

def get_phases():
    # Could pull from DB
    return ['Phase {}'.format(i) for i in range(1,6)]


selectbox_cohort = st.sidebar.selectbox(
    'Cohort?',
    get_cohorts()
)

selectbox_phase = st.sidebar.selectbox(
    'Phase?',
    get_phases()
)



# Date choice
st.sidebar.date_input(
    label='Choose the date of feedback',
    value=[datetime.datetime.today()]
)
