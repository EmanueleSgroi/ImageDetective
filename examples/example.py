import sys
sys.path.append("../mod")
import imagedetective

my_image = imagedetective.ImageDetective("original.jpg")
print "Edge detection is executing..."
my_image.edge_detection(40)
print "Done! Saving image..."
my_image.save_image("example.jpg", "JPEG")
print "Done!"
