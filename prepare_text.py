# Functions used in the file are based on Kaggle sample code found at
# https://github.com/wendykan/DeepLearningMovies
# This file prepares movie reviews for input by loading data from the tsv and performing 
# tranformation functions

import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
import pickle
# nltk.download()

# Load punkt tokenizer
TOKENIZER = nltk.data.load('tokenizers/punkt/english.pickle')
#TOKENIZER = nltk.data.load('/home/ubuntu/nltk_data/tokenizers/punkt/english.pickle')

# lists used across files
review_list = []
test_review_list = []

def extract_data_from_tsv():
	# fetch the reviews from the tsv file, both labeled and unlabeled
	labeled_training_data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3) # 25,000 reviews
	unlabeled_training_data = pd.read_csv("unlabeledTrainData.tsv", header=0, delimiter="\t", quoting=3) # 50,000 reviews
	test_data = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3) # 25, 000 reviews 
	
	print "LABELED: ", labeled_training_data['review'].size()
	print "UNLABELED: ", unlabeled_training_data['review'].size()
	print "TEST: ", test_data['review'].size()


class MovieReview(object):
	def __init__(self, mreview):
		self.mreview = mreview
		self.mreview_clean = None
		self.mreview_word_list = []
		self.mreview_sentence_list = []

	def clean_review(self):
		# function to clean the review by stripping html from review text body
		self.mreview_clean = BeautifulSoup(self.mreview).get_text()

	def remove_punctuation_and_nums(self):
		self.mreview_clean = re.sub("[^a-zA-Z]", " ", self.mreview_clean)

	def split_review_into_words(self):
		# function to split the review text to list of words
	    self.mreview_word_list = self.mreview_clean.lower().split()

	def remove_stop_words(self):
		self.mreview_word_list = [word for word in self.mreview_word_list if not word in set(stopwords.words("english"))]
		self.mreview_clean = " ".join(self.mreview_word_list)

	def split_review_into_sentences(self):
		# function to split review into list of sentences
		# where each setence is a list of words
		extracted_sentences = TOKENIZER.tokenize(self.mreview_clean.strip())
		for extracted_sentence in extracted_sentences:
			if len(extracted_sentence) > 0:
				# extracted_sentence needs to be operated on if stopword or punctuation
				# removal is required eventually(not required for word2Vec)
				self.mreview_sentence_list.append(extracted_sentence.lower().split())

def main():
	global review_list
	global test_list
	labeled_training_data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3) # 25,000 reviews
	# unlabeled_training_data = pd.read_csv("unlabeledTrainData.tsv", header=0, delimiter="\t", quoting=3) # 50,000 reviews
	test_data = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3) # 25, 000 reviews 
	
	# print "LABELED: ", labeled_training_data['review'].size()
	# print "UNLABELED: ", unlabeled_training_data['review'].size()
	# print "TEST: ", test_data['review'].size()

	for mreview in labeled_training_data["review"]:
		mreview_obj = MovieReview(mreview)
		mreview_obj.clean_review()
		mreview_obj.remove_punctuation_and_nums()
		mreview_obj.split_review_into_words()
		mreview_obj.remove_stop_words()
		review_list.append(mreview_obj.mreview_clean)

	for mreview in test_data["review"]:
		mreview_obj = MovieReview(mreview)
		mreview_obj.clean_review()
		mreview_obj.remove_punctuation_and_nums()
		mreview_obj.split_review_into_words()
		mreview_obj.remove_stop_words()
		test_review_list.append(mreview_obj.mreview_clean)

	print "Finished"
	print "Pickle a list??"
	print "Pickle"
	with open("review_file_pickle.txt", 'wb') as fp1:
		pickle.dump(review_list, fp1)

	with open("test_review_file_pickle.txt", 'wb') as fp2:
		pickle.dump(test_review_list, fp2)

	print "Write to a .py file"
	with open('review_file.py', 'w') as f1:
		f1.write('review_list = %s' % review_list)

	with open('test_review_file.py', 'w') as f2:
		f2.write('test_review_list = %s' % test_review_list)

if __name__ == '__main__':
	main()


	
