from copy import deepcopy

file_ground_truth = open("C:/Users/pasca/Dropbox/PaktikumTextimaging/rnng-master/Thomas_Mann_Der_kleine_Herr_Friedemann_Ground_Truth.txt", "r") #Franz_Kafka_Auf_der_Galerie_Quelle_DigBib_Ground_Truth.txt","r") #Franz_Kafka_Das_Urteil_Ground_Truth.txt","r")
file_pred = open("C:/Users/pasca/Dropbox/PaktikumTextimaging/rnng-master/Thomas_Mann_Der_kleine_Herr_Friedemann_predict.txt", "r") #Franz_Kafka_Auf_der_Galerie_Quelle_DigBib_predict.txt","r") #Franz_Kafka_Das_Urteil_predict.txt", "r")   
chars = ["(t", "(s", "(seg", "))", "T1","T2","T3","T4","T5","T6"]

def eval_char(list_gt, list_pred, char):
    chars_gt = 0
    chars_pred = 0
    matches = 0
    char_list = []
    t_list = ["))",")))","))))",")))))","))))))",")))))))"]
    
    for elem in list_gt:
        if(char[0] == "T"):
            if((t_list[int(char[1])-1] in elem[0]) and (t_list[int(char[1])] not in elem[0])):
                chars_gt += 1
        elif(char == elem[0] or (char in elem[0] and char == "))")):
            chars_gt += elem[2]
            
    for elem in list_pred:
        if(char[0] == "T"):
            if((t_list[int(char[1])-1] in elem[0]) and (t_list[int(char[1])] not in elem[0])):
                chars_pred += 1
                char_list.append(elem)
        elif(char == elem[0] or (char in elem[0] and char == "))")):
            chars_pred += elem[2]
            char_list.append(elem)
            
    gt_copy = deepcopy(list_gt)
    for elem in char_list:
        for i in range(len(gt_copy)):
            if(elem[0] == gt_copy[i][0] and elem[1] == gt_copy[i][1]):
                if(char[0] == "T"):
                    matches += 1
                else:
                    matches += elem[2] if (elem[2] <= gt_copy[i][2]) else gt_copy[i][2]
                gt_copy.pop(i)
                break
    
    if(char == "))"):
        char = ")"

    prec = 0 if chars_gt == 0 else (matches/chars_gt)*100
    rec = 0 if chars_pred == 0 else (matches/chars_pred)*100
    print("{:6s}|{:16d}|{:15d}|{:13.3f}|{:9.3f}".format(char, chars_gt, chars_pred, prec, rec))  

gt = []
lines = file_ground_truth .read().splitlines()
for line in lines:
    gt += line.split(" ")

help1= [] #only test
help2= [] # -_____-

"""
for i in range(len(gt)):
    if("(w" in gt[i]):
        help1.append(gt[i] + gt[i+1])
    elif("(c" in gt[i]):
        if("»" in gt[i+1] or "«" in gt[i+1] or "€" in gt[i+1]):
            help1.append(gt[i] + gt[i+1])
        else:
            for char in gt[i+1]:
                if(char != ")"):
                    help1.append(gt[i] + char)

"""
       
list_gt = []
counter = 0

for i in range(len(gt)):
    if("(c" in gt[i]):
        if("»" in gt[i+1] or "«" in gt[i+1] or "€" in gt[i+1]):
            counter += 1
        else:
            for char in gt[i+1]:
                counter += 1 if(char != ")") else 0 #for position from token
    elif("(w" in gt[i]):
            counter += 1
    elif("(t" in gt[i] or "(s" in gt[i] or "(seg" in gt[i]):
        list_gt.append((gt[i],counter,1))
    elif("))" in gt[i]):
        number = -1 #for # ")" ,-1 because 1 is for closed token w or c
        for char in gt[i]:
            number += 1 if(char == ")") else 0
        list_gt.append((gt[i],counter,number))
    else:
        pass

print("#Ground Truth: ", len(list_gt))

pred = []
lines = file_pred.read().splitlines()
for line in lines:
    split = line.split(" ")
    help_ = 0 #for finding "(t ... "
    for elem in split:
        if("(t" == elem):
            break
        help_ += 1
    pred += split[help_:]

"""
for i in range(len(pred)-1):
    if("(XX" in pred[i]):
        help2.append(pred[i] + pred[i+1])
for i in range(len(help1)):
    print(help1[i],"_____",help2[i])########################################################
"""

list_pred = []
counter = 0

for elem in pred:
    if("(XX" in elem):
        counter += 1 #for position from token
    elif("(t" in elem or "(s" in elem or "(seg" in elem):
        list_pred.append((elem,counter,1))
    elif("))" in elem):
        number = -1 #for # ")" ,-1 because 1 is for closed token w or c
        for char in elem:
            if(char == ")"):
                number += 1
        list_pred.append((elem,counter,number))
    else:
        pass
"""
print("#Prediction: ", len(list_pred))
min_ = len(list_pred) if(len(list_pred) <= len(list_gt)) else len(list_gt)
for i in range(min_):
    if("(t" in list_gt[i][0] or "(t" in list_pred[i]):
        print(list_gt[i],"_____",list_pred[i])
"""
print("#Wörter und Zeichen Ground Truth:", list_gt[-1][1])
print("#Wörter und Zeichen Preciction:", list_pred[-1][1])

print("File: Franz_Kafka_Auf_der_Galerie_Quelle_DigBib")
print("Token | # Ground Truth | # predictions | % precision | % recall")
print("---------------------------------------------------------------")

for char in chars:
    eval_char(list_gt, list_pred, char)
   
