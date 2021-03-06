import re, nltk, math
from nltk.corpus import treebank

# List of text files to be analyzed
filenames = ['debate1.txt', 'debate2.txt', 'debate3.txt']

speech_segments = {'clinton': [], 'trump': []}

def mean(numbers):
  return float(sum(numbers)) / len(numbers)

def variance(numbers):
  mu = mean(numbers)
  diff_from_mu = []
  for n in numbers:
    diff_from_mu.append((n - mu)**2)
  return mean(diff_from_mu)

def std_dev(numbers):
  return math.sqrt(variance(numbers))

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# main loop. iteratively parse each file
for filename in filenames:
  f = open(filename, 'r')

  current_speaker = ''
  current_segment = ''

  # iteratively read each line in the transcript
  for line in f:
    speaker = re.match( r'[A-Z]+\:', line)
    if speaker:
      current_speaker = speaker.group(0)[:-1].lower()
      current_segment = line.decode('utf-8').split(': ', 1)[1].strip()
    else:
      current_segment += line.decode('utf-8').strip()
    sentences = tokenizer.tokenize(current_segment)

    for sentence in sentences:
      if current_speaker in speech_segments:
        speech_segments[current_speaker].append(sentence)
      else:
        speech_segments[current_speaker] = [sentence]
  f.close()

for speaker in speech_segments:
  print "Parsed {0} sentences for speaker {1}".format(len(speech_segments[speaker]), speaker)
  segment_lengths = []
  for segment in speech_segments[speaker]:
    tokens = nltk.word_tokenize(segment)
    segment_lengths.append(len(tokens))
  print "Speaker {0} averaged at {1} words per sentence, with a min of {2}, a max of {3}, and a standard deviation of {4}\n".format(
    speaker, mean(segment_lengths), min(segment_lengths), max(segment_lengths), std_dev(segment_lengths))






