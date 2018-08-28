def _print_1(sen_len,word_len):
        print("+",end="")
        for i in range(0,sen_len+1):
                print("-",end="")
        print("+",end="")
        for i in range(0,word_len+1):
                print("-",end="")
        print("+")

def display_1(ans_set,sen_len,word_len):
    _print_1(sen_len,word_len)
    for key in ans_set:
            print("+ "+key,end="")
            for i in range(0,sen_len-len(key)):
                    print(" ",end="")
            noun=ans_set[key][0]+" "+ans_set[key][1]
            print("+ "+noun,end="")
            for i in range(0,word_len-len(noun)):
                    print(" ",end="")
            print("+")
            _print_1(sen_len,word_len)