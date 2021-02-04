from copy import deepcopy

gram_file = open("test_set.txt", 'r')
    
def make_sentences(string,source="test_set_separated.txt"):
    sentence_help = 0 #check "(" and ")"
    start = 0
    gram_sentences = []
    for i in range(len(string)):
        if(string[i] == "(" ):
            sentence_help += 1
        elif(string[i] == ")"):
            sentence_help -= 1
            if(sentence_help == 0 ):
                gram_sentences.append(string[start:i+1])
                start = i+2       
    text_sentences = deepcopy(gram_sentences)
    file_source = open(source, 'w', newline='')
    for sentence in text_sentences:
        if(sentence[:2] != "(c"):
            file_source.write(sentence + '\n')
    file_source.close()

if __name__ == "__main__":
    string = ""
    lines = gram_file.read().splitlines()
    for line in lines:
        string += line + " "

    make_sentences(string)


             
         
         
         
    
