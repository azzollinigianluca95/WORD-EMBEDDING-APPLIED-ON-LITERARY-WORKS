**WORD EMBEDDING APPLIED ON LITERARY WORKS** <br/> 
Given a word, detecting all other words having similar meaning in a given literary work, using Word2Vec algorithm and Apache Spark enviroment. 

The analyzer takes in input literary works as text files, grouped by their literary period and applies preprocessing removing useless spaces and step-words. </br>
Then, given a word in input, it finds other words with similar meaning for each literary period. </br>
There's no limit of works which can be loaded for each period.

In output the best results for each period are shown, making possible to compare how the same word can change its meaning during different literary periods.

The system was implemented on a simulated distributed system using Apache Spark. </br>
The similarity word search is implemented using the word embedding technique known as 'word vector'. </br>
Then a 'Word2Vec' algorithm with a 'SkipGram' model computes the similarity factors. </br>
At the end, words are sorted respect to their similarity factor.

The exploited model is included in the Mlib library of the Apache Spark framework.

**If you publish any work which uses the code stored in this project, please cite the following creators:** <br/>
Sergio Abascià, Gianluca Azzollini, Alberto Carlo  Maria Mancino

**Developers** <br/>
Sergio Abascià  <br/>
Gianluca Azzollini <br/>
Alberto Carlo Maria Mancino <br/>

**Contacts** <br/>
We are happy to help you with any question. Please contact us on our mails: <br/>
sergio05.abascia@gmail.com <br/>
azzollinigianluca@gmail.com <br/>
alberto.mancino94@gmail.com <br/>
<br/>


<img src="https://github.com/azzollinigianluca95/Word-Embedding-applied-on-literary-works/blob/master/screenshot1.png" width="348">

<img src="https://github.com/azzollinigianluca95/Word-Embedding-applied-on-literary-works/blob/master/screenshot2.png" width="348">
