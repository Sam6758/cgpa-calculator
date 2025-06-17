import tkinter as tk
from tkinter import ttk, messagebox

class CGPAConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA ↔ GPA Converter")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f8ff")
        
        # Set application icon
        try:
            self.root.iconbitmap("cgpa_icon.ico")
        except:
            pass
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('Header.TLabel', 
                            background='#f0f8ff', 
                            foreground='#6c3483', 
                            font=('Segoe UI', 24, 'bold'))
        self.style.configure('Tab.TButton', 
                            font=('Segoe UI', 12, 'bold'), 
                            padding=10,
                            background='#8e44ad',
                            foreground='white')
        self.style.map('Tab.TButton', 
                      background=[('active', '#6c3483'), ('pressed', '#5b2c70')])
        
        # Create header
        header_frame = ttk.Frame(root)
        header_frame.pack(pady=20, fill='x')
        
        header_label = ttk.Label(
            header_frame,
            text="CGPA ↔ GPA Converter",
            style='Header.TLabel'
        )
        header_label.pack()
        
        subheader_label = ttk.Label(
            header_frame,
            text="Convert between 10-point CGPA and 4-point GPA systems",
            background='#f0f8ff',
            font=('Segoe UI', 12),
            foreground='#555'
        )
        subheader_label.pack(pady=10)
        
        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        self.cgpa_to_gpa_frame = ttk.Frame(self.tab_control)
        self.gpa_to_cgpa_frame = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.cgpa_to_gpa_frame, text='CGPA to GPA')
        self.tab_control.add(self.gpa_to_cgpa_frame, text='GPA to CGPA')
        
        self.tab_control.pack(expand=1, fill='both', padx=20, pady=10)
        
        # Build the CGPA to GPA tab
        self.build_cgpa_to_gpa_tab()
        
        # Build the GPA to CGPA tab
        self.build_gpa_to_cgpa_tab()
        
        # Build the reference table
        self.build_reference_table()
    
    def build_cgpa_to_gpa_tab(self):
        # Input section
        input_frame = ttk.LabelFrame(
            self.cgpa_to_gpa_frame,
            text="Enter CGPA (10-point scale)",
            padding=20
        )
        input_frame.pack(fill='x', padx=20, pady=20)
        
        cgpa_label = ttk.Label(
            input_frame,
            text="CGPA:",
            font=('Segoe UI', 12),
            background='#f0f8ff'
        )
        cgpa_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.cgpa_entry = ttk.Entry(
            input_frame,
            font=('Segoe UI', 14),
            width=10,
            justify='center'
        )
        self.cgpa_entry.grid(row=0, column=1, padx=10, pady=10)
        self.cgpa_entry.insert(0, "8.5")
        
        scale_label = ttk.Label(
            input_frame,
            text="Scale: 0.0 to 10.0",
            font=('Segoe UI', 10),
            background='#f0f8ff',
            foreground='#777'
        )
        scale_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Convert button
        convert_btn = ttk.Button(
            input_frame,
            text="Convert to GPA",
            style='Tab.TButton',
            command=self.convert_cgpa_to_gpa
        )
        convert_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Output section
        output_frame = ttk.LabelFrame(
            self.cgpa_to_gpa_frame,
            text="Converted GPA (4-point scale)",
            padding=20
        )
        output_frame.pack(fill='x', padx=20, pady=20)
        
        self.gpa_result = ttk.Label(
            output_frame,
            text="3.40",
            font=('Segoe UI', 36, 'bold'),
            foreground='#2ecc71',
            background='#f0f8ff'
        )
        self.gpa_result.pack(pady=10)
        
        self.grade_equivalent = ttk.Label(
            output_frame,
            text="Equivalent to: A-",
            font=('Segoe UI', 14),
            background='#f0f8ff'
        )
        self.grade_equivalent.pack(pady=5)
        
        scale_label = ttk.Label(
            output_frame,
            text="Scale: 0.0 to 4.0",
            font=('Segoe UI', 10),
            background='#f0f8ff',
            foreground='#777'
        )
        scale_label.pack(pady=5)
    
    def build_gpa_to_cgpa_tab(self):
        # Input section
        input_frame = ttk.LabelFrame(
            self.gpa_to_cgpa_frame,
            text="Enter GPA (4-point scale)",
            padding=20
        )
        input_frame.pack(fill='x', padx=20, pady=20)
        
        gpa_label = ttk.Label(
            input_frame,
            text="GPA:",
            font=('Segoe UI', 12),
            background='#f0f8ff'
        )
        gpa_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.gpa_entry = ttk.Entry(
            input_frame,
            font=('Segoe UI', 14),
            width=10,
            justify='center'
        )
        self.gpa_entry.grid(row=0, column=1, padx=10, pady=10)
        self.gpa_entry.insert(0, "3.4")
        
        scale_label = ttk.Label(
            input_frame,
            text="Scale: 0.0 to 4.0",
            font=('Segoe UI', 10),
            background='#f0f8ff',
            foreground='#777'
        )
        scale_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Convert button
        convert_btn = ttk.Button(
            input_frame,
            text="Convert to CGPA",
            style='Tab.TButton',
            command=self.convert_gpa_to_cgpa
        )
        convert_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Output section
        output_frame = ttk.LabelFrame(
            self.gpa_to_cgpa_frame,
            text="Converted CGPA (10-point scale)",
            padding=20
        )
        output_frame.pack(fill='x', padx=20, pady=20)
        
        self.cgpa_result = ttk.Label(
            output_frame,
            text="8.50",
            font=('Segoe UI', 36, 'bold'),
            foreground='#2ecc71',
            background='#f0f8ff'
        )
        self.cgpa_result.pack(pady=10)
        
        self.cgpa_grade_equivalent = ttk.Label(
            output_frame,
            text="Equivalent to: B+",
            font=('Segoe UI', 14),
            background='#f0f8ff'
        )
        self.cgpa_grade_equivalent.pack(pady=5)
        
        scale_label = ttk.Label(
            output_frame,
            text="Scale: 0.0 to 10.0",
            font=('Segoe UI', 10),
            background='#f0f8ff',
            foreground='#777'
        )
        scale_label.pack(pady=5)
    
    def build_reference_table(self):
        table_frame = ttk.LabelFrame(
            self.root,
            text="Conversion Reference Table",
            padding=20
        )
        table_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create table
        columns = ("cgpa", "gpa", "grade", "percentage")
        table = ttk.Treeview(
            table_frame, 
            columns=columns, 
            show="headings",
            height=12
        )
        
        # Define headings
        table.heading("cgpa", text="10-Point CGPA")
        table.heading("gpa", text="4-Point GPA")
        table.heading("grade", text="Letter Grade")
        table.heading("percentage", text="Percentage Range")
        
        # Set column widths
        table.column("cgpa", width=150, anchor='center')
        table.column("gpa", width=150, anchor='center')
        table.column("grade", width=150, anchor='center')
        table.column("percentage", width=250, anchor='center')
        
        # Add data
        data = [
            ("10.0", "4.0", "A+", "95-100%"),
            ("9.5", "3.8", "A", "90-94%"),
            ("9.0", "3.6", "A-", "85-89%"),
            ("8.5", "3.4", "B+", "80-84%"),
            ("8.0", "3.2", "B", "75-79%"),
            ("7.5", "3.0", "B-", "70-74%"),
            ("7.0", "2.8", "C+", "65-69%"),
            ("6.5", "2.6", "C", "60-64%"),
            ("6.0", "2.4", "C-", "55-59%"),
            ("5.5", "2.2", "D+", "50-54%"),
            ("5.0", "2.0", "D", "45-49%"),
            ("<5.0", "<2.0", "F", "Below 45%")
        ]
        
        for row in data:
            table.insert("", "end", values=row)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def convert_cgpa_to_gpa(self):
        try:
            cgpa = float(self.cgpa_entry.get())
            
            if cgpa < 0 or cgpa > 10:
                messagebox.showerror("Invalid Input", "CGPA must be between 0.0 and 10.0")
                return
            
            # Convert CGPA to GPA
            gpa = round(cgpa * 0.4, 2)
            self.gpa_result.config(text=f"{gpa:.2f}")
            
            # Determine grade equivalent
            grade = self.get_grade_equivalent(gpa)
            self.grade_equivalent.config(text=f"Equivalent to: {grade}")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid CGPA value")
    
    def convert_gpa_to_cgpa(self):
        try:
            gpa = float(self.gpa_entry.get())
            
            if gpa < 0 or gpa > 4:
                messagebox.showerror("Invalid Input", "GPA must be between 0.0 and 4.0")
                return
            
            # Convert GPA to CGPA
            cgpa = round(gpa * 2.5, 2)
            self.cgpa_result.config(text=f"{cgpa:.2f}")
            
            # Determine grade equivalent
            grade = self.get_cgpa_grade_equivalent(cgpa)
            self.cgpa_grade_equivalent.config(text=f"Equivalent to: {grade}")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid GPA value")
    
    def get_grade_equivalent(self, gpa):
        if gpa >= 3.85:
            return "A+"
        elif gpa >= 3.65:
            return "A"
        elif gpa >= 3.40:
            return "A-"
        elif gpa >= 3.15:
            return "B+"
        elif gpa >= 2.90:
            return "B"
        elif gpa >= 2.60:
            return "B-"
        elif gpa >= 2.30:
            return "C+"
        elif gpa >= 2.00:
            return "C"
        elif gpa >= 1.70:
            return "C-"
        elif gpa >= 1.30:
            return "D+"
        elif gpa >= 1.00:
            return "D"
        else:
            return "F"
    
    def get_cgpa_grade_equivalent(self, cgpa):
        if cgpa >= 9.5:
            return "A+"
        elif cgpa >= 9.0:
            return "A"
        elif cgpa >= 8.5:
            return "A-"
        elif cgpa >= 8.0:
            return "B+"
        elif cgpa >= 7.5:
            return "B"
        elif cgpa >= 7.0:
            return "B-"
        elif cgpa >= 6.5:
            return "C+"
        elif cgpa >= 6.0:
            return "C"
        elif cgpa >= 5.5:
            return "C-"
        elif cgpa >= 5.0:
            return "D+"
        elif cgpa >= 4.5:
            return "D"
        else:
            return "F"

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPAConverterApp(root)
    root.mainloop()
