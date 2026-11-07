import os 
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# api metadata
APP_TITLE="ATS RESUME ANALYZER"
APP_VERSION="1.0.0"
APP_DESCRIPTION="analyze resume agaianst job description using nlp ans ml"

ALLOWED_ORIGINS=[
    "http://localhost:5137", # Vite dev server (React)
    "http://localhost:3000", # Create react app fallback
    "http://localhost:5137"
]

# File
MAX_FILE_SIZE_MB=5
MAX_FILE_SIZE_BYTES=MAX_FILE_SIZE_MB*1024*1024

# supported name type and their short names

SUPPORTED_MIME_TYPES={
    "application/pdf":"pdf",
    'application/msword': 'doc',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx' 
}

SUPPORTED_EXTENSIONS = {'.pdf', '.doc', '.docx'}

SPACY_MODEL_PRIMARY="en_core_web_sm" #better accuracy
SPACY_MODEL_SECONDARY="en_core_web_md" 
SENTENCE_TRANSFORMER_MODEL = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")

# Score component weights — this is business logic treated as config
SCORE_WEIGHTS = {
    "formatting": 20, "keywords": 25, "content": 25,
    "skill_validation": 15, "ats_compatibility": 15,
}

JD_KEYWORD_WEIGHT=0.6
JD_SEMANTIC_WEIGHT=0.4

SUPABASE_URL       = os.getenv('SUPABASE_URL', '')
SUPABASE_KEY       = os.getenv('SUPABASE_KEY', '')          # service_role — DB writes (bypasses RLS)
SUPABASE_ANON_KEY  = os.getenv('SUPABASE_ANON_KEY', '')     # public anon — frontend auth calls
SUPABASE_JWT_SECRET= os.getenv('SUPABASE_JWT_SECRET', '')   # used by backend to verify access tokens
OPENAI_API_KEY       = os.getenv('OPENAI_API_KEY', '')


