function getSongs() {
    songs = {}

    directories = [path.join(data_dir, d) for d in os.listdir(data_dir)]

    return {song: open(os.path.join(d, song)).read()
            for d in directories for song in os.listdir(d)}
}

function getUniqueWords(songs) {
}

function getRhymingPair(words) {
    function randomItem(arr) {
        return arr[Math.floor(Math.random()*items.length)];
    }

    var vocabWord = randomItem(words);
    rhymes = pronouncing.rhymes(vocab_word).filter(w => words.contains(w));

    if (!(rhymes && rhymes.length)) { // okay, everybody back to the lab, try again
        return getRhymingPair(words);
    }

    return [vocab_word, randomItem(rhymes)];
}
