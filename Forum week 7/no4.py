import re

def sentence_splitter(file_name):
	with open(file_name, 'r') as f:
		file_content = f.read()

	sentences = re.sub(r'\s+', ' ', file_content) 

	sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

 	sentences = re.sub(r'\!', '\n', sentences)

 	sentences = re.sub(r'\?\s', '?\S', sentences)

	print (sentences)

sentence_splitter("Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.")