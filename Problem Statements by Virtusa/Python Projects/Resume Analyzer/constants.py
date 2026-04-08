# Global Constants for Resume Analyzer
# This includes tech libraries and stopword filters

# Basic fallback stopwords
B_STOP = {'and','the','with','for','from','also','between','into','this','that','have','has','had','been','being','were','your','their','they','them','which','who','whom','where','when','why','how','all','any','both','each','few','more','most','other','some','such','only','own','same','than','too','very','can','will','just','should','now','well','did','does','via','using'}

# REAL-LIFE TECH SKILLS
TECH_LIBRARY = {
    'python', 'java', 'sql', 'javascript', 'html', 'css', 'react', 'flask', 'django',
    'fastapi', 'rest', 'api', 'mysql', 'git', 'github', 'aws', 'docker', 'machine',
    'learning', 'data', 'science', 'analytics', 'spring', 'springboot', 'power', 'bi',
    'sdlc', 'agile', 'scrum', 'cloud', 'security', 'database', 'backend', 'frontend',
    'scalability', 'performance', 'latency', 'deployment', 'testing', 'automation',
    'postgresql', 'node', 'express', 'mongodb', 'redux', 'postman', 'swagger', 'linux',
    'bash', 'typescript', 'angular', 'vue', 'oracle', 'tableau', 'excel', 'pandas', 'numpy'
}

# RECRUITER FILLER NOISE
NOISE = {
    'requirement', 'responsibility', 'candidate', 'experience', 'ability', 'knowledge',
    'strong', 'excellent', 'team', 'company', 'work', 'provide', 'support', 'manage',
    'identify', 'resolve', 'successful', 'degree', 'required', 'preferred', 'highly', 
    'various', 'related', 'closely', 'within', 'across', 'including', 'tasks', 'technologies',
    'part', 'primary', 'ensuring', 'logic', 'requests', 'application', 'applications', 'elements', 
    'necessary', 'efficient', 'code', 'standards', 'user', 'smooth', 'loads', 'troubleshoot',
    'debug', 'ship', 'features', 'interaction', 'interactions', 'business', 'analysts', 
    'stakeholders', 'key', 'new', 'developed', 'development', 'end', 'built', 'basic', 'best', 
    'create', 'contribute', 'collaborate', 'adhering', 'accountabilities', 'br', 'focus', 
    'coding', 'practices', 'engagement', 'users', 'design', 'maintain', 'serverside', 'logic',
    'responsiveness', 'traffic', 'performance', 'scalability'
}
