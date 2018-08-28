from nltk.corpus import wordnet
from .similarities import check_similarity

f=open("files/corpus.dat","r")
data=f.read()
data=data.split("\n")
sample_set=[a_set.split() for a_set in data if a_set]
#print(sample_set)

def extract_noun(pair_list):
	dic={}
	for pair in pair_list:
		dic[pair]=0
		s0=wordnet.synsets(pair[0])
		s1=wordnet.synsets(pair[1])
		for a_set in sample_set:
			s2=wordnet.synsets(a_set[0])
			s3=wordnet.synsets(a_set[1])
			if (s0 and s2) and (s1 and s3):
				w1=check_similarity(s0,s2)
				w2=check_similarity(s1,s3)
				w=(w1+w2)/2
				#print(pair,a_set,w)
				dic[pair]=max(dic[pair],w)
	#print(dic)
	ans=max(dic,key=lambda i:dic[i])
	#print("\nINTERPRETED COMPOUND NOUN : "+ans)
	return ans