text_5 = """Ethiopia's crop production up 24%

Ethiopia produced 14.27 million tonnes of crops in 2004, 24% higher than in 2003 and 21% more than the average of the past five years, a report says.

In 2003, crop production totalled 11.49 million tonnes, the joint report from the Food and Agriculture Organisation and the World Food Programme said. Good rains, increased use of fertilizers and improved seeds contributed to the rise in production. Nevertheless, 2.2 million Ethiopians will still need emergency assistance.

The report calculated emergency food requirements for 2005 to be 387,500 tonnes. On top of that, 89,000 tonnes of fortified blended food and vegetable oil for "targeted supplementary food distributions for a survival programme for children under five and pregnant and lactating women" will be needed.

In eastern and southern Ethiopia, a prolonged drought has killed crops and drained wells. Last year, a total of 965,000 tonnes of food assistance was needed to help seven million Ethiopians. The Food and Agriculture Organisation (FAO) recommend that the food assistance is bought locally. "Local purchase of cereals for food assistance programmes is recommended as far as possible, so as to assist domestic markets and farmers," said Henri Josserand, chief of FAO's Global Information and Early Warning System. Agriculture is the main economic activity in Ethiopia, representing 45% of gross domestic product. About 80% of Ethiopians depend directly or indirectly on agriculture.
"""

vec = np.array(get_vector(text_5), dtype=np.float32).tobytes()
q = Query('@content:recession => [KNN 3 @vector $query_vec AS vector_score]')\
    .sort_by('vector_score')\
    .return_fields('vector_score', 'content')\
    .dialect(2)    
params = {"query_vec": vec}

results = client.ft('idx').search(q, query_params=params)
for doc in results.docs:
    print(f"distance:{round(float(doc['vector_score']),3)} content:{doc['content']}\n")