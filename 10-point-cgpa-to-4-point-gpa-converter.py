import streamlit as st
import pandas as pd

# Title and icon
st.set_page_config(page_title="CGPA ↔ GPA Converter", page_icon="🔄", layout="centered")

# Constants and mappings
GRADE_EQUIVALENTS = [
    (3.85, 4.00, 'A+'),
    (3.65, 3.84, 'A'),
    (3.40, 3.64, 'A-'),
    (3.15, 3.39, 'B+'),
    (2.90, 3.14, 'B'),
    (2.60, 2.89, 'B-'),
    (2.30, 2.59, 'C+'),
    (2.00, 2.29, 'C'),
    (1.70, 1.99, 'C-'),
    (1.30, 1.69, 'D+'),
    (1.00, 1.29, 'D'),
    (0.00, 0.99, 'F')
]

REF_TABLE = pd.DataFrame([
    {'CGPA (10)': 10.0, 'GPA (4)': 4.0, 'Grade': 'A+', 'Percent': '95-100%'},
    {'CGPA (10)': 9.5, 'GPA (4)': 3.8, 'Grade': 'A',  'Percent': '90-94%'},
    {'CGPA (10)': 9.0, 'GPA (4)': 3.6, 'Grade': 'A-', 'Percent': '85-89%'},
    {'CGPA (10)': 8.5, 'GPA (4)': 3.4, 'Grade': 'B+', 'Percent': '80-84%'},
    {'CGPA (10)': 8.0, 'GPA (4)': 3.2, 'Grade': 'B',  'Percent': '75-79%'},
    {'CGPA (10)': 7.5, 'GPA (4)': 3.0, 'Grade': 'B-', 'Percent': '70-74%'},
    {'CGPA (10)': 7.0, 'GPA (4)': 2.8, 'Grade': 'C+', 'Percent': '65-69%'},
    {'CGPA (10)': 6.5, 'GPA (4)': 2.6, 'Grade': 'C',  'Percent': '60-64%'},
    {'CGPA (10)': 6.0, 'GPA (4)': 2.4, 'Grade': 'C-', 'Percent': '55-59%'},
    {'CGPA (10)': 5.5, 'GPA (4)': 2.2, 'Grade': 'D+', 'Percent': '50-54%'},
    {'CGPA (10)': 5.0, 'GPA (4)': 2.0, 'Grade': 'D',  'Percent': '45-49%'},
    {'CGPA (10)': '<5.0', 'GPA (4)': '<2.0','Grade': 'F',  'Percent': 'Below 45%'}
])

# Sidebar: selection
st.sidebar.title("Conversion Type")
mode = st.sidebar.radio("Choose conversion:", ["CGPA → GPA", "GPA → CGPA"])

# Input and calculation
if mode == "CGPA → GPA":
    st.header("10-Point CGPA to 4-Point GPA")
    cgpa = st.number_input("Enter your CGPA (0.00–10.00):", min_value=0.0, max_value=10.0, value=8.5, step=0.01, format="%.2f")
    gpa = round((cgpa / 10) * 4, 2)
    st.metric(label="Converted GPA", value=f"{gpa:.2f}")
    # letter grade
    grade = next((g for low, high, g in GRADE_EQUIVALENTS if gpa >= low and gpa <= high), 'F')
    st.write(f"**Equivalent to:** {grade}")

else:
    st.header("4-Point GPA to 10-Point CGPA")
    gpa = st.number_input("Enter your GPA (0.00–4.00):", min_value=0.0, max_value=4.0, value=3.4, step=0.01, format="%.2f")
    cgpa = round((gpa * 10) / 4, 2)
    st.metric(label="Converted CGPA", value=f"{cgpa:.2f}")
    # letter grade based on CGPA
    # reuse table lookup
    grade = REF_TABLE[REF_TABLE['CGPA (10)'] != '<5.0']
    grade = grade[(grade['CGPA (10)']<=cgpa)]['Grade'].max() if cgpa>=5.0 else 'F'
    st.write(f"**Equivalent to:** {grade}")

# Display reference table
st.subheader("Conversion Reference Table")
st.dataframe(REF_TABLE.reset_index(drop=True))

# Footer note
st.markdown("---")
st.info("Different universities may use different conversion methods. Check with your institution for their preferred formula.")
