

#reading and writing files -------------------------------------------------------------
from pypdf import PdfReader as pdf
import nltk
import spacy
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import treebank

import en_core_web_sm

nlp = en_core_web_sm.load()






testFile = open("C:/Users/vince/OneDrive/Documents/PythonTest.txt")

reader = pdf("C:/Users/vince/Dropbox/Vincenzo Martemucci - Resume August 2024.pdf")
print(testFile.read())
all_text = ''
for page in reader.pages:
    all_text += page.extract_text() + '\n'
#print(all_text)

tokens = nltk.word_tokenize(all_text)
#print(tokens)

nlp = spacy.load("en_core_web_sm")
doc = nlp(all_text)
print(doc)

filtered_words = [token.text for token in doc if not token.is_stop]
clean_text = ' '.join(filtered_words)
# print("Text after Stopword Removal:", clean_text)