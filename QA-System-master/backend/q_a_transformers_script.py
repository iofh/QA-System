# !python -m spacy download en_core_web_sm

"""Required modules"""
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

VEC_PICKLE_LOC = "/home/student/QA-System/backend/files/data/vectorizer.pickle"

#lemmas word
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

def processing_question(ques, paragraphs, domain_lemma_cache, domain_pickle):
    """Return answer"""
    #Lemmatizing whole csv text column
    lemma_cache = domain_lemma_cache
    if not os.path.isfile(lemma_cache):
        lemmas = [lemmatize(par) for par in tqdm(paragraphs)]
        df = pd.DataFrame(data={'context': paragraphs, 'lemmas': lemmas})
        df.to_feather(lemma_cache)
    df = pd.read_feather(lemma_cache)
    paragraphs = df.context
    lemmas = df.lemmas
    #Vectorizor cache
    if not os.path.isfile(VEC_PICKLE_LOC):
        vectorizer = TfidfVectorizer(
            stop_words='english', min_df=5, max_df=.5, ngram_range=(1, 3))
        vectorizer.fit_transform(lemmas)
        pickle.dump(vectorizer, open(VEC_PICKLE_LOC, "wb"))      
    #Vectorized lemmas cache cache
    if not os.path.isfile(domain_pickle):
        tfidf = vectorizer.fit_transform(lemmas)
        pickle.dump(tfidf, open(domain_pickle, "wb"))
    vectorizer = pickle.load(open(VEC_PICKLE_LOC, "rb"))
    tfidf = pickle.load(open(domain_pickle, "rb"))
    question = ques
    query = vectorizer.transform([lemmatize(question)])
    (query > 0).sum(), vectorizer.inverse_transform(query)
    scores = (tfidf * query.T).toarray()
    results = (np.flip(np.argsort(scores, axis=0)))
    qapipe = pipeline('question-answering',
                      model='distilbert-base-uncased-distilled-squad',
                      tokenizer='bert-base-uncased',
                      device=0)
    candidate_idxs = [(i, scores[i]) for i in results[0:10, 0]]
    contexts = [(paragraphs[i], s) for (i, s) in candidate_idxs if s > 0.01]
    question_df = pd.DataFrame.from_records([{
        'question': question,
        'context':  ctx
    } for (ctx, s) in contexts])
    preds = qapipe(question_df.to_dict(orient="records"))
    torch.cuda.empty_cache()
    gc.collect()
    answer_df = pd.DataFrame.from_records(preds)
    #torch.cuda.empty_cache()
    #gc.collect()
    answer_df['context'] = question_df['context']
    answer_df = answer_df.sort_values(by="score", ascending=False)
    return answer_df

# def question_answer(domain, question):
#     """API method"""
#     domains_choices = {
#         'op':('./files/data/op/op.csv',
#               './files/data/op/op.feather',
#               './files/data/op/op_tfidf.pickle')
#     }
#     domain_lemma_cache = domains_choices[domain][1]
#     csvpath = domains_choices[domain][0]
#     pickle_cache = domains_choices[domain][2]
#     paragraphs = reading_csv(csvpath)
#     ques = question
#     result_df = processing_question(ques, paragraphs, domain_lemma_cache, pickle_cache)
#     return result_df

# def question_answer(domain, question):
#     """API method"""

torch.cuda.empty_cache()

gc.collect()
domains_choices = {
    'op':('/home/student/QA-System/backend/files/data/op/op.csv',
          '/home/student/QA-System/backend/files/data/op/op.feather',
          '/home/student/QA-System/backend/files/data/op/op_tfidf.pickle')
}
domain = 'op'
ques = "Where is the department for electrical engineering"
domain_lemma_cache = domains_choices[domain][1]
csvpath = domains_choices[domain][0]
pickle_cache = domains_choices[domain][2]
paragraphs = reading_csv(csvpath)
# ques = question
result_df = processing_question(ques, paragraphs, domain_lemma_cache, pickle_cache)
print(result_df.iloc[0])
# return result_df
