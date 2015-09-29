#import cgitb
#cgitb.enable()
import query_model as qm
#import nltk
#nltk.download('all')

#def main():
#	print "Main Function"
#	print qm.calculate_sentiment("This is a good movie")	

def get_info(req):
	tmp = None
	info = req.form
	moviereview = info['txtMovieReview']
	try:
		sentiment = qm.calculate_sentiment(moviereview)
		if sentiment == 1:
			tmp = "<span style='color:Green'><b>Positive Review</b></span>"
		else:
			tmp = "<span style='color:Red'><b>Negative Review</b></span>"
	except:
		return "Error"
	#moviesentiment = str(qm.calculate_sentiment("This is a good movie"))
	return """
<html style='display: table; margin: auto'>
<head>
<title>Sentimental Analysis on Movie Review</title>
</head>
<body style='display: table-cell; vertical-align: middle; width: 700px; background-color: #e3e2dd; font-family: verdana'>
<h2 style='text-align: center; padding-top: 10px'>Movie Review Sentimental Analysis</h2>
<br/>
<p style='text-align: center'>You have requested movie reviw sentimental analysis for the following movie reviews.</p>
<table style='margin: 0px auto; font-family: verdana; font-size: 18px'>
<tr>
<td style='width: 300px'><b>Entered Movie Review</b></td><td>%s</td>
</tr>
<tr>
<td><b>Classified Sentiment</b></td><td>%s</td>
</tr>
</table>
</body>
</html>
""" %(moviereview,tmp)

#if __name__ == '__main__':
#	main()

