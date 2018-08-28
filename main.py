from itertools import permutations
from os.path import expanduser
from nltk.tag.senna import SennaTagger
from src.preprocess import get_word_list
from src.extraction import extract_noun
from src.relation import create_relation_set
from src.output1 import display_1
from src.output2 import display_2

home=expanduser("~")
st=SennaTagger(home+'/senna')

f=open("files/in.dat","r")
para=f.read()
f.close()

sentences=para.split(".")
ans_set={}
sen_len,word_len=0,0

for sentence in sentences:
        #print(sentence)
        sentence=sentence.strip()
        words=st.tag(sentence.split())
        #print(words)
        word_list=get_word_list(words)
        if(len(word_list)<2):
                continue
        pair_list=list(permutations(word_list,2))
        #print(pair_list)
        ans_set[sentence]=extract_noun(pair_list)
        noun=ans_set[sentence][0]+" "+ans_set[sentence][1]
        word_len=max(word_len,len(noun))
        sen_len=max(sen_len,len(sentence))

display_1(ans_set,sen_len,word_len)
rel_set,set_len,word_len=create_relation_set(ans_set)
print("\nGrouping:")
display_2(rel_set,set_len,word_len)