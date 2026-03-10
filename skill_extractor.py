skills_db = ["python","sql","machine learning","pandas","numpy","data analysis"]

def extract_skills(resume_text):

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills
