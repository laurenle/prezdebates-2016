74# prezdebates-2016
Comparative speech analysis for candidates Hillary Rodham Clinton and Donald J. Trump using data drawn from the 2016 presidential debates.

## Installation

Before running analyze.py, you will need to install the nltk module:

    $ sudo pip install -U nltk

Once this is complete, you can run the script using:

    $ python analyze.py

For some reason, you may need to download additional nltk modules using the built-in installer. To do so, the following two commands on terminal:

    $ python
    >>> import nltk
    >>> nltk.download()

A NLTK Downloader GUI will open. From here, select "All packages" and click the Download button.

## Results

Running the analyzer will return the following results:

    Parsed 75 segments for speaker cooper
    Speaker cooper averaged at 16.5466666667 words per segment, with a min of 2, a max of 136, and a standard deviation of 23.7600748222

    Parsed 342 segments for speaker trump
    Speaker trump averaged at 74.014619883 words per segment, with a min of 2, a max of 568, and a standard deviation of 120.21808797

    Parsed 123 segments for speaker wallace
    Speaker wallace averaged at 28.4959349593 words per segment, with a min of 1, a max of 338, and a standard deviation of 48.2089581096

    Parsed 96 segments for speaker holt
    Speaker holt averaged at 21.7395833333 words per segment, with a min of 2, a max of 231, and a standard deviation of 36.8115258195

    Parsed 8 segments for speaker question
    Speaker question averaged at 39.0 words per segment, with a min of 22, a max of 58, and a standard deviation of 13.1339255366

    Parsed 226 segments for speaker clinton
    Speaker clinton averaged at 95.0 words per segment, with a min of 1, a max of 472, and a standard deviation of 122.647924052
    
    Parsed 60 segments for speaker raddatz
    Speaker raddatz averaged at 23.2 words per segment, with a min of 2, a max of 181, and a standard deviation of 35.2026514153