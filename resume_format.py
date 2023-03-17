# Define the candidate's name and contact information
name = "John Doe"
email = "johndoe@email.com"
phone = "555-1234"

# Define the candidate's objective
objective = "To obtain a software engineering position at a leading tech company"

# Define the candidate's education
education = [
    {"degree": "Bachelor of Science in Computer Science", "school": "University of XYZ", "grad_year": "2020"},
    {"degree": "High School Diploma", "school": "ABC High School", "grad_year": "2016"}
]

# Define the candidate's skills
skills = ["Python", "Java", "C++", "SQL", "Git", "HTML", "CSS", "JavaScript"]

# Define the candidate's work experience
work_experience = [
    {
        "title": "Software Engineer",
        "company": "ABC Company",
        "start_date": "June 2020",
        "end_date": "Present",
        "description": "Developed and maintained software applications using Python and Java"
    },
    {
        "title": "Software Development Intern",
        "company": "XYZ Corporation",
        "start_date": "May 2019",
        "end_date": "August 2019",
        "description": "Assisted with software development projects using Python and C++"
    }
]

# Print the resume information
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"\nObjective: {objective}\n")

print("Education:")
for degree in education:
    print(f"{degree['degree']} - {degree['school']}, {degree['grad_year']}")
print()

print("Skills:")
print(", ".join(skills))
print()

print("Work Experience:")
for job in work_experience:
    print(f"{job['title']}, {job['company']} ({job['start_date']} - {job['end_date']})")
    print(f"\t{job['description']}\n")
