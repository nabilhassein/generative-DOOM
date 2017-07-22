function getUniqueWords() {
    words = []

    $.ajax({
        async: false,
        url: 'data/words.json',
        dataType: 'json',
        success: function(data) {
            words = data;
        },
    });

    return words;
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
