# Recognizing-logical-document-structures
Rocognition of logical document structures based on [recurrent neural network grammars](https://arxiv.org/abs/1602.07776/). 

This work is the preliminary work of the paper [Recognizing Sentence-level Logical Document Structures with the Help of
Context-free Grammars](https://arxiv.org/abs/1602.07776) 
## General Information
<img align="right" width="300" height="" src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Logo-Goethe-University-Frankfurt-am-Main.svg">

**Instructors:**
* [Prof. Dr. Alexander Mehler](https://www.texttechnologylab.org/team/alexander-mehler/), email: mehler@em.uni-frankfurt.de
* [Dr. Wahed Hemati](https://www.texttechnologylab.org/team/wahed-hemati/), email: hemati@em.uni-frankfurt.de

**Institutions:**
* **[Goethe University](http://www.informatik.uni-frankfurt.de/index.php/en/)**
* **[TTLab - Text Technology Lab](https://www.texttechnologylab.org/)**

**Project team:**
* Fabian Vogel
* Pascal Fischer

**Configuration**
Take a look here for the correct conifuration [recurrent neural network grammars](https://arxiv.org/abs/1602.07776/)

## Prediction
The model is able to predict the output in the usually format like in example_predict.txt. or in the .xml format like in example_XML.tei.

In following DATANAME is a free selectable name. 

There are to options to make a prediction:
* You have the ground truth of a text and you want to predict the rnng-output as .tei file as well as the evaluation. For this you have to save your ground_truth data as DATANAME_Ground_Truth.text.
* You only want to predict the rnng-output. For this you have to save your text in the file DATANAME.txt as plain text.

In both cases you have to save your files in the directory >/PLACE_YOUR_FILES_HERE

To make a prediciton (and get the evaluation results) you only have to navigate to the directory of the predict.sh file and execute 

    ./predict.sh DATEINAME 

The following files are generated in the /PLACE_YOUR_FILES_HERE directory

* DATEINAME_graminput.txt: The rnng input file 
* DATEINAME_predict.txt: The precition in grammar format.
* DATEINAME.tei: This is the final rnng out file which contains the prediction in .tei format.
* DATEINAME.txt: The purely input text without grammar format is saved here (if not available).
* DATEINAME_Ground_Truth.txt: This file only exists if, you saved a ground truth file here.
* DATEINAME_evaluation.txt: Here you can find the evaluation results (this file only exists if you have saved a ground truth file).
