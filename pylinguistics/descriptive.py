import nltk
import tools


#################################
#### DESCRIPTIVE METRICIS #######
########################## ######

def avg_word_per_sentence (pylinguistObj):
	x=0
	try:
		x= pylinguistObj.word_count / float(pylinguistObj.sentence_count)
	except:
		x=0
	pylinguistObj.avg_word_per_sentence = x
	return float(x)
            
def avg_syllables_per_word (pylinguistObj):
	x=0
	try:
		x=  float(pylinguistObj.syllable_count) / pylinguistObj.word_count
	except:
		x=0
	pylinguistObj.avg_syllables_per_word = x
	return x

def word_count (pylinguistObj):
	if (pylinguistObj.tokens == []):
		pylinguistObj.tokens = tools.getTokens(pylinguistObj.text)
	pylinguistObj.word_count = len(pylinguistObj.tokens)
	return len(pylinguistObj.tokens)

def sentence_count (pylinguistObj):
	x=0
	try:
		if (pylinguistObj.language == "pt-br"):
			nltk.sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
			tokenized_sentences = nltk.sent_tokenizer.tokenize(pylinguistObj.text)
		else:
			tokenized_sentences = nltk.sent_tokenize(pylinguistObj.text)

		x= len(tokenized_sentences)
	except ValueError:
		#print('error:' +ValueError)
		x=0
	pylinguistObj.sentence_count = x
	return x

	x=0
	return x

def syllable_count (pylinguistObj):
	x=0
	if (pylinguistObj.language == "pt-br"):
		#from source.syllable import silva2011
		#import source.syllable.silva2011
		from resources.syllable.silva2011 import syllable_separator
		count=0
		count_error=0
		for w in pylinguistObj.tokens:
			w_clean = tools.clear_string(w)
			if len(w_clean)>1:
				#result = 
				#print ('separando palavra:%s' %w_clean)
				try:
					leng = len(syllable_separator.separate(str(w_clean)))
					count+=leng
				except:
					count_error+=1
					#print ('ERROR ON WORD: %s' %w_clean)
			#print ('word:%s syllables:%s %i ' %(w, syllable_separator.separate(w),leng))
		pylinguistObj.syllable_count = count
		return count

	# try:

	# 	count = 0
	# 	vowels = 'aeiouy'
	# 	text = pylinguistObj.text.lower().strip(".:;?!)(")
	# 	if text is not None and text != "":
	# 		if text[0] in vowels:
	# 			count += 1
	# 		for index in range(1, len(text)):
	# 			if text[index] in vowels and text[index-1] not in vowels:
	# 				count += 1
	# 		if text.endswith('e'):
	# 			count -= 1
	# 		if text.endswith('le'):
	# 			count += 1
	# 		if count == 0:
	# 			count += 1
	# 		count = count - (0.1*count)
	# 	x= (round(count))
	# except:
	# 	x=0
	# pylinguistObj.syllable_count = x
	return x

