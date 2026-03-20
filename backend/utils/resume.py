from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_desc = "python machine learning flask api pandas numpy"

def analyze_resume(text):
    docs = [text, job_desc]
    tfidf = TfidfVectorizer()
    mat = tfidf.fit_transform(docs)

    score = cosine_similarity(mat[0:1], mat[1:2])[0][0]
    return round(score * 100, 2)