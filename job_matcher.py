def calculate_match(candidate_skills, required_skills):

    matched = set(candidate_skills).intersection(set(required_skills))

    score = len(matched) / len(required_skills) * 100

    return score, matched
