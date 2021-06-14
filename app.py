import streamlit as st
import datetime

import matplotlib.pyplot as plt

import data_loader


# Load Data
df = data_loader.load_csvs()


# Use the data to allow for filtering in sidebar
selectbox_cohort = st.sidebar.selectbox(
    'Cohort?',
    data_loader.get_cohorts()
)

selectbox_phase = st.sidebar.selectbox(
    'Phase?',
    data_loader.get_phases()
)

selectbox_student = st.sidebar.selectbox(
    'Student?',
    data_loader.get_student_names(df)
)

# Choose the date range for feedback
date_range = st.sidebar.date_input(
    label='Choose the date of feedback',
    value=[datetime.datetime.today(),datetime.datetime.today()],
    max_value=datetime.datetime.today()
)



# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Display Data
st.write('Full Data')
st.dataframe(df)

# Get a subset (based on filtering)
def display_student_data(student_name, sort_by=['name','submitted'],
    cols=['name','section','phase','cohort','lecture','submitted','n correct','n incorrect']):
    st.write('Filtered Data for  {}'.format(student_name))

    # Filter by student and sort by date
    df_subset = df[df['name']==student_name].sort_values(by=sort_by)

    df_to_display  = df_subset[cols]
    st.dataframe(df_to_display)

    # Display Visuals
    f, (ax_feedback, ax_percent) = plt.subplots(ncols=2)
    # Line Plot - Percent Correct
    # Note: May need to adjust since feedback is also "graded"
    total_percent = df_subset['n correct'] / (df_subset['n correct'] + df_subset['n incorrect'])
    ax_percent.plot(df_subset['lecture'], total_percent)
    ax_percent.set_ylabel('Percent Correct')
    ax_percent.set_ylim(0,1)
    plt.gcf().autofmt_xdate()
    # Bar Chart - Feedback
    df_subset['This lecture was..._other'].value_counts().plot(kind='bar', rot=40, ax=ax_feedback)
    # ax_feedback =  df_subset.hist('This lecture was...', ax=ax_feedback)
    f.tight_layout()
    st.pyplot(f)

display_student_data(selectbox_student)