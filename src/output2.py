def _print_2(sen_len,word_len):
    for i in range(0,sen_len):
        print("+",end="")
        for j in range(0,word_len+1):
            print("-",end="")
    print("+")

def display_2(rel_set,set_len,word_len):
    _print_2(set_len,word_len)
    for pairs in rel_set:
        for pair in pairs:
            pair=str(pair)
            print("+ "+pair,end="")
            for i in range(0,word_len-len(pair)):
                    print(" ",end="")
        for i in range(0,set_len-len(pairs)):
            print("+ ",end="")
            for i in range(0,word_len):
                    print(" ",end="")
        print("+")
        _print_2(set_len,word_len)