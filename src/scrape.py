from bs4 import BeautifulSoup
import requests
import re
import os


def fetch(artist, song):
    """Given an artist and a song name, fetch the lyrics from genius and
    return them as a list of strings, with each lyric on its own line.
    """

    regex = re.compile('[^a-zA-Z-]')

    # hyphens for spaces; other non alphabetical characters removed
    artist = regex.sub('', artist.replace(' ', '-'))
    song = regex.sub('', song.replace(' ', '-'))

    slug = 'https://genius.com/%s-%s-lyrics' % (artist, song)
    page = requests.get(slug)

    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]

    lyrics = html.find('div', class_='lyrics').get_text().split('\n')
    # strip empty lines, [Verse: MF DOOM], etc.
    lyrics = [line for line in lyrics if line and line[0] != '[']

    return lyrics


# case insensitive, and deliberately missing punctuation not present in genius slugs
# obtained from wikipedia, with alterations to match genius slugs
artist_to_album_to_songs = {
    'MF DOOM': {
        'operation doomsday': [
            "The Time We Faced Doom",
            "Doomsday",
            "Rhymes Like Dimes",
            "The Finest",
            "Back in the Days ",
            "Go with the Flow",
            "Tick, Tick…",
            "Red and Gold",
            "The Hands of Doom ",
            "Who You Think I Am?",
            "Doom, Are You Awake?",
            "Hey!",
            "Operation: Greenbacks",
            "The Mic",
            "The Mystery of Doom (Skit)",
            "Dead Bent",
            "Gas Drawls",
            "?",
            "Hero vs. Villain (Epilogue)",
        ],
        'mm food': [
        ],
    },
    'King Geedorah': {
        'take me to your leader': [
        ],
    },
    'Viktor Vaughn': {
        'vaudeville villain': [
        ],
        'venomous villain':[
        ],
    },
    'Madvillain': {
        'madvillainy': [
        ],
    },
    'DangerDOOM': {
        'the mouse and the mask': [
        ],
    },
    'DOOM': {
        'born like this': [
        ],
    },
    'JJ DOOM': {
        'key to the kuffs': [
        ],
    },
    'Nehruvian DOOM': {
        'nehruhviandoom': [
        ],
    },
}


if __name__ == '__main__':
    for artist in artist_to_album_to_songs:
        for album in artist_to_album_to_songs[artist]:
            directory = os.path.abspath('../data/%s' % album)
            if not os.path.exists(directory):
                os.makedirs(directory)

            for song in artist_to_album_to_songs[artist][album]:
                lyrics = fetch(artist, song)
                filename = os.path.join(folder, song)
                with open(filename, 'w') as f:
                    f.write('\n'.join(lyrics))
