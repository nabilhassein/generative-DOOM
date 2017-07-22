function getSongs() {
    // no way to say for each file in a directory from the browser?? :(

    var songs = [
        '?',
        'A Dead Mouse',
        'A.T.H.F',
        'Absolutely',
        'Accordion',
        'All Caps',
        'America\'s Most Blunted',
        'Angelz',
        'Anti-Matter',
        'Back End',
        'Back in the Days',
        'Bada Bing',
        'Ballskin',
        'Banished',
        'Basket Case',
        'Batty Boyz',
        'Beef Rapp',
        'Benzie Box',
        'Bistro',
        'Bite the Thong',
        'Bloody Chain',
        'Borin Convo',
        'Bout the Shoes',
        "Bumpy's Message",
        'Caskets',
        'Cellz',
        'Change the Beat',
        'Coming for You',
        'Crosshairs',
        'Curls',
        'Darkness (HBU)',
        'Dawg Friendly',
        'Dead Bent',
        'Deep Fried Frenz',
        'Disastrous',
        'Do Not Fire!',
        'Doom, Are You Awake?',
        'Doomsday',
        'Dope Skill',
        'Doper Skiller',
        'El Chupa Nibre',
        'Eye',
        'Fall Back Titty Fat',
        'Fancy Clown',
        'Fastlane',
        'Fazers',
        'Fig Leaf Bi-Carbonate',
        'Figaro',
        'Fillet-O-Rapper',
        'G.M.C.',
        'Gas Drawls',
        'Gazzillion Ear',
        'GMO',
        'Go with the Flow',
        'Great Day',
        'Great Things',
        'Guinnesses',
        'Gumbo',
        "Guv'nor",
        'Hardcore Hustle',
        'Hero vs. Villain (Epilogue)',
        'Hey!',
        'Hoe Cakes',
        'I Wonder',
        'Intro',
        'Kon Karne',
        'Kon Queso',
        'Kookies',
        'Krazy World',
        'Lactose and Lecithin',
        'Let Me Watch',
        'Lickupon',
        'Lightworks',
        'Lockjaw',
        'Mean the Most',
        'Meat Grinder',
        'Microwave Mayo',
        'Mince Meat',
        'Modern Day Mugging',
        'Money Folder',
        'Monster Zero',
        "More Rhymin'",
        'Mr. Clean',
        'Never Dead',
        'Next Levels',
        'No Names',
        'No Snakes Alive',
        'Ode to Road Rage',
        'Old School',
        'Om',
        'One Beer',
        'One Smart Nigger',
        'Open Mic Nite, Pt. 1',
        'Open Mic Nite, Pt. 2',
        'Operation Lifesaver a.k.a. Mint Test',
        'Operation: Greenbacks',
        'Overture',
        'Perfect Hair',
        'Poo-Putt Platter',
        'Pop Quiz (Bonus Extra Credit Remix)',
        'Pop Quiz (Remix)',
        'Popsnot',
        'Potholderz',
        'R.A.P. G.A.M.E.',
        'Raedawn',
        'Raid',
        'Rainbows',
        'Rap Ambush',
        'Rapp Snitch Knishes',
        'Red and Gold',
        'Retarded Fren',
        'Rhinestone Cowboy',
        'Rhymes Like Dimes',
        'Rhymin Slang',
        'Saliva',
        'Shadows of Tomorrow',
        'Sickfit',
        'Snatch That Dough (Skit)',
        'So Alone',
        'Sofa King',
        "Space Ho's",
        'Still Dope',
        'Still Kaps',
        'Strange Ways',
        'Supervillain Intro',
        'Supervillain Theme',
        'Supervillainz',
        'Thank Ya',
        "That's That",
        'The Drop',
        'The Final Hour',
        'The Fine Print',
        'The Finest',
        'The Hands of Doom',
        'The Illest Villains',
        'The Mask',
        'The Mic',
        'The Mystery of Doom (Skit)',
        'The Time We Faced Doom',
        'Tick, Tick',
        'Vats of Urine',
        'Vaudeville Villain',
        'Viberian Sun Pt. II',
        'Vomitspit',
        'Wash Your Hands',
        'Waterlogged (Skit)',
        'Who You Think I Am?',
        'Winter Blues',
        'Yessir!'
    ];

    var songObj = {};

    for (var i = 0; i < songs.length; i++) {
        var song = songs[i];
        $.ajax({
            async: false,
            url: 'data/' + song,
            dataType: 'text',
            success: function(data) {
                songObj[song] = data;
            },
        });
    }

    return songObj;
}

function getUniqueWords(songObj) {
    function onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }

    var allWords = Object.values(songObj).join(' ').split(/\s/);

    return allWords.filter(onlyUnique);
}

function getRhymingPair(words) {
    function randomItem(arr) {
        return arr[Math.floor(Math.random()*arr.length)];
    }

    var vocabWord = randomItem(words);
    var rhymes = pronouncing.rhymes(vocabWord).filter(function(w) {
        return words.indexOf(w) > -1;
    });

    if (!(rhymes && rhymes.length)) { // okay, everybody back to the lab, try again
        return getRhymingPair(words);
    }

    return [vocabWord, randomItem(rhymes)];
}
