# Bilingual Audiobook Reader 

Alexa Skill that reads short sections from a book in German and English with the correct pronunciations and that has the following features:
* Remember the position you are
* Can be asked to repeat sentences again
* Handle multiple proficiency levels


# Machine Learning Pipeline

## Data Collection
We used The Trial (German: Der Prozess) by Franz Kafka which is a book from the public domain as an example.

## Data Preprocessing
After we splitted the original English translation into sentences 
We applied the following steps for both original and translated English sentences 
* Stopwords and punctuation are removed 
* Porter stemmer is used for stemming words

## Model & Matching Logic
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ra0k/alexa_skill_bilingual_audiobook/blob/main/bilingual_reader.ipynb)
* German sentences are translated to English using the FSMT (FairSeq MachineTranslation) model.
* Word2vec word embedding model is trained on English sentences using Gensim.
* The average feature vector is calculated for each sentence. 
* Cosine similarity is calculated to measure the similarity between sentences.
* Similarity calculations are performed within a window size of 3 to match the sequence of sentences on a one-to-one or many-to-one basis


# Deployment 
### Requirements
Python3, and SqlAlchemy compatibe database installed.

#### Dependencies
- flask_sqlalchemy
- flask
- flask_ask

#### Environment
The database URI is not hard-coded into the script. Before using, the URI needs to be saved to the corresponding environment variable. 

```audiobook_db=database_URI```

#### Secure connection
If the server doesn't have SSL connection or public IP, localtunnel or ngrok can be used as an alternative to set up a secure connecton with Alexa. Without a secure connection, Alexa won't communicate with the skill. 

#### Start server

```python3 audiobook.py```

# Code

##### data/
Raw and generated bilingual books in text format

##### models/
Data objects and their interface. User states are stored in the database, while books are loaded into the memory. 

##### audiobook.py
Main logic and intents. 

##### func.py
Implementation of the features, database operations, output generation. 

##### templates.yaml
Contains the rendering logic of the answers, questions and other texts.

##### intents.json
Configuration of the intents. 


# Alexa-Interface & Examples

## Sample from the matched file:

**German:**
Nein , warum denn ?
**English:**
No, why should you think that?

**German:**
Sie sind nur verhaftet , nichts weiter .
**English:**
You're simply under arrest, nothing more than that.

**German:**
Das hatte ich Ihnen mitzuteilen , habe es getan und habe auch gesehen , wie Sie es aufgenommen haben .
**English:**
That's what I had to tell you, that's what I've done and now I've seen how you've taken it.


## Extraction from an Alexa conversation 

![conversation extracted from Alexa](alexa_screenshot.png?raw=true "Conversation extracted from Alexa")
