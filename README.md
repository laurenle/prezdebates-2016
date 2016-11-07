# prezdebates-2016
Comparative speech analysis for candidates Hillary Rodham Clinton and Donald J. Trump using data drawn from the 2016 presidential debates.

## Installation

Before running analyze.py, you will need to install the nltk module:

    $ sudo pip install -U nltk
    $ sudo pip install -U numpy

Once this is complete, you can run the script using:

    $ python analyze.py

For some reason, you may need to download additional nltk modules using the built-in installer. To do so, the following two commands on terminal:

    $ python
    >>> import nltk
    >>> nltk.download()

A NLTK Downloader GUI will open. From here, select "All packages" and click the Download button.

## Notes

- Data for Middle-Eastern Americans, Asian Americans, and Native Americans was not included because these groups were not mentioned by either candidate.
- Data for 'Mexicans' was not included in the search for Latinos/Hispanics, because whether this referred to Mexican-Americans or Mexican citizens was ambiguous.