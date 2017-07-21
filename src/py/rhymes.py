from collections import defaultdict, Counter
import os
import pronouncing
import random
from sklearn.feature_extraction.text import CountVectorizer
from spacy.en.language_data import STOP_WORDS


def get_songs(data_dir=None):
    data_dir = data_dir or os.path.abspath('../../data')
    directories = [os.path.join(data_dir, d) for d in os.listdir(data_dir)]

    return {song: open(os.path.join(d, song)).read()
            for d in directories for song in os.listdir(d)}


def get_unique_words(song_dict):
    vectorizer = CountVectorizer()

    filtered_songs = list(w for w in song_dict.values() if w not in STOP_WORDS)

    vectorizer.fit_transform(filtered_songs)
    return vectorizer.get_feature_names()


def get_rhyming_pair(words):
    vocab_word = random.choice(words)
    rhymes = [w for w in pronouncing.rhymes(vocab_word) if w in words]

    if not rhymes: # okay, everybody back to the lab, try again
        return get_rhyming_pair(words)

    return vocab_word, random.choice(rhymes)


def train_reverse_char_model(data, order=5):
    pad = "~" * order
    data = (pad + data)[::-1]

    model = defaultdict(Counter)
    for i in range(len(data) - order):
        future, char = data[i:i+order], data[i+order]
        model[future][char] += 1

    def normalize(counter):
        s = float(sum(counter.values()))
        return [(w, count/s) for w, count in counter.items()]

    return {future:normalize(chars) for future, chars in model.items()}


def generate_previous_char(model, future, order):
    future = future[-order:]
    dist = model[future]
    x = random.random()

    for c, v in dist:
        x = x - v
        if x <= 0: return c


def generate_forward_text(model, order, seed=None, nletters=50):
    seed = seed[::-1]
    future = seed or ("~" * order)
    out = [c for c in seed]
    for _ in range(nletters):
        c = generate_previous_char(model, future, order)
        future = future[-order:] + c
        out.append(c)

    return "".join(out)[::-1]


def test(model=None, order=5):
    song_dict = get_songs()
    all_songs = '\n'.join(song_dict.values())
    unique_words = get_unique_words(song_dict)
    word1, word2 = get_rhyming_pair(unique_words)
    
    model = model or train_reverse_char_model(all_songs, order)

    def drop_until_full_word(s):
        return s.split(' ', 1)[1].replace('\n', ' ')

    try:
        lines = [drop_until_full_word(generate_forward_text(model, order, word))
                 for word in (word1, word2)]
    except KeyError:
        return test()

    return '\n'.join(lines)
