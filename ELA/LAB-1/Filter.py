from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
text = "What is Web Mining? Web Mining is the process of ''Data Mining'' techniques, and extract information from Web documents and services. The main purpose of web mining is discovering useful information from the World-Wide Web and it's usage patterns"
punctuations = '!@#$%^&*()_+=-`~?\':\|"/.,<>;[]'
without_punctuation = ""

for char in text:
    if char not in punctuations:
        without_punctuation+=char

stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(without_punctuation)
 
filtered_words = [w for w in word_tokens if not w.lower() in stop_words]
 
filtered_words = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_words.append(w)
 
# print(word_tokens)
print("Words without stop-words and punctuations are: \n", filtered_words)