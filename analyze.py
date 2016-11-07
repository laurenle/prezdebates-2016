import re, json, nltk
from nltk.corpus import treebank

# List of text files to be analyzed
filenames = ['debate1.txt', 'debate2.txt', 'debate3.txt']

speech_segments = {'clinton': [], 'trump': []}

num_black_mentions = 0

for filename in filenames:
  f = open(filename, 'r')

  current_speaker = ''
  current_segment = ''

  # iteratively read each line in the transcript
  for line in f:
    speaker = re.match( r'[A-Z]+\:', line)
    mentions_black = re.search( r'((A|a)frican( *)(-*)( *)(A|a)merican)|((B|b)lack)', line)
    mentions_latino = re.search( r'((L|l)atin(o|a))|((H|h)ispanic)', line)
    # if a speaker is introduced, update the current speaker accordingly
    if speaker:
      current_speaker = speaker.group(0)[:-1].lower()
      current_segment = line.decode('utf-8').split(': ', 1)[1].strip()
    else:
      current_segment = line.decode('utf-8').strip()
    # if african americans or latinos are mentioned, add speech segment for analysis
    if (mentions_black or mentions_latino) and current_speaker in speech_segments:
      speech_segments[current_speaker].append(current_segment)
    elif mentions_black or mentions_latino:
      speech_segments[current_speaker] = [current_segment]
  f.close()

for speaker in speech_segments:
  print "Parsed {0} lines for speaker '{1}'".format(len(speech_segments[speaker]), speaker)
  for segment in speech_segments[speaker]:
    print segment
    tokens = nltk.word_tokenize(segment)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    # print entities
