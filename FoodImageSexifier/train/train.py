from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import glob, os


app = ClarifaiApp()

model = app.models.create("tasty-not-tasty",   
    concepts=["tasty","nasty"], concepts_mutually_exclusive=True)

os.chdir("/data/tasty")
for file in glob.glob("*.jpg"):
    app.inputs.create_image_from_filename (url=file, concepts=["tasty"])

os.chdir("/data/nasty")
for file in glob.glob("*.jpg"):
    app.inputs.create_image_from_filename (url=file, concepts=["nasty"])

model.train()
