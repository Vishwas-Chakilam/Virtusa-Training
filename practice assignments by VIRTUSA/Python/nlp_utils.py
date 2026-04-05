import re
import constants # Import our constants file

# Required Libraries: pip install nltk PyPDF2
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        N_STOP = set(stopwords.words('english'))
    except:
        N_STOP = set() 
except ImportError:
    nltk = None
    N_STOP = set()

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

# Combine all filters
MASTER_STOP = N_STOP.union(constants.B_STOP).union(constants.NOISE)

# --- REFINED KEYWORD EXTRACTION ---

def extract_meaningful_tech_skills(raw_text):
    if not raw_text: return set()
    
    # 1. PRE-CLEANING
    text = raw_text.lower()
    text = re.sub(r'br\b|[\r\n]', ' ', text)
    text = re.sub(r'[/\\-]', ' ', text)      
    text = re.sub(r'[^a-z\s]', ' ', text)    
    
    # 2. Tokenization
    tokens = word_tokenize(text) if nltk else text.split()
    
    final_skills = []
    
    # 3. STRICT MATCHING LOGIC
    if nltk:
        try:
            tagged = pos_tag(tokens)
            idx = 0
            while idx < len(tagged):
                word, tag = tagged[idx]
                if word in constants.TECH_LIBRARY:
                    final_skills.append(word)
                elif tag.startswith('NN') and word not in MASTER_STOP:
                    if len(word) >= 4 and word.isalpha():
                        final_skills.append(word)
                idx += 1
        except:
            for w in tokens:
                if w in constants.TECH_LIBRARY or (w not in MASTER_STOP and len(w) >= 4):
                    final_skills.append(w)
    else:
        for w in tokens:
            if w in constants.TECH_LIBRARY or (w not in MASTER_STOP and len(w) >= 5):
                final_skills.append(w)
                
    return set(final_skills)

def get_pdf_text_util(path):
    if not PyPDF2: return "Error: PyPDF2 Missing."
    try:
        with open(path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            return "".join([p.extract_text() or "" for p in pdf.pages])
    except Exception as e:
        return f"Error: {e}"
