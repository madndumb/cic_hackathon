#stop words elimination
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Stopwords:
    def __init__(self,input_text):
        self.input_text = input_text

    def eliminator(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.input_text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return filtered_sentence
