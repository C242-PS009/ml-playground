import nltk

nltk.download("wordnet")
wnl = nltk.WordNetLemmatizer()

def lemmatize(sentence: str) -> str:
    sentence = sentence.lower().strip()
    words = [wnl.lemmatize(word) for word in sentence.split()]
    return " ".join(words)