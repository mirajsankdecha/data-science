import os

def create_subject_folders(base_path, subjects):
    for subject in subjects:
        subject_path = os.path.join(base_path, subject.title())
        os.makedirs(subject_path, exist_ok=True)
        
        # Create subfolders for Unit 1 to Unit 5 and Task
        for i in range(1, 6):
            unit_path = os.path.join(subject_path, f'Unit {i}')
            os.makedirs(unit_path, exist_ok=True)
            
            # Create subfolders inside each Unit
            for sub in ['PDF', 'PPT', 'Other']:
                os.makedirs(os.path.join(unit_path, sub), exist_ok=True)
                
        # Create Task folder
        task_path = os.path.join(subject_path, 'Task')
        os.makedirs(task_path, exist_ok=True)

if __name__ == "__main__":
    # Get the Desktop path dynamically
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    base_directory = os.path.join(desktop_path, "Subjects")
    
    subjects_list = [
        "Big Data Analytics Using Hadoop -II",
        "Big Data Analytics Using Spark",
        "Cloud Computing",
        "Corporate Finance",
        "Data Visualization Techniques Using Power BI",
        "Legal Aspects Of IT Business",
        "Machine Learning Using Python -1",
        "Personal Competence And Capability Building -II",
        "R Programming For Statistics",
        "Research Methodology"
    ]
    
    create_subject_folders(base_directory, subjects_list)
    print("Folders created successfully on Desktop!")
