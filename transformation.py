import joblib
import spacy, en_core_web_sm
from spacy.lang.en.stop_words import STOP_WORDS
import string
from spacy.lang.en import English
from sklearn.base import TransformerMixin 


'''
Custom spaCy transformer trained on 
'''
class predictors(TransformerMixin):
    def transform(self, data, **transform_params):
        return [self.clean_text(text) for text in data]
    def fit(self, data, y, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}
    
        # Basic function to clean the text 
    def clean_text(self, text):     
        return text.strip().lower()
    
  
'''
Tokenize a given sentence, remove stopwords and punctuation as well
'''
def my_tokenizer(sentence):
    nlp = en_core_web_sm.load()
    stopwords = list(STOP_WORDS)
    punctuations = string.punctuation
    parser = English()
    mytokens = parser(sentence)
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    mytokens = [ word for word in mytokens if word not in stopwords and word not in punctuations ]
    return mytokens
  




    
    