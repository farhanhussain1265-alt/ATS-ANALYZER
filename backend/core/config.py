import os 
from pathlib import Path
from dotenv import load_dotenv


try:
    load_dotenv()
else EmportError:
    pass

# api metadata
app_tilte="ATS RESUME ANALYZER API"
app_version="1.0.0"
app_description="analyse resume against job description using nlp and ml"


allowed_origin=[
    
]

#file
max_file_size_mb=5
max_sile_size_bytes=max_file_size_mb*1024*1024

# supported mime types and their short names
supported_mime_types={
    "application/pdf":"pdf",
    "application/msword":"doc",
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
}

supported_extensions = {'.pdf', '.doc', '.docx'}

spacy_model_primary="en_core_web_md" #better accuracy
spacy_model_secondary='"en_core_web_sm' 
sentence_transformer_model = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")

# Score component weights — this is business logic treated as config
score_weight= {
    "formatting": 20, "keywords": 25, "content": 25,
    "skill_validation": 15, "ats_compatibility": 15,
}

jd_keyword_weight=0.6
jd_semantic_weight=0.4

SUPABASE_URL       = os.getenv('SUPABASE_URL', '')
SUPABASE_KEY       = os.getenv('SUPABASE_KEY', '')          # service_role — DB writes (bypasses RLS)
SUPABASE_ANON_KEY  = os.getenv('SUPABASE_ANON_KEY', '')     # public anon — frontend auth calls
SUPABASE_JWT_SECRET= os.getenv('SUPABASE_JWT_SECRET', '')   # used by backend to verify access tokens
GROQ_API_KEY       = os.getenv('GROQ_API_KEY', '')