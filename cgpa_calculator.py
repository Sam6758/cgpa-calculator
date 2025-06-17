import streamlit as st
from streamlit.components.v1 import html
import base64

def main():
    # Set page configuration
    st.set_page_config(
        page_title="CGPA Calculator",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Inject custom CSS
    st.markdown("""
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2c3e50;
            --accent: #e74c3c;
            --light: #f8f9fa;
            --dark: #212529;
            --success: #2ecc71;
            --card-bg: rgba(255, 255, 255, 0.95);
        }

        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: var(--dark);
            line-height: 1.6;
        }

        .container {
            width: 90%;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        .hero {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9));
            background-size: cover;
            background-position: center;
            border-radius: 15px;
            margin: 20px 0 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .calculator-card {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            margin: 30px auto;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s ease;
        }

        .calculator-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 8px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
        }

        .input-group {
            margin-bottom: 20px;
        }

        .input-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #555;
            font-size: 1.1rem;
        }

        .input-group input, .input-group select {
            width: 100%;
            padding: 14px 18px;
            border: 2px solid #e1e5eb;
            border-radius: 12px;
            font-size: 1rem;
            transition: all 0.3s;
            background: #f8f9fa;
        }

        .btn {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 30px;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            margin: 10px 5px;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
        }

        .btn:hover {
            background: #2980b9;
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(52, 152, 219, 0.4);
        }

        .btn-accent {
            background: var(--accent);
            box-shadow: 0 4px 12px rgba(231, 76, 60, 0.3);
        }

        .btn-accent:hover {
            background: #c0392b;
            box-shadow: 0 6px 18px rgba(231, 76, 60, 0.4);
        }

        .btn-success {
            background: var(--success);
            box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3);
        }

        .btn-success:hover {
            background: #27ae60;
            box-shadow: 0 6px 18px rgba(46, 204, 113, 0.4);
        }

        .button-group {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 25px 0;
        }

        .courses-section {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
        }

        .course-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }

        .course-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }

        .add-course-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            background: rgba(52, 152, 219, 0.1);
            border: 2px dashed var(--primary);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            color: var(--primary);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .result-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 40px;
        }

        .result-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            position: relative;
            overflow: hidden;
            border-top: 5px solid var(--primary);
        }

        .result-card.semester {
            border-top-color: var(--success);
        }

        .result-card.cumulative {
            border-top-color: var(--accent);
        }

        .result-value {
            font-size: 3.5rem;
            font-weight: 800;
            color: var(--primary);
            margin: 10px 0;
            text-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
        }

        .result-card.semester .result-value {
            color: var(--success);
        }

        .result-card.cumulative .result-value {
            color: var(--accent);
        }

        .main-site-link {
            text-align: center;
            margin: 50px auto;
            padding: 30px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            color: white;
            max-width: 700px;
        }
        
        @media (max-width: 768px) {
            .button-group {
                flex-direction: column;
                gap: 10px;
            }
            
            .input-section, .result-section {
                grid-template-columns: 1fr;
            }
            
            .course-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # App content
    st.markdown("""
    <div class="container">
        <div class="hero">
            <h2>CGPA Calculator</h2>
            <p>Calculate your Cumulative Grade Point Average instantly with our easy-to-use tool</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculator section
    with st.container():
        st.markdown("""
        <div class="container">
            <div class="calculator-card">
                <h2 style="text-align: center; margin-bottom: 30px; color: #2c3e50; font-size: 2.2rem; position: relative; padding-bottom: 15px;">
                    <i class="fas fa-graduation-cap"></i> CGPA Calculator
                </h2>
        """, unsafe_allow_html=True)
        
        # Input section
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            prev_credits = st.number_input(
                "Previous Total Credits", 
                min_value=0, 
                value=0,
                key="prev_credits",
                help="Enter your previous total credits"
            )
        
        with col2:
            prev_cgpa = st.number_input(
                "Previous CGPA", 
                min_value=0.0, 
                max_value=10.0, 
                value=0.0, 
                step=0.01,
                key="prev_cgpa",
                help="Enter your previous CGPA"
            )
        
        with col3:
            num_courses = st.number_input(
                "Number of Courses", 
                min_value=1, 
                max_value=15, 
                value=5,
                key="num_courses",
                help="Enter the number of current semester courses"
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Courses section
    st.markdown(f"""
    <div class="container">
        <div class="courses-section">
            <div class="courses-header">
                <h3 style="color: #2c3e50; font-size: 1.5rem;">
                    <i class="fas fa-book-open"></i> Current Semester Courses
                </h3>
                <span id="courseCount">{num_courses} courses</span>
            </div>
            
            <div class="course-grid" id="coursesContainer">
    """, unsafe_allow_html=True)
    
    # Generate course inputs
    grade_options = [
        ('O (Outstanding) - 10.0', 10),
        ('A+ (Excellent) - 9.0–9.99', 9.5),
        ('A (Very Good) - 8.0–8.99', 8.5),
        ('B+ (Good) - 7.0–7.99', 7.5),
        ('B (Above Average) - 6.0–6.99', 6.5),
        ('C (Average) - 5.0–5.99', 5.5),
        ('P (Pass) - 4.0–4.99', 4.5),
        ('F (Fail) - 0.0', 0)
    ]
    
    credit_options = [1, 2, 3, 4, 5, 6]
    
    courses = []
    for i in range(num_courses):
        with st.container():
            st.markdown(f"""
            <div class="course-card">
                <h4 style="margin-bottom: 15px; color: #2c3e50;">
                    <i class="fas fa-book"></i> Course {i+1}
                </h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                grade = st.selectbox(
                    f"Grade for Course {i+1}", 
                    [option[0] for option in grade_options],
                    key=f"grade_{i}"
                )
            with col2:
                credit = st.selectbox(
                    f"Credits for Course {i+1}", 
                    credit_options,
                    key=f"credit_{i}"
                )
            
            # Store course data
            grade_value = next((val for label, val in grade_options if label == grade), 0)
            courses.append({"grade": grade_value, "credit": credit})
    
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        calculate = st.button("📊 Calculate CGPA", use_container_width=True)
    with col2:
        reset = st.button("🔄 Reset All", use_container_width=True)
    
    # Calculate CGPA
    if calculate:
        sem_credits = 0
        sem_points = 0
        
        for course in courses:
            sem_credits += course["credit"]
            sem_points += course["grade"] * course["credit"]
        
        if sem_credits == 0:
            st.error("Please enter at least one course with credits")
        else:
            sem_gpa = sem_points / sem_credits
            
            if prev_credits > 0:
                total_points = prev_cgpa * prev_credits + sem_points
                total_credits = prev_credits + sem_credits
                cumulative_gpa = total_points / total_credits
            else:
                cumulative_gpa = None
            
            # Display results
            st.markdown("""
            <div class="container">
                <div class="result-section">
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="result-card semester">
                    <h3>Semester GPA</h3>
                    <div class="result-value">{sem_gpa:.2f}</div>
                    <div class="result-label">Based on current courses</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if cumulative_gpa is not None:
                    st.markdown(f"""
                    <div class="result-card cumulative">
                        <h3>Cumulative CGPA</h3>
                        <div class="result-value">{cumulative_gpa:.2f}</div>
                        <div class="result-label">Combined with previous performance</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("""
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Reset functionality
    if reset:
        st.session_state.prev_credits = 0
        st.session_state.prev_cgpa = 0.0
        st.session_state.num_courses = 5
        st.experimental_rerun()
    
    # Main site link
    st.markdown("""
    <div class="container">
        <div class="main-site-link">
            <h2><i class="fas fa-external-link-alt"></i> More Academic Tools</h2>
            <p>Visit CGPAcalculator.in for additional GPA calculators, grade converters, and academic planning tools designed for all education levels.</p>
            <a href="https://cgpacalculator.in/" target="_blank" style="display: inline-block; background: white; color: #3498db; padding: 15px 40px; border-radius: 50px; font-size: 1.2rem; font-weight: 700; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);">Explore All Tools</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Inject Font Awesome
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()