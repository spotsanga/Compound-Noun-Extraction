from nltk.corpus import wordnet

def check_similarity_all(syn1,syn2):
    max_wei=0
    for s1 in syn1:
        for s2 in syn2:
            wei=s1.wup_similarity(s2)
            if(wei):
                max_wei=max(max_wei,wei)
    return max_wei

def check_similarity(syn1,syn2):
    wei=syn1[0].wup_similarity(syn2[0])
    if wei:
        return wei
    return 0