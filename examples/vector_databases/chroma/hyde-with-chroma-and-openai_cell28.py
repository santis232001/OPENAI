claim_query_result = scifact_corpus_collection.query(query_texts=claims, include=['documents', 'distances'], n_results=3)