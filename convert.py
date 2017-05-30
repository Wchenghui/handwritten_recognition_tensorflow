from PIL import Image
import os.path
import glob
from numpy import *
def convertpng(pngfile,outdir):
    img=array(Image.open(pngfile))   
    img2=255-img 
    new_img = Image.fromarray(img2) 
    new_img.save(os.path.join(outdir,os.path.basename(pngfile)))
for pngfile in glob.glob("/home/wch/MNIST_data/data/*.png"):
    convertpng(pngfile,"/home/wch/MNIST_data/data_convert")
