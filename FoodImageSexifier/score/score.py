import sys, getopt
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

def main(argv):
	model = app.models.get('tasty-or-nasty')
	image = ClImage(url=argv[0])
	response = model.predict([image]) 
	print ('your score is ', response.data.concepts[0].value)

