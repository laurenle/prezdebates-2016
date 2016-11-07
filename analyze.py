import re, nltk, math

# List of text files to be analyzed
filenames = ['debate1.txt', 'debate2.txt', 'debate3.txt']

speech_segments = {'clinton': [], 'trump': []}

def mean(numbers):
  return float(sum(numbers)) / max(len(numbers), 1)

def variance(numbers):
  mu = mean(numbers)
  diff_from_mu = []
  for n in numbers:
    diff_from_mu.append((n - mu)**2)
  return mean(diff_from_mu)

def std_dev(numbers):
  return math.sqrt(variance(numbers))

# main loop. iteratively parse each file
for filename in filenames:
  f = open(filename, 'r')

  current_speaker = ''
  current_segment = ''

  # iteratively read each line in the transcript
  for line in f:
    speaker = re.match( r'[A-Z]+\:', line)
    if speaker:
      if current_speaker in speech_segments:
        speech_segments[current_speaker].append(current_segment)
      elif current_speaker != '':
        speech_segments[current_speaker] = [current_segment]
      current_speaker = speaker.group(0)[:-1].lower()
      current_segment = line.decode('utf-8').split(': ', 1)[1].strip()
    else:
      current_segment += line.decode('utf-8').strip()

  f.close()

for speaker in speech_segments:
  print "Parsed {0} segments for speaker {1}".format(len(speech_segments[speaker]), speaker)
  segment_lengths = []
  for segment in speech_segments[speaker]:
    tokens = nltk.word_tokenize(segment)
    segment_lengths.append(len(tokens))
  print "Speaker {0} averaged at {1} words per segment, with a min of {2}, a max of {3}, and a standard deviation of {4}".format(
    speaker, mean(segment_lengths), min(segment_lengths), max(segment_lengths), std_dev(segment_lengths))






