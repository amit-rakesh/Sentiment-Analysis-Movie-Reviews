import os
import argparse
from prepare_text import MovieReview
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

# currently using the best model so far - BOW and Random Forest
def calculate_sentiment(review_string):
	os.chdir('/home/ubuntu/Src')
	bow_model = joblib.load('bow_model.pkl')
	rf_model  = joblib.load('rf_bow_model.pkl')

	single_sample_review_list = []
	mreview_obj = MovieReview(review_string)
	mreview_obj.clean_review()
	mreview_obj.remove_punctuation_and_nums()
	mreview_obj.split_review_into_words()
	mreview_obj.remove_stop_words()
	single_sample_review_list.append(mreview_obj.mreview_clean)

	query_features = bow_model.transform(single_sample_review_list)
	query_features = query_features.toarray()

	# use the trained forest to make predictions
	prediction = rf_model.predict(query_features)
	#print "Result: " , prediction[0]
	return prediction[0]

def calculate_sentiment_1(review_string):
	#return str(os.getcwd())

	os.chdir('/home/ubuntu/Src')
        bow_model = joblib.load('bow_model.pkl')
        rf_model  = joblib.load('rf_bow_model.pkl')

        single_sample_review_list = []
        mreview_obj = MovieReview(review_string)
        mreview_obj.clean_review()
        mreview_obj.remove_punctuation_and_nums()
        mreview_obj.split_review_into_words()
        mreview_obj.remove_stop_words()
        single_sample_review_list.append(mreview_obj.mreview_clean)

        query_features = bow_model.transform(single_sample_review_list)
        query_features = query_features.toarray()

	return str(os.getcwd())

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--review", type=str, required=True)
	args = parser.parse_args()
	calculate_sentiment(args.review)
	# return calculate_sentiment()
