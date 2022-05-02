from nltk.tokenize import sent_tokenize

text = "What is Web Mining? Web Mining is the process of ‘’Data Mining” techniques, and extract information from Web documents and services. The main purpose of web mining is discovering useful information from the World-Wide Web and it’s usage patterns"
sent_tokens = sent_tokenize(text)

print("Tokenized sentences are: \n", sent_tokens)