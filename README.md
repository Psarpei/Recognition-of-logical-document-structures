# Recognizing-logical-document-structures
Rocognition of logical document structures based on recurrent neural network grammars(https://arxiv.org/abs/1602.07776/). 
This work is the preliminary work of the paper Recognizing Sentence-level Logical Document Structures with the Help of
Context-free Grammars(https://arxiv.org/abs/1602.07776) 

## General Information
<img align="right" width="300" height="" src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Logo-Goethe-University-Frankfurt-am-Main.svg">;

**Instructors:**
* [Prof. Dr. Alexander Mehler](https://www.texttechnologylab.org/team/alexander-mehler/), email: mehler@em.uni-frankfurt.de
* [Dr. Wahed Hemati](https://www.texttechnologylab.org/team/wahed-hemati/), email: hemati@em.uni-frankfurt.de

# Konfiguration
Für Vorraussetzungen sowie die Konfigurierung schauen sie bitte hier: https://github.com/clab/rnng

# Vorhersagen
Das Modell kann die Ausgabe im gewöhnlichen rnng Ausgabe Format wie in example_predict.txt, oder in einem XML-Format wie in example_XML.tei generieren.

# Anleitung
DATEINAME ist ein frei wählbarer Name. Um eine Vorhersage treﬀen zu lassen, gibt es zwei Möglichkeiten:

* Man hat die Ground Truth eines Textes zur Verfügungund möchte sowohl die Vorhersage als .tei Datei bekommen, als auch die Evaluation dazu. Dafürmuss man die Ground Truth in der Datei ”DATEINAME_Ground_Truth.txt” gespeichert haben. 
* Man möchte einfach nur die Vorhersage eines Textes sehen. Dafür muss der Text in der Datei ”
DATEINAME.txt gespeichert sein.

In beiden Fällen müssen die Dateien im Verzeichnis /PLACE_YOUR_FILES_HERE gespeichert werden. 

Um nun Vorhersagen zu treﬀen (und Evaluationsergebnisse zu erlangen), muss man lediglich mit der Konsole in den selben Dateipfad wie die predict.sh navigieren und den Befehl:

    ./predict.sh DATEINAME 

ausführen. Dabei werden folgende Dateien im Ordner /PLACE_YOUR_FILES_HERE erzeugt:

* DATEINAME_graminput.txt: Diese Datei wird in das RNNG eingegeben. 
* DATEINAME_predict.txt: Hier ist die Vorhersage im Grammatikformat enthalten.
* DATEINAME.tei: Diese Datei ist die ﬁnale Ausgabe, die den vorhergesagten Text im .tei-Format enthält.
* DATEINAME.txt: Hier wird (falls noch nicht vorhanden) der reine Eingabetext ohne Grammatikformat gespeichert.
* DATEINAME_Ground_Truth.txt: Diese Datei existiert nur, wenn man eine Ground Truth zur Verfügung und hier abgespeichert hat.
* DATEINAME_evaluation.txt: Hier ﬁndet man die Evaluationsergebnisse (existiert nur, falls DATEINAME_Ground_Truth.txt existiert).

# Danksagung
Herzlichsten Dank an Fabian Vogel für tolle Mitarbeit an diesem Projekt.
