#import cgitb
#cgitb.enable()
import query_model1 as qm
#import nltk
#nltk.download('all')

#def main():
#	print "Main Function"
#	print qm.calculate_sentiment("This is a good movie")	

def get_info(req):
	tmp = None
	info = req.form
	moviereview = info['txtMovieReview']
	allmoviereview = info['iSavedReview']
	spEachReview = allmoviereview.split('<br/><hr/>')
	#allmoviereview = len(spEachReview)
	combinedText = ''
	#countPositive = 0
	#countNegative = 0
	for review in spEachReview:
		tmp1 = None
                sentiment =  qm.calculate_sentiment(review)
                if sentiment == 1:
                        tmp1 = "<span style='color:Green'><b>Positive Review</b></span>"
			#countPositive = countPositive + 1	
                else:
                        tmp1 = "<span style='color:Red'><b>Negative Review</b></span>"
			#countNegative = countNegative + 1
		
		if review != '' :
			combinedText = str(combinedText) + str(review) + ' - ' + str(tmp1) + '<br/>'

	#try:
	#	sentiment = qm.calculate_sentiment(moviereview)
	#	if sentiment == 1:
	#		tmp = "<span style='color:Green'><b>Positive Review</b></span>"
	#	else:
	#		tmp = "<span style='color:Red'><b>Negative Review</b></span>"
	#except:
	#	return "Error"
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
<table style='margin: 0px auto; font-family: verdana; font-size: 18px; line-height: 28px'>
<tr>
<td style='width: 250px'><b>Entered Movie Review</b></td><td>%s</td>
</tr>
</table>
</body>
</html>
""" %(combinedText)

#if __name__ == '__main__':
#	main()
#	<p>Positive Count: %d, Negative Count: %d</p>
#	%(countPositive, countNegative, combinedText)

