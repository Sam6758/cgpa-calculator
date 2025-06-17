import streamlit as st

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="KTU GPA Calculator", layout="wide")

st.title("📊 KTU GPA Calculator | Enhanced in Python")

tabs = st.tabs(["GPA Calculator", "CGPA Calculator", "History"])

with tabs[0]:
    st.header("GPA Calculator")
    num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=20, value=1, step=1)
    
    total_credits, total_points = 0, 0
    
    for i in range(1, num_subjects + 1):
        st.subheader(f"Subject {i}")
        name = st.text_input(f"Subject Name #{i}", key=f"name_{i}")
        credits = st.number_input(f"Credits for {name or 'Subject'}", min_value=1, max_value=10, value=4, key=f"cred_{i}")
        grade = st.selectbox(
            f"Grade for {name or 'Subject'}",
            options=["A+", "A", "B+", "B", "C+", "C", "D", "F"],
            index=0, key=f"grade_{i}"
        )
        grade_point_map = {"A+": 10, "A": 9, "B+": 8, "B": 7, "C+": 6, "C": 5, "D": 4, "F": 0}
        gp = grade_point_map[grade]
        
        total_credits += credits
        total_points += credits * gp
    
    sgpa = (total_points / total_credits) if total_credits > 0 else 0.0
    st.markdown(f"### Semester GPA (SGPA): **{sgpa:.2f}**")
    
    if st.button("Save Result"):
        st.session_state.history.append({
            "type": "SGPA",
            "value": f"{sgpa:.2f}",
            "details": f"{num_subjects} subjects | {total_credits} credits"
        })
        st.success("Result saved to history!")

with tabs[1]:
    st.header("CGPA Calculator")
    num_semesters = st.number_input("Number of Semesters", min_value=1, max_value=20, value=1, step=1)
    
    total_sem_credits, total_sem_points = 0, 0
    for j in range(1, num_semesters + 1):
        st.subheader(f"Semester {j}")
        sem_credits = st.number_input(f"Credits for Semester {j}", min_value=1, max_value=50, value=22, key=f"sem_cred_{j}")
        sem_sgpa = st.number_input(f"SGPA for Semester {j}", min_value=0.0, max_value=10.0, value=8.5, step=0.01, key=f"sem_sgpa_{j}")
        
        total_sem_credits += sem_credits
        total_sem_points += sem_credits * sem_sgpa
    
    cgpa = (total_sem_points / total_sem_credits) if total_sem_credits > 0 else 0.0
    st.markdown(f"### Cumulative GPA (CGPA): **{cgpa:.2f}**")
    
    if st.button("Save CGPA"):
        st.session_state.history.append({
            "type": "CGPA",
            "value": f"{cgpa:.2f}",
            "details": f"{num_semesters} semesters | {total_sem_credits} credits"
        })
        st.success("CGPA saved to history!")

with tabs[2]:
    st.header("History")
    if st.session_state.history:
        for idx, record in enumerate(st.session_state.history, start=1):
            st.write(f"**{idx}. {record['type']}**: {record['value']} | {record['details']}")
            # Remove button mutates state and Streamlit will auto‑rerun
            if st.button(f"Delete {record['type']} #{idx}", key=f"del_{idx}"):
                st.session_state.history.pop(idx-1)
    else:
        st.info("No history yet. Save a result to see it here.")
