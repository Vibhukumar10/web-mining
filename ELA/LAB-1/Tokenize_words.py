from nltk.tokenize import word_tokenize

text = "What is Web Mining? Web Mining is the process of ‘’Data Mining” techniques, and extract information from Web documents and services. The main purpose of web mining is discovering useful information from the World-Wide Web and it’s usage patterns"
word_tokens = word_tokenize(text)

print("Tokenized words are: \n", word_tokens)