from nltk.corpus import wordnet
from .similarities import check_similarity

def create_relation_set(ans_set):
	th=1.0
	rel_set=set()
	set_len,word_len=0,0
	for key in ans_set:
		temp_rel=set()
		s0=wordnet.synsets(ans_set[key][0])
		s1=wordnet.synsets(ans_set[key][1])
		for a_set in ans_set:
			s2=wordnet.synsets(ans_set[a_set][0])
			s3=wordnet.synsets(ans_set[a_set][1])
			if (s0 and s2) and (s1 and s3):
				w1=check_similarity(s0,s2)
				w2=check_similarity(s1,s3)
				if (w1+w2>th):
					noun=ans_set[a_set][0]+" "+ans_set[a_set][1]
					temp_rel.add(noun)
				word_len=max(word_len,len(noun))
		set_len=max(set_len,len(temp_rel))
		rel_set.add(tuple(temp_rel))
	return rel_set,set_len,word_len
