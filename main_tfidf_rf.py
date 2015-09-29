from prepare_text import MovieReview
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from review_file import review_list
from test_review_file import test_review_list

def main():
	# extract reviews from tsv files
	labeled_training_data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3) # 25,000 reviews
	test_data = pd.read_csv("testData.tsv", header=0, delimiter="\t", quoting=3) # 25, 000 reviews

	print "Creating TF-IDF Vectors...."" "		
	vectorizer = TfidfVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000) 
	trained_data_features  = vectorizer.fit_transform(review_list)
	trained_data_features = trained_data_features.toarray() # convert to numpy array for faster processing


	print "Supervised Learning - Random Forest"
	forest = RandomForestClassifier(n_estimators = 100) # 100 trees
	forest = forest.fit(trained_data_features, labeled_training_data["sentiment"]) # using BOW as feaures and the given labels as repsonse variables

	print "---------------------------------"
	print " "
	print "Predicting on test data: "

	# BOW for test set
	test_data_features = vectorizer.transform(test_review_list)
	test_data_features = test_data_features.toarray()

	# use the trained forest to make predictions
	predictions = forest.predict(test_data_features)

	# prepare output submission file
	prediction_output = pd.DataFrame( data = {"id":test_data["id"], "sentiment":predictions} ) # create pandas dataframe
	prediction_output.to_csv("TFIDF_RF.csv", index=False, quoting=3)# write to csv file
	joblib.dump(vectorizer, 'tfidf_model.pkl')
	joblib.dump(forest, 'rf_tfidf_model.pkl')  

if __name__ == '__main__':
	main()