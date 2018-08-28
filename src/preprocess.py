#sort out unnecessary words
def get_word_list(words):
	valid_words=["NN","VB","VBG","VBN","JJ"]
	word_list=[]
	for word in words:
		if(word[1] in valid_words and word[0] not in word_list):
			word_list.append(word[0])
	return word_list
