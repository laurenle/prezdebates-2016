import re, nltk
from nltk.corpus import treebank

# List of text files to be analyzed
filenames = ['debate1.txt', 'debate2.txt', 'debate3.txt']

minority_mention_count = {}

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

for filename in filenames:
  f = open(filename, 'r')

  current_speaker = ''
  current_segment = ''

  # iteratively read each line in the transcript
  for line in f:
    speaker = re.match( r'[A-Z]+\:', line)
    # if a speaker is introduced, update the current speaker accordingly
    if speaker:
      current_speaker = speaker.group(0)[:-1].lower()
      current_segment = line.decode('utf-8').split(': ', 1)[1].strip()
    else:
      current_segment = line.decode('utf-8').strip()
    if current_speaker not in minority_mention_count:
      minority_mention_count[current_speaker] = {'black': 0, 'hispanic': 0, 'latino': 0, 'african-american': 0}
    sentences = tokenizer.tokenize(current_segment)

    for sentence in sentences:
      if re.search( r'(B|b)lack', sentence):
        minority_mention_count[current_speaker]['black'] += 1
      if re.search( r'(A|a)frican( *)(-*)( *)(A|a)merican', sentence):
        minority_mention_count[current_speaker]['african-american'] += 1
      if re.search( r'(L|l)atin(o|a)', sentence):
        minority_mention_count[current_speaker]['latino'] += 1
      if re.search( r'(H|h)ispanic', sentence):
        minority_mention_count[current_speaker]['hispanic'] += 1
  f.close()

for speaker in minority_mention_count:
  print "-----------------------------------------"
  for minority in minority_mention_count[speaker]:
    print "Speaker {0} used term {1} {2} times".format(speaker, minority, minority_mention_count[speaker][minority])
