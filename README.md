All Downloaded Python Libraries used:
wordcloud
spacy
pysynth
matplotlib

using our learning model to generate songs in the text style from Taylor Swift (other singers' style also could generate).
First, we use obtaining a random number and generate different templates based on the random number, so our project can generate lyrics in ACBC, ABCB, ABCC patterns.
Second,  we use desiredlength to judge whether the sentence is too long. When the sentence is too long, cut it, and sew the sentence in smaller parts and put them in a new sentence. 
Third, we use SpaCy to write a rule saying that the last word of a generated sentence cannot be a conjunction, adjective.
In Showmanship, we we graph the songs in different picture. (Notice: When you running our program,you need to reset the directory of picture in line 154, on generate.py, and you also can choose the different picture to generate wordcloud if you want. )
