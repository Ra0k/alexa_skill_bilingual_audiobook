default_book = 'The Trial'

def _get_book(name=default_book):
    
    if name == 'Harry Potter and the Philosopher\'s Stone':
        filename = 'hp1_de_en_cleaned_translated.txt'
    elif name == 'The Trial':
        filename = 'de_en_matched_Kafka_Franz_Prozess.txt'

    file = open(f'data/{filename}', 'r')

    data = []
    lines = file.readlines()
    for line in lines:
        items = line.split('|')
        data.append({
            'de': items[1],
            'en': items[2]
        })
    return data

def get_book_titles():
    return books.keys()

def get_book(title=default_book):
    return books[title]

def get_sentences(title=default_book):
    return books[title]['sentences']

books = {
    'Harry Potter and the Philosopher\'s Stone': {
        'sentences': [], #_get_book('Harry Potter and the Philosopher\'s Stone'),
        'source': 'de',
        'translations': ['en']
    },
    'The Trial': {
        'sentences': _get_book('The Trial'),
        'source': 'de',
        'translations': ['en']
    }
}

