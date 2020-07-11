from typing import List

import gensim.corpora as corpora
from gensim.corpora import Dictionary


def create_dictionary(data_lemmatized: List[List[str]]):
	return corpora.Dictionary(data_lemmatized)


def term_document_matrix(texts, dictionary: Dictionary):
	return [dictionary.doc2bow(text) for text in texts]