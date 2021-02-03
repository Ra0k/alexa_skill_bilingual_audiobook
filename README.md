# alexa_skill_bilingual_audiobook

# Bilingual Audiobook Reader 

Alexa Skill that reads short sections from a book in German and English with the correct pronunciations and that has the following features:
* Remember the position you are
* Can be asked to repeat sentences again
* Handle multiple proficiency levels


# Data
We used The Trial (German: Der Prozess) by Franz Kafka which is a book from the public domain as an example.


# Data Preprocessing
After we splitted the original English translation into sentences 
We applied the following steps for both original and translated English sentences 
* Stopwords and punctuation are removed 
* Porter stemmer is used for stemming words

# Model & Method
* German sentences are translated to English using the FSMT (FairSeq MachineTranslation) model.
* Word2vec word embedding model is trained on English sentences using Gensim.
* The average feature vector is calculated for each sentence. 
* Cosine similarity is calculated to measure the similarity between sentences.
* Similarity calculations are performed within a window size of 3 to match the sequence of sentences on a one-to-one or many-to-one basis


# Deployment 


# Alexa-Interface & Examples

3-5. sentences from the book (contain both one-to-one and many-to-one match )
maybe an example from the other book 
video or audio (?)
