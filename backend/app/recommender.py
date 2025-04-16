import json

def generate_recommendations(user):
    skills = json.loads(user.skills)
    interests = json.loads(user.interests)

    recommendations = []

    tech_skills = {'python', 'java', 'javascript', 'c++', 'html', 'css', 'sql'}
    if any(skill.lower() in tech_skills for skill in skills):
        recommendations.append({
            'field': 'Software Development',
            'reason': 'Your technical skills match well with software development roles',
            'jobs': ['Frontend Developer', 'Backend Developer', 'Full Stack Developer'],
            'courses': ['Advanced Algorithms', 'Cloud Computing', 'DevOps']
        })

    design_skills = {'photoshop', 'illustrator', 'ui', 'ux', 'figma'}
    if any(skill.lower() in design_skills for skill in skills):
        recommendations.append({
            'field': 'Design',
            'reason': 'Your design skills indicate potential in creative fields',
            'jobs': ['UI/UX Designer', 'Graphic Designer', 'Product Designer'],
            'courses': ['Design Principles', 'User Research', 'Prototyping']
        })

    business_skills = {'marketing', 'finance', 'management', 'leadership'}
    if any(skill.lower() in business_skills for skill in skills):
        recommendations.append({
            'field': 'Business',
            'reason': 'Your business-oriented skills suggest management potential',
            'jobs': ['Business Analyst', 'Marketing Manager', 'Product Manager'],
            'courses': ['Marketing', 'Business Strategy', 'Financial Modeling']
        })

    if not recommendations:
        recommendations.append({
            'field': 'General',
            'reason': 'Explore various fields to find your passion',
            'jobs': ['Internships', 'Entry-level roles'],
            'courses': ['Career Exploration', 'Personality Assessments']
        })

    return {'recommendations': recommendations}
