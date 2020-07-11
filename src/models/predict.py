from typing import List

import gensim

def predict(tokens: List[str]):
	lda_model = gensim.models.ldamodel.LdaModel.load("../../data/models/lda_model.pkl")

	predictions = []
	for token in tokens:
		prediction = {
			'id': token,
			'topics': lda_model.get_term_topics(token)
		}
		prediction.append(prediction)

	return predictions