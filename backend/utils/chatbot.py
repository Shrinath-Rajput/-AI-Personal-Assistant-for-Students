from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = ["python", "machine learning", "flask", "ai"]
answers = [
    "Python is a programming language",
    "Machine learning is AI subset",
    "Flask is a Python web framework",
    "AI means Artificial Intelligence"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot_response(msg):
    vec = vectorizer.transform([msg])
    sim = cosine_similarity(vec, X)
    return answers[sim.argmax()]