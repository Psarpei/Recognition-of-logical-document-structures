# Recognizing-logical-document-structures
Erkennung von logischen Dokumentstrukturen basierend auf recurrent neural network grammars. 
Paper: https://arxiv.org/abs/1602.07776

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


# Reconstruction of the Synagogue Höchst, Goethe University (Spring 2019)

## General Information
<img align="right" width="300" height="" src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Logo-Goethe-University-Frankfurt-am-Main.svg">;

**Instructors:**
* [Prof. Dr. Alexander Mehler](https://www.texttechnologylab.org/team/alexander-mehler/), email: mehler@em.uni-frankfurt.de
* [Giuseppe Abrami](https://www.texttechnologylab.org/team/giuseppe-abrami/), email: abrami@em.uni-frankfurt.de

**Institutions:**
* **[Goethe University](http://www.informatik.uni-frankfurt.de/index.php/en/)**
* **[TTLab - Text Technology Lab](https://www.texttechnologylab.org/)**

**Project team:**
* Mischa Dankert
* Andre Kerkhoff
* Alen Smajic

## Project Description ##
This project was developed as part of the CS course 'Ubiquitous Texttechnologies' in support of the Text Technology Lab at Goethe University Frankfurt. The goal of the project was to develop a virtual 3D reconstruction of the Synagogue Höchst, which was destroyed during the Novemberpogrome 1938. The model was then integrated into the [Stolperwege project](https://www.researchgate.net/publication/317070372_Stolperwege_-_An_App_for_a_Digital_Public_History_of_the_Holocaust), which aims to develop an app for realizing a digital public history of the Holocaust. For the realistic reconstruction we used the Blender tool which is an open-source 3D computer graphics software toolset used for creating animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality and computer games. As reference we used original construction plans and architectural recordings as well as an existing [3D model from Architectura Virtualis GmbH](http://www.architectura-virtualis.de/rekonstruktion/synagogehoechst.php?lang=de&img=v&file=0).

## Publications ##
* **[ResearchGate](https://www.researchgate.net/publication/344830141_Rekonstruktion_der_Synagoge_Hochst)**
* **[YouTube Video](https://www.youtube.com/watch?v=D5pH_EUDmik)**

## Tools ##
* Blender
* Unity

## Results ##
<img align="center" width="1000" height="" src="Images%20of%20our%20reconstruction/Exterior/Synagogue%20Höchst%20Comparison.png">

<img align="left" width="390" height="" src="Images%20of%20our%20reconstruction/Exterior/Exterior%202.png">
<img align="right" width="390" height="" src="Images%20of%20our%20reconstruction/Exterior/Exterior%204.png">

<img align="left" width="390" height="" src="Images%20of%20our%20reconstruction/Exterior/Exterior%205.png">
<img align="right" width="390" height="" src="Images%20of%20our%20reconstruction/Interior/Interior%201.png">

<img align="left" width="390" height="" src="Images%20of%20our%20reconstruction/Interior/Interior%202.png">
<img align="right" width="390" height="" src="Images%20of%20our%20reconstruction/Interior/Interior%203.png">
