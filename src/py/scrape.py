from bs4 import BeautifulSoup
import requests
import re
import os


def fetch(artist, song):
    """Given an artist and a song name, fetch the lyrics from genius and
    return them as a list of strings, with each lyric on its own line.
    """

    regex = re.compile('[^0-9a-zA-Z-]')

    # hyphens for spaces; other non alphabetical characters removed
    artist = regex.sub('', artist.replace(' ', '-')).strip()
    song = regex.sub('', song.replace(' ', '-')).strip()

    slug = 'https://genius.com/%s-%s-lyrics' % (artist, song)
    page = requests.get(slug)

    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]

    try:
        lyrics = html.find('div', class_='lyrics').get_text().split('\n')
    except Exception as e:
        print('failed on %s, %s' % (artist, song))
        raise e
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
            "Back in the Days",
            "Go with the Flow",
            "Tick, Tick…",
            "Red and Gold",
            "The Hands of Doom",
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
            "Beef Rapp",
            "Hoe Cakes",
            "Potholderz",
            "One Beer",
            "Deep Fried Frenz",
            "Poo-Putt Platter",
            "Fillet-O-Rapper",
            "Gumbo",
            "Fig Leaf Bi-Carbonate",
            "Kon Karne",
            "Guinnesses",
            "Kon Queso",
            "Rapp Snitch Knishes",
            "Vomitspit",
            "Kookies"
        ],
        'born like this': [
            "Supervillain Intro",
            "Gazzillion Ear",
            "Ballskin",
            "Yessir!",
            "Absolutely",
            "Rap Ambush",
            "Lightworks",
            "Batty Boyz",
            "Angelz",
            "Cellz",
            "Still Dope",
            "Microwave Mayo",
            "More Rhymin'",
            "That's That",
            "Supervillainz",
            "Bumpy's Message",
            "Thank Ya",
        ],
    },
    'King Geedorah': {
        'take me to your leader': [
            "Fazers",
            "Fastlane",
            "Krazy World",
            "The Final Hour",
            "Monster Zero",
            "Next Levels",
            "No Snakes Alive",
            "Anti-Matter",
            "Lockjaw",
            "I Wonder",
            "One Smart Nigger",
            "The Fine Print"
        ],
    },
    'Viktor Vaughn': {
        'vaudeville villain': [
            "Overture",
            "Vaudeville Villain",
            "Lickupon",
            "The Drop",
            "Lactose and Lecithin",
            "A Dead Mouse",
            "Open Mic Nite, Pt. 1",
            "Raedawn",
            "Let Me Watch",
            "Saliva",
            "Modern Day Mugging",
            "Open Mic Nite, Pt. 2",
            "Never Dead",
            "Popsnot",
            "Mr. Clean",
            "G.M.C.",
            "Change the Beat",
        ],
        'venomous villain':[
            "Back End",
            "Fall Back Titty Fat",
            "R.A.P. G.A.M.E.",
            "Dope Skill",
            "Doper Skiller",
            "Ode to Road Rage",
            "Bloody Chain",
            "Pop Quiz (Remix)",
            "Pop Quiz (Bonus Extra Credit Remix)",
        ],
    },
    'Madvillain': {
        'madvillainy': [
            "The Illest Villains",
            "Accordion",
            "Meat Grinder",
            "Bistro",
            "Raid",
            "America’s Most Blunted",
            "Sickfit",
            "Rainbows",
            "Curls",
            "Do Not Fire!",
            "Money Folder",
            "Shadows of Tomorrow",
            "Operation Lifesaver a.k.a. Mint Test",
            "Figaro",
            "Hardcore Hustle",
            "Strange Ways",
            "Fancy Clown",
            "Eye",
            "Supervillain Theme",
            "All Caps",
            "Great Day",
            "Rhinestone Cowboy",
        ],
    },
    'DangerDOOM': {
        'the mouse and the mask': [
            "El Chupa Nibre",
            "Sofa King",
            "The Mask",
            "Perfect Hair",
            "Benzie Box",
            "Old School",
            "A.T.H.F",
            "Basket Case",
            "No Names",
            "Crosshairs",
            "Mince Meat",
            "Vats of Urine",
            "Space Ho's",
            "Bada Bing",
        ],
    },
    'JJ DOOM': {
        'key to the kuffs': [
            "Waterlogged (Skit)",
            "Guv'nor",
            "Banished",
            "Bite the Thong",
            "Rhymin Slang",
            "Dawg Friendly",
            "Borin Convo",
            "Snatch That Dough (Skit)",
            "GMO",
            "Bout the Shoes",
            "Winter Blues",
            "Still Kaps",
            "Retarded Fren",
            "Viberian Sun Pt. II",
            "Wash Your Hands",
        ],
    },
    'NehruvianDOOM': {
        'nehruviandoom': [
            "Intro",
            "Om",
            "Mean the Most",
            "So Alone",
            "Coming for You",
            "Darkness (HBU)",
            "Caskets",
            "Great Things",
            "Disastrous"
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
                filename = os.path.join(directory, song)
                if not os.path.exists(filename):
                    with open(filename, 'w') as f:
                        f.write('\n'.join(lyrics))
