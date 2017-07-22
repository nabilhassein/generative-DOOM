function getUniqueWords() {
    var words = [];

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

function getModel() {
    var model = {};

    $.ajax({
        async: false,
        url: 'data/model.json',
        dataType: 'json',
        success: function(data) {
            model = data;
        },
    });

    return model;
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


function generateChar(model, future, order) {
    future = future.slice(future.length - order);
    var dist = model[future];
    var x = Math.random();

    for (var i = 0; i < dist.length; i++) {
        c = dist[i][0];
        v = dist[i][1];
        x = x - v;
        if(x <= 0) { return c; }
    }
}


function generateText(model, order, seed, nletters) {
    function reverse(s) {
        return s.split('').reverse().join('');
    }

    seed = reverse(seed);
    var future = seed || Array(order).join('~');
    var out = seed.split('');
    for (var i = 0; i < nletters; i++) {
        var c = generateChar(model, future, order);
        future = future.slice(future.length - order) + c;
        out.push(c);
    }

    return reverse(out.join(''));
}


function main() {
    function dropUntilFullWord(s) {
        return s.substr(s.indexOf(' ') + 1);
    }

    try {
        var order = 5;
        var nletters = 50;

        var rhymingPair = getRhymingPair(words);
        var word1 = rhymingPair[0];
        var word2 = rhymingPair[1];

        var line1 = dropUntilFullWord(generateText(model, order, word1, nletters));
        var line2 = dropUntilFullWord(generateText(model, order, word2, nletters));
    }
    catch(e) {
        return main();
    }

    return [line1, line2];
}
