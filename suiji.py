import random, os
from PIL import Image
path = r"/home/wch/MNIST_data/data_convert"
random_filename = random.sample([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
],100)
print(random_filename)
for y in random_filename:
    img=Image.open('/home/wch/MNIST_data/data_convert/' + str(y))
    img.save('/home/wch/MNIST_data/randomdata/' + str(y))
