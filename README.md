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
Obtained by running `rhymes.test()` a few times in the ipython REPL. Very lightly massaged.

"you get it your own Smith's earful And this bar world's in sitting? Did is time warm (arm of a diseasoning  
Sweet do your bro, take sure you could wrong Even we needed they over, the strain the rooming of greasoning"

"JJ Uh, last you're dements off life I wonder than June Sounds, a neatly come drama... goes tryin together  
sicko Why young Rings slang (There's a man On a rubber's back in the stand you! We trife to get weather"

"seem the grab you Don't like for his Coogi in high volume will that rap over word from a good, reduced  
much of the nine, she was to Poetry he's truth was on Brooklyn Plus nobody wanna hand Tilling to roost"
