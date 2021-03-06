# Recognition of logical document structures
Rocognition of logical document structures for german language based on [recurrent neural network grammars](https://arxiv.org/abs/1602.07776/). 

This work is the preliminary work of the paper [Recognizing Sentence-level Logical Document Structures with the Help of
Context-free Grammars](https://www.aclweb.org/anthology/2020.lrec-1.650.pdf) 
## General information
<img align="right" width="300" height="" src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Logo-Goethe-University-Frankfurt-am-Main.svg">

**Instructors**
* [Prof. Dr. Alexander Mehler](https://www.texttechnologylab.org/team/alexander-mehler/), email: mehler@em.uni-frankfurt.de
* [Dr. Wahed Hemati](https://www.texttechnologylab.org/team/wahed-hemati/), email: hemati@em.uni-frankfurt.de

**Institutions**
* **[Goethe University](http://www.informatik.uni-frankfurt.de/index.php/en/)**
* **[TTLab - Text Technology Lab](https://www.texttechnologylab.org/)**

**Project team**
* [Fabian Vogel](https://github.com/legnaib)
* [Pascal Fischer](https://github.com/Psarpei)

**Configuration**

Take a look here for the correct configuration [recurrent neural network grammars](https://github.com/clab/rnng)

## Project
The model is able to recognizing the followig logical document structures
* ```(t``` - text start
* ```(s``` - sentence start
* ```(seg``` - segment start
* ```(w``` - word start
* ```(c``` - char start
* ```)``` end of logical document structure
* ```Ti``` - sentence/segment depth will be measured recursive 

**Example**

The sentence
    
```Georg Bendemann, ein junger Kaufmann,  saß in seinem Privatzimmer im ersten Stock eines der niedrigen leichtgebauten Häuser, die entlang des Flusses in einer langen Reihe, fast nur in der Höhe und Färbung unterschieden, sich hinzogen.```

should be predicted as
    
```(s (seg (w Georg) (w Bendemann) (c ,)) (seg (w ein) (w junger) (w Kaufmann) (c ,)) (seg (w saß) (w in) (w seinem) (w Privatzimmer) (w im) (w ersten) (w Stock) (w eines) (w der) (w niedrigen) (c ,)) (seg (w leichtgebauten) (w Häuser) (c ,)) (seg (w die) (w entlang) (w des) (w Flusses) (w in) (w einer) (w langen) (w Reihe) (c,)) (seg (w fast) (w nur) (w in) (w der) (w Höhe) (w und) (w Färbung) (w unterschieden) (c ,)) (seg (w sich) (w hinzogen) (c .)))```

**Training results**

<img align="center" width="500" height="" src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Train_example2.png">

**Validation results**

<img align="center" width="500" height="" src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Test_example2.png">

**Prediction**

The model is able to predict the output in the usually format like in example_predict.txt. or in the .xml format like in example_XML.tei.

In following ```DATANAME``` is a free selectable name. 

There are to options to make a prediction:
* You have the ground truth of a text and you want to predict the rnng-output as ```.tei``` file as well as the evaluation. For this you have to save your ground_truth data as ```DATANAME_Ground_Truth.txt```.
* You only want to predict the rnng-output. For this you have to save your text in the file ```DATANAME.txt``` as plain text.

In both cases you have to save your files in the directory ```/PLACE_YOUR_FILES_HERE```

To make a prediciton (and get the evaluation results) you only have to navigate to the directory of the ```predict.sh``` file and execute 

    ./predict.sh DATEINAME 

The following files are generated in the ```/PLACE_YOUR_FILES_HERE directory```

* ```DATEINAME_graminput.txt```: The rnng input file 
* ```DATEINAME_predict.txt```: The prediction in grammar format.
* ```DATEINAME.tei```: This is the final rnng out file which contains the prediction in .tei format.
* ```DATEINAME.txt```: The purely input text without grammar format is saved here (if not available).
* ```DATEINAME_Ground_Truth.txt```: This file only exists if, you saved a ground truth file here.
* ```DATEINAME_evaluation.txt```: Here you can find the evaluation results (this file only exists if you have saved a ground truth file).
