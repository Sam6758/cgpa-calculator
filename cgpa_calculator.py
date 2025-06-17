import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="CGPA Calculator | GPA Tools for All Education Levels",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling
st.markdown("""
<style>
    :root {
        --primary: #3498db;
        --secondary: #2c3e50;
        --accent: #e74c3c;
        --success: #2ecc71;
        --light: #f8f9fa;
        --dark: #212529;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
        background-size: cover !important;
        background-attachment: fixed !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    .header-card {
        background: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)) !important;
        border-radius: 20px !important;
        padding: 40px 30px !important;
        margin: 20px 0 30px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
        text-align: center !important;
        border-left: 6px solid var(--primary) !important;
    }
    
    .calculator-card {
        background: rgba(255, 255, 255, 0.97) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12) !important;
        position: relative !important;
        overflow: hidden !important;
        margin-bottom: 30px !important;
        border-top: 8px solid var(--primary) !important;
    }
    
    .course-card {
        background: white !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05) !important;
        margin-bottom: 15px !important;
        border-left: 4px solid var(--primary) !important;
        transition: all 0.3s ease !important;
    }
    
    .course-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1) !important;
    }
    
    .result-card {
        background: white !important;
        border-radius: 15px !important;
        padding: 25px !important;
        text-align: center !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08) !important;
        position: relative !important;
        overflow: hidden !important;
        border-top: 5px solid var(--primary) !important;
        margin-top: 20px !important;
        transition: all 0.4s ease !important;
    }
    
    .result-card.semester {
        border-top-color: var(--success) !important;
    }
    
    .result-card.cumulative {
        border-top-color: var(--accent) !important;
    }
    
    .result-value {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        margin: 10px 0 !important;
        text-shadow: 0 3px 6px rgba(0, 0, 0, 0.1) !important;
    }
    
    .add-course-btn {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        background: rgba(52, 152, 219, 0.1) !important;
        border: 2px dashed var(--primary) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center !important;
        color: var(--primary) !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        margin-top: 20px !important;
    }
    
    .add-course-btn:hover {
        background: rgba(52, 152, 219, 0.2) !important;
        transform: scale(1.02) !important;
    }
    
    .stButton>button {
        border-radius: 50px !important;
        padding: 14px 30px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
        width: 100% !important;
    }
    
    .stButton>button:first-of-type {
        background: var(--success) !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton>button:first-of-type:hover {
        background: #27ae60 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 18px rgba(46, 204, 113, 0.3) !important;
    }
    
    .stButton>button:last-of-type {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton>button:last-of-type:hover {
        background: #c0392b !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 18px rgba(231, 76, 60, 0.3) !important;
    }
    
    .footer-card {
        text-align: center !important;
        margin: 50px auto 20px !important;
        padding: 30px !important;
        background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
        color: white !important;
    }
    
    .pulse {
        animation: pulse 1.5s 1;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease forwards;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .highlight {
        background: linear-gradient(120deg, rgba(46, 204, 113, 0.1), rgba(52, 152, 219, 0.1)) !important;
        padding: 20px !important;
        border-radius: 15px !important;
        margin: 20px 0 !important;
        border-left: 4px solid var(--primary) !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--secondary) !important;
    }
    
    .stNumberInput, .stSelectbox {
        background: #f8f9fa !important;
        border-radius: 12px !important;
        padding: 8px 15px !important;
        border: 2px solid #e1e5eb !important;
    }
    
    .stNumberInput:focus, .stSelectbox:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 4px rgba(52, 152, 219, 0.2) !important;
    }
    
    .stExpander {
        background: transparent !important;
        border: none !important;
    }
    
    .stExpander .streamlit-expanderHeader {
        background: transparent !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 0 !important;
    }
    
    .course-header {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        margin-bottom: 20px !important;
        padding-bottom: 15px !important;
        border-bottom: 2px solid #e1e5eb !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    if 'courses' not in st.session_state:
        st.session_state.courses = [{"grade": 0.0, "credit": 1} for _ in range(3)]
    if 'prev_credits' not in st.session_state:
        st.session_state.prev_credits = 0
    if 'prev_cgpa' not in st.session_state:
        st.session_state.prev_cgpa = 0.0
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False
    if 'animation_class' not in st.session_state:
        st.session_state.animation_class = ""

# Main function
def main():
    initialize_session_state()
    
    # Header section
    st.markdown("""
    <div class="header-card pulse">
        <h1 style="font-size: 2.8rem; margin-bottom: 15px; color: #2c3e50;">CGPA Calculator</h1>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto 20px; color: #555;">
            Calculate your Cumulative Grade Point Average instantly with our easy-to-use tool
        </p>
        <div style="font-size: 3rem; color: #3498db; margin: 20px 0;">
            <i class="fas fa-calculator"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculator card
    with st.container():
        st.markdown("""
        <div class="calculator-card">
            <h2 style="text-align: center; margin-bottom: 30px; position: relative; padding-bottom: 15px;">
                <i class="fas fa-graduation-cap"></i> Calculate Your CGPA
            </h2>
        """, unsafe_allow_html=True)
        
        # Academic history section
        st.markdown("""
        <div class="highlight">
            <h3><i class="fas fa-history"></i> Academic History</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            prev_credits = st.number_input(
                "**Previous Total Credits**", 
                min_value=0, 
                value=st.session_state.prev_credits,
                key="prev_credits",
                help="Enter your previous total credits"
            )
        with col2:
            prev_cgpa = st.number_input(
                "**Previous CGPA**", 
                min_value=0.0, 
                max_value=10.0, 
                value=st.session_state.prev_cgpa,
                step=0.01,
                key="prev_cgpa",
                help="Enter your previous CGPA"
            )
        
        # Current semester courses
        st.markdown("""
        <div class="highlight">
            <h3><i class="fas fa-book-open"></i> Current Semester Courses</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Display courses
        for i, course in enumerate(st.session_state.courses):
            with st.expander(f"**Course {i+1}**", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    grade = st.selectbox(
                        f"Grade", 
                        [
                            "O (Outstanding) - 10.0",
                            "A+ (Excellent) - 9.5",
                            "A (Very Good) - 8.5",
                            "B+ (Good) - 7.5",
                            "B (Above Average) - 6.5",
                            "C (Average) - 5.5",
                            "P (Pass) - 4.5",
                            "F (Fail) - 0.0"
                        ],
                        key=f"grade_{i}",
                        index=0
                    )
                with col2:
                    credit = st.selectbox(
                        f"Credits", 
                        [1, 2, 3, 4, 5, 6],
                        key=f"credit_{i}",
                        index=0
                    )
                
                # Map grade to value
                grade_value = {
                    "O (Outstanding) - 10.0": 10.0,
                    "A+ (Excellent) - 9.5": 9.5,
                    "A (Very Good) - 8.5": 8.5,
                    "B+ (Good) - 7.5": 7.5,
                    "B (Above Average) - 6.5": 6.5,
                    "C (Average) - 5.5": 5.5,
                    "P (Pass) - 4.5": 4.5,
                    "F (Fail) - 0.0": 0.0
                }[grade]
                
                # Update session state
                st.session_state.courses[i] = {"grade": grade_value, "credit": credit}
        
        # Add course button
        if st.button("➕ Add Another Course", key="add_course", use_container_width=True):
            st.session_state.courses.append({"grade": 0.0, "credit": 1})
            st.experimental_rerun()
        
        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            calculate = st.button("📊 Calculate CGPA", key="calculate", use_container_width=True)
        with col2:
            reset = st.button("🔄 Reset All", key="reset", use_container_width=True)
        
        # Reset functionality
        if reset:
            st.session_state.courses = [{"grade": 0.0, "credit": 1} for _ in range(3)]
            st.session_state.prev_credits = 0
            st.session_state.prev_cgpa = 0.0
            st.session_state.show_results = False
            st.experimental_rerun()
        
        # Calculate CGPA
        if calculate:
            st.session_state.show_results = True
            st.session_state.animation_class = "fade-in"
            
            sem_credits = 0
            sem_points = 0
            
            for course in st.session_state.courses:
                sem_credits += course["credit"]
                sem_points += course["grade"] * course["credit"]
            
            if sem_credits == 0:
                st.error("Please enter at least one course with credits")
                st.session_state.show_results = False
            else:
                sem_gpa = sem_points / sem_credits
                
                if prev_credits > 0:
                    total_points = prev_cgpa * prev_credits + sem_points
                    total_credits = prev_credits + sem_credits
                    cumulative_gpa = total_points / total_credits
                else:
                    cumulative_gpa = None
                
                # Store results in session state
                st.session_state.sem_gpa = sem_gpa
                st.session_state.cumulative_gpa = cumulative_gpa
        
        # Display results
        if st.session_state.show_results:
            st.markdown(f"""
            <div class="result-section {st.session_state.animation_class}">
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="result-card semester">
                    <h3><i class="fas fa-chart-pie"></i> Semester GPA</h3>
                    <div class="result-value" style="color: #2ecc71;">{st.session_state.sem_gpa:.2f}</div>
                    <div class="result-label">Based on current courses</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.session_state.cumulative_gpa is not None:
                    st.markdown(f"""
                    <div class="result-card cumulative">
                        <h3><i class="fas fa-chart-line"></i> Cumulative CGPA</h3>
                        <div class="result-value" style="color: #e74c3c;">{st.session_state.cumulative_gpa:.2f}</div>
                        <div class="result-label">Combined with previous performance</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close calculator card
    
    # Footer with link to main site
    st.markdown("""
    <div class="footer-card">
        <h2 style="margin-bottom: 20px; display: flex; align-items: center; justify-content: center; gap: 15px;">
            <i class="fas fa-external-link-alt"></i> More Academic Tools
        </h2>
        <p style="font-size: 1.2rem; max-width: 600px; margin: 0 auto 30px; line-height: 1.7;">
            Visit CGPAcalculator.in for additional GPA calculators, grade converters, and academic planning tools designed for all education levels.
        </p>
        <a href="https://cgpacalculator.in/" target="_blank" style="display: inline-block; background: white; color: #3498db; padding: 15px 40px; border-radius: 50px; font-size: 1.2rem; font-weight: 700; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);">
            Explore All Tools
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Inject Font Awesome
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
