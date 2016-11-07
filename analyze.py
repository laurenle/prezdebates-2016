import re

# List of text files to be analyzed
filenames = ['debate1.txt', 'debate2.txt', 'debate3.txt']

speech_segments = {'clinton': [], 'trump': []}

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
      current_segment = line.split(': ', 1)[1].strip()
    else:
      current_segment += line.strip()

  f.close()

for speaker in speech_segments:
  print "Parsed {0} lines for speaker {1}".format(len(speech_segments[speaker]), speaker)