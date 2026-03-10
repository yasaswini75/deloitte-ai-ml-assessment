from skill_extractor import extract_skills
from job_matcher import calculate_match

required_skills = ["python","sql","machine learning","data analysis"]

with open("sample_resume.txt","r") as file:
    resume = file.read()

candidate_skills = extract_skills(resume)

score, matched = calculate_match(candidate_skills, required_skills)

print("Detected Skills:", candidate_skills)
print("Matched Skills:", matched)
print("Job Match Score:", score,"%")
