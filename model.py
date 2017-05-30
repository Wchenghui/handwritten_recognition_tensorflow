from PIL import Image
import struct

def read_image(filename):
    f = open(filename, 'rb')

    index = 0
    buf = f.read()

    f.close()
    magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')
    for i in xrange(images):
        image = Image.new('L', (columns, rows))

        for x in xrange(rows):
            for y in xrange(columns):
                image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                index += struct.calcsize('>B')
        print 'save ' + str(i) + 'image'
        image.save('/home/wch/MNIST_data/data/' + str(i) + '.png')

def read_label(filename, saveFilename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()

    f.close()

    magic, labels = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')

    labelArr = [0] * labels
    # labelArr = [0] * 2000

    for x in xrange(labels): 
        labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')

    save = open(saveFilename, 'w')

    save.write(','.join(map(lambda x: str(x), labelArr)))
    save.write('\n')

    save.close()
    print 'save labels success'


if __name__ == '__main__':
     read_image('/home/wch/MNIST_data/test-images-idx3-ubyte')
     read_label('/home/wch/MNIST_data/test-labels-idx1-ubyte', '/home/wch/MNIST_data/label.txt')
