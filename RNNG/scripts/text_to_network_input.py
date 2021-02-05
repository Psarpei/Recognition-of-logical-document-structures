import argparse

ap = argparse.ArgumentParser()
ap.add_argument('filename')
#filename = "C:/Users/pasca/Dropbox/PaktikumTextimaging/rnng-master/Franz_Kafka_Das_Urteil"

if __name__ == "__main__":
    args = ap.parse_args()
    txt_file = open(args.filename, 'r')
    #txt_file = open(filename +".txt", 'r')
    target_file = open(args.filename[:-4] + "_graminput.txt", 'w')
    #target_file = open(filename + "_graminput.txt", 'w')
    whole_txt_splitted = txt_file.read().split(" ")
    gram_str = "(t"
    for word in whole_txt_splitted:
        if word == '':
            continue
        i = 0
        last_i = 0
        while i < len(word):
            if word[i] not in "QWERTZUIOPÜASDFGHJKLÖÄYXCVBNMqwertzuiopüasdfghjklöäyxcvbnmß1234567890":
                if word[last_i:i] != "":
                    gram_str += " (w " + word[last_i:i] + ")"
                gram_str += " (c " + ("[" if word[i] == "(" else ("]" if word[i] == ")" else word[i])) + ")"
                last_i = i+1
            i += 1    
        if word[last_i:i] != '':
            gram_str += " (w " + word[last_i:i] + ")"
    gram_str.replace("  ", " ")
    """start_bracket = False
    start_word = False
    total = True
    for i in range(len(gram_str)):
        if start_word:
            if gram_str[i] == ")":
                start_bracket = False
                start_word = False
            elif gram_str[i] not in " QWERTZUIOPÜASDFGHJKLÖÄYXCVBNMqwertzuiopüasdfghjklöäyxcvbnmß1234567890":
                print(i, "Example: ", gram_str[i-30:i+30])
                total = False
        if start_bracket and not start_word and gram_str[i] == "w":
            start_word = True
        if gram_str[i] == "(":
            start_bracket = True"""
    #print(whole_txt_splitted[-40:])
    #print(gram_str)
    target_file.write(gram_str + ")")
