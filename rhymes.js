var songs = [
    
]

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
