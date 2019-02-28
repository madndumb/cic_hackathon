from nltk_stopwords import Stopwords,Tfcompute

alpha=Stopwords('the the the the the the abcdsfesfsdfs  abcdsfesfsdfs abcdsfesfsdfs abcdsfesfsdfs')
beta=Tfcompute(alpha)
x=beta.wordListToFreqDict()
print(alpha.nontrivial_words())
