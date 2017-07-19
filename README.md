# What is this?
This is an attempt to generate rhymes similar to those of my favorite MC
[DOOM](https://en.wikipedia.org/wiki/MF_Doom) (who has gone by many names).

# Why?
Basically, to learn about natural language processing, and for fun.
This is a project I worked on at the School for Poetic Computation,
as part of a two week intensive called [Code Narratives](http://sfpc.io/codenarratives/).

# How?
Basically, I start by generating rhyming pairs of words to serve as the end of a line,
and then generate "likely" preceding characters through a random (Markov) process.

Usually we think of Markov processes as generating the *next* item in a sequence, but
since (by definition) a Markov process has no memory, future and past are completely symmetrical.

So I start with the last word I want, use its reversed version as a seed to generate previous characters,
and then reverse it all at the end to make the line look like English.

For full details, see src/rhymes.py. It is very short.

I obtained the lyrics to train the model from [Genius](https://genius.com); see src/scrape.py.

It would be nice to try and use neural networks (probably an LSTM) to generate more meaningful rhymes.
Maybe I'll attempt that in the future.

# Related thoughts
DOOM does not generally pronounce words in the "General American" dialect
captured by the [Pronouncing library](https://pronouncing.readthedocs.io/en/latest/index.html)
that I'm using to generate rhymes, as it is based on the
[CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
funded by DARPA (i.e. the US military). Hence many rhymes that DOOM has made or
might make cannot be captured by this program as it currently exists.

This is indicative of larger biases in computing generally and NLP specifically
based on its history and funding sources. I have more thoughts about this.

Of course, the lack of flow, grammar, and meaning are all much
bigger problems with the generated rhymes. I'm still working on it.

# Sample rhymes
A few I liked, obtained by running `rhymes.test()` a few times in the ipython REPL.

"kid, you're goes the weed, gettin black, he wore jelly  
looking but was depicted they too hot smelly"

"goin y'all just know the shit come on the rain bubbles  
the people we canvas Instead off she doubles"

"to bag of science out 'em I knew, known That closely  
of the villain with the beatbox The gone and the mostly"
