from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

text="What is Web Mining? Web Mining is the process of ‘’Data Mining” techniques, and extract information from Web documents and services. The main purpose of web mining is discovering useful information from the World-Wide Web and it’s usage patterns"
text_tokens=word_tokenize(text)

print(text_tokens)

# tokens_without_sw=[word for word in text_tokens if not word in stopwords.words()]
# print(tokens_without_sw)

# filtered_sentence=(" ").join(tokens_without_sw)
# print(filtered_sentence)

# print(stopwords.words('english'))

# all_stopwords=stopwords.words('english')
# all_stopwords.append('play')
# text_tokens=word_tokenize(text)
# tokens_without_sw=[word for word in text_]