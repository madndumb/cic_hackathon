import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import numpy as np
import json

word_net_lemmatizer = WordNetLemmatizer()

def text_preprocessing(text):

    final_list = []

    tokens = word_tokenize(text.lower())

    stopwords_and_punctuations_list = stopwords.words("english")+list(string.punctuation)
    for word in tokens:

        if word not in stopwords_and_punctuations_list:

            final_list.append(word_net_lemmatizer.lemmatize(word))

    return final_list


def compute_cosine_similarity(vector_A,vector_B):

    return (np.dot(vector_A,vector_B) /( np.linalg.norm(vector_A) * np.linalg.norm(vector_B)))

text = { 'Rawtext1': "Marijuana is legal in some countries. It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.", 'Rawtext2' :"Marijuana is gaining popularity around the world, and Thailand became the first south east Asian country to legalise it.Beginning with the new year, people will be able to use it as a medicine or study it. However, licenses to produce and sell marijuana products will be strictly controlled. People will be able to carry certain amounts of the drugs if they have a prescription or certificate. The new law also allows kratom, which is a plant native to the region. People use it to treat pain, anxiety and other problems" };

json_str = json.dumps(text)

resp = json.loads(json_str)

a= str(resp['Rawtext1'])
b= str(resp['Rawtext2'])


tokens = sorted(set(text_preprocessing(a)+text_preprocessing(b)))

print(tokens)

bag_of_words_a = []

bag_of_words_b = []

for word in tokens:

    bag_of_words_a.append(text_preprocessing(a).count(word))

len1 = 100-len(bag_of_words_a)
for i in range(0,len1):
    bag_of_words_a.append(0)


for word in tokens:

    bag_of_words_b.append(text_preprocessing(b).count(word))

len2 = 100-len(bag_of_words_b)
for i in range(0,len2):
    bag_of_words_b.append(0)

print(bag_of_words_a)
print(bag_of_words_b)


print("cosine similarity {:.2f}".format(round(compute_cosine_similarity(bag_of_words_a,bag_of_words_b), 2)))
