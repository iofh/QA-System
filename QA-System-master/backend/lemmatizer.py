
#!/home/student/QA-System/qa_env python3

import os
import pickle
import pandas as pd
import spacy
import numpy as np
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import gc
import torch

def lemmatize(phrase):
    """Return lematized words"""
    spa = spacy.load("en_core_web_sm")
    return " ".join([word.lemma_ for word in spa(phrase)])

def reading_csv(path_to_csv):
    """Return text column in csv"""
    data = pd.read_csv(path_to_csv)
    ctx_paragraph = []
    for txt in data['text']:
        if not pd.isna(txt):
            ctx_paragraph.append(txt)
    return ctx_paragraph

def lemmatizer(paragraphs, domain_lemma_cache, domain_pickle):
    lemma_cache = domain_lemma_cache
    if not os.path.isfile(lemma_cache):
        lemmas = [lemmatize(par) for par in tqdm(paragraphs)]
        df = pd.DataFrame(data={'context': paragraphs, 'lemmas': lemmas})
        df.to_feather(lemma_cache)
        
    if not os.path.isfile(VEC_PICKLE_LOC):
        vectorizer = TfidfVectorizer(
            stop_words='english', min_df=5, max_df=.5, ngram_range=(1, 3))
        pickle.dump(vectorizer, open(VEC_PICKLE_LOC, "wb"))
        
    if not os.path.isfile(domain_pickle):
        tfidf = vectorizer.fit_transform(lemmas)
        pickle.dump(tfidf, open(domain_pickle, "wb"))
        

domains_choices = {
    'auckland':('/home/student/QA-System/backend/files/data/auckland_uni/auckland.csv',
          '/home/student/QA-System/backend//backend/files/data/auckland_uni/auckland.feather',
          '/home/student/QA-System/backend//backend/files/data/auckland_uni/auckland_tfidf.pickle'),
    'otago':('/home/student/QA-System/backend//files/data/otago_uni/otago.csv',
          '/home/student/QA-System/backend//files/data/otago_uni/otago.feather',
          '/home/student/QA-System/backend//files/data/otago_uni/otago_tfidf.pickle'),
    'canterbury':('/home/student/QA-System/backend//files/data/canterbury_uni/canterbury.csv',
          '/home/student/QA-System/backend//files/data/canterbury_uni/canterbury.feather',
          '/home/student/QA-System/backend//files/data/canterbury_uni/canterbury.pickle'),
    'massey':('/home/student/QA-System/backend//files/data/massey_uni/massey.csv',
          '/home/student/QA-System/backend//files/data/massey_uni/massey.feather',
          '/home/student/QA-System/backend//files/data/massey_uni/massey_tfidf.pickle'),
    'wgtn':('/home/student/QA-System/backend//files/data/wgtn/wgtn.csv',
          '/home/student/QA-System/backend//files/data/wgtn/wgtn.feather',
          '/home/student/QA-System/backend//files/data/wgtn/wgtn_tfidf.pickle')
}      
        

for i in domains_choices:   
    LEMMA_CACHE = domains_choices[i][1]
    csvpath = domains_choices[i][0]
    pickle_cache = domains_choices[i][2]
    paragraphs = reading_csv(csvpath)
    lemmatizer(paragraphs, LEMMA_CACHE, pickle_cache)