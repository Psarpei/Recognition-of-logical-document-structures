"""Convert prediction of Network to .tei file and correct the _predict.txt file"""

from lxml import etree
import lxml.etree as ET
import time
import argparse

#file_network_input = open("/home/svogel/projects/textimaging/rnng-master/Franz_Kafka_Das_Urteil_graminput.txt", "r") #Thomas_Mann_Der_Tod_in_Venedig_Neu_graminput.txt", "r") #
#file_pred = open("/home/svogel/projects/textimaging/rnng-master/Franz_Kafka_Das_Urteil_predict.txt", "r") #Thomas_Mann_Der_Tod_in_Venedig_Neu_predict.txt","r")  # 
#file_pred = open("C:/Users/pasca/Dropbox/PaktikumTextimaging/raw/predicted_gram/Franz_Kafka_Der_Gruftwaechter_Quelle_DigBib_predict.txt", "r") #Thomas_Mann_Der_Tod_in_Venedig_Neu_predict.txt","r")  # 
p = argparse.ArgumentParser()
p.add_argument('file')

if __name__ == "__main__":
    args = p.parse_args()
    file_network_input = open(args.file + '_graminput.txt', 'r')
    file_pred = open(args.file + '_predict.txt', 'r')
    def get_clips(string):
        first = True
        clips = ""
        for char in string:
            if char == ")":
                clips += "" if first else ")"
                first = False
        return clips

    network_input = ["(t"]
    lines = file_network_input.read().splitlines()
    for line in lines:
        # correctly working with multiple (t: Convert all t into only an outer t
        network_input += line[3:-1].split(" ")
    network_input[-1] += ")"

    pred = ["(t"]
    lines = file_pred.read().splitlines()
    for line in lines:
        split = line[:-1].split(" ")
        help_ = 0 #for finding "(t ... "
        for elem in split:
            if("(t" == elem):
                break
            help_ += 1
        pred += split[help_+1:]
    pred[-1] += ")"

    def get_full_prediction(network_input, pred):
        """Network outputs some weird changes, i.e. (XX ) instead of (w ) and some words are not correctly written
        
        This method corrects the output"""

        w_and_c = []
        #print("Network: ", network_input[:100])
        #print("pred: ", pred[:100])
        for i in  range(len(network_input)):
            if("(w" in network_input[i] or "(c" in network_input[i]):
                w_and_c.append(network_input[i] + " " + network_input[i+1])

        counter = 0
        helpBool = False #for let the words from prediction out
        full_pred = ""
        for i in range(len(pred)):
            if(helpBool):
                helpBool = False
            elif("(XX" in pred[i]):
                full_pred += w_and_c[counter] + get_clips(pred[i+1]) + " "
                counter +=1
                helpBool = True
            else:
                full_pred += pred[i] + " "
            
        return full_pred[:-2]

    def create_xml(full_pred):
        """Convert the corrected predicted output to a complete .tei file"""
        publication_stmt = ["Timestamp", "Number of tokens", "Number of unknown tokens",
                            "Number of word forms", "TTR", "Guiraud", "MTLD",
                            "Number of punctuation marks", "Number of lemmata", "Number of segments",
                            "Number of level-1 segments", "Number of level-2 segments",
                            "Number of level-3 segments", "Number of level-4 segments",
                            "Number of level-5 segments", "Number of level-6 segments",
                            "Number of level-7 segments", "Maximum segment level", "Number of quotes",
                            "Number of sentences", "Number of level-1 sentences",
                            "Number of level-2 sentences", "Number of level-3 sentences",
                            "Maximum sentence level", "Number of paragraphs", "Number of divisions",
                            "Number of captions", "Number of tables","Number of named entities",
                            "Number of nouns", "Number of verbs", "Number of adjectives",
                            "Number of adverbs"]
        elements = []
        preds = full_pred.split(" ")
        s_count = 0
        s_count_deep = [0,0,0,0,0,0]
        s_deep = 1
        seg_count = 0
        seg_count_deep = [0,0,0,0,0,0,0,0,0]
        seg_deep = 1
        w_count = 0
        c_count = 0
        
        tei = ET.Element("TEI", id="TEI1")
        elements.append(ET.SubElement(tei, "teiHeader"))
        elements.append(ET.SubElement(elements[0],"fileDesc"))
        elements.append(ET.SubElement(elements[1],"titleStmt"))
        elements.append(ET.SubElement(elements[2],"title"))
        elements[3].text = "PlainText"
        elements.append(ET.SubElement(elements[1],"publicationStmt"))

        for stmt in publication_stmt:
            elements.append(ET.SubElement(elements[4],"idno", type=stmt))
            elements[-1].text = "0"
            
        elements.append(ET.SubElement(elements[1],"sourceDesc"))
        elements.append(ET.SubElement(elements[38],"p", Name= "TTLab-Corpus; tagging by RNNG prediction from Fabian Vogel and Pascal Fischer"))
        stack = [tei]
        elements.append(ET.SubElement(tei, "text", id="text1"))
        stack.append(elements[-1])
        elements.append(ET.SubElement(stack[-1], "body", id="body1"))
        stack.append(elements[-1])
        for pred in preds[1:]:
            if(pred == "(s"):
                elements.append(ET.SubElement(stack[-1], "s", id="s"+str(s_count), n=str(s_deep)))
                stack.append(elements[-1])
                s_count += 1
                s_count_deep[s_deep -1] += 1
                s_deep += 1
                #if(s_deep == 4):
                #    print(s_deep)
            elif(pred == "(seg"):
                elements.append(ET.SubElement(stack[-1], "seg", id="seg"+str(seg_count), n=str(seg_deep+1)))
                stack.append(elements[-1])
                seg_count += 1
                seg_count_deep[seg_deep -1] += 1
                seg_deep += 1
            elif(pred == "(w"):
                elements.append(ET.SubElement(stack[-1], "w", id="w"+str(w_count), lemma="unknown", type="unknown", ana="unknown"))
                w_count += 1
            elif(pred == "(c"):
                elements.append(ET.SubElement(stack[-1], "c", type="PUN"))
                c_count += 1
            else:
                txt= ""
                clips = -1
                for char in pred:
                    if(char == ")"):
                        clips += 1
                    else:
                        txt += char
                elements[-1].text = txt
                for i in range(clips):
                    if(stack[-1].tag == "s"):
                        s_deep -= 1
                    else:
                        seg_deep -= 1
                    stack.pop()
                elements.append(ET.SubElement(stack[-1], "c",))
                elements[-1].text= " "
        #print("Satztiefen: ", s_count_deep)                
        #print("Segmenttiefen: ", seg_count_deep)                

        elements[5].text= time.strftime("%d.%m.%Y")
        elements[6].text= str(w_count)
        elements[7].text= str(w_count)
        words = []
        quotes = 0
        
        for i in range(len(preds)-1):
            if(preds[i] == "(w"):
                word = ""
                for char in preds[i+1]:
                    if(char != ")"):
                        word += char
                words.append(word)
            if('»' in preds[i]):
                quotes += 1

        elements[8].text = str(len(list(set(words))))
        elements[12].text = str(c_count)
        elements[14].text = str(seg_count)
        max_seg_lvl = 0
        
        for i in range(7):
            elements[15+i].text = str(seg_count_deep[i])
            if(seg_count_deep[i] > 0):
                max_seg_lvl += 1

        elements[22].text = str(max_seg_lvl)
        elements[23].text = str(quotes)
        elements[24].text = str(s_count)
        max_s_lvl = 0
        for i in range(3):
            elements[25+i].text = str(s_count_deep[i])
            if(s_count_deep[i] > 0):
                max_s_lvl += 1
        elements[28].text = str(max_s_lvl)
                
        

        tree = ET.ElementTree(tei)
        with open(args.file+".tei", "wb") as writter:
            writter.write(etree.tostring(tree, pretty_print=True,\
                                        xml_declaration=True,encoding='UTF-8'))

    full_pred = get_full_prediction(network_input, pred)
    # safe the corrected version of the prediction
    with open(args.file + '_predict.txt',"w") as pred_file:
        pred_file.write(full_pred)
    create_xml(full_pred)

