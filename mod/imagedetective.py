import cv
import math
from PIL import Image


class ImageDetective:
    
    def __init__(self, src):
        self.src = Image.open(src)


    def rgb_to_hsv(self, r, g, b):
        maxc = max(r, g, b)
        minc = min(r, g, b)
        colorMap = {
            id(r): 'r',
            id(g): 'g',
            id(b): 'b'
        }
        if colorMap[id(maxc)] == colorMap[id(minc)]:
            h = 0
        elif colorMap[id(maxc)] == 'r':
            h = 60.0 * ((g - b) / (maxc - minc)) % 360.0
        elif colorMap[id(maxc)] == 'g':
            h = 60.0 * ((b - r) / (maxc - minc)) + 120.0
        elif colorMap[id(maxc)] == 'b':
            h = 60.0 * ((r - g) / (maxc - minc)) + 240.0
        v = maxc
        if maxc == 0.0:
            s = 0.0
        else:
            s = 1.0 - (minc / maxc)
        return (h, s, v)


    def point_detection(self):
        img = self.src
        pixels = img.load()
        
        for y in xrange(1, img.size[1]-1):
            for x in xrange(1, img.size[0]-1):
                columns = []
                matrix = [[pixels[x-1, y-1], pixels[x, y-1], pixels[x+1, y-1]],
                            [pixels[x-1, y], pixels[x, y], pixels[x+1, y]],
                            [pixels[x+1, y+1], pixels[x, y+1], pixels[x+1, y+1]]]
                for column in matrix:
                    columns.append(map(lambda k: k > 200, [k for w in column for k in w if k == w[0]]))
            
                if len([j for i in columns for j in i if not j]) <= 5:
                    img.putpixel((x,y), (255, 255, 255))
                    
        self.src = img
        return self.src
        

    def edge_detection(self, S):
        img = self.src
             
        img_output = Image.new("RGB", (img.size[0], img.size[1]))
        pixels = img.load()

        for y in xrange(1, img.size[1]-1):
            for x in xrange(1, img.size[0]-1):
                y_this_rgb = pixels[x, y]
                y_prev_rgb = pixels[x, y-1]
                y_next_rgb = pixels[x, y+1]
                y_this_hsv = self.rgb_to_hsv(y_this_rgb[0], y_this_rgb[1], y_this_rgb[2])
                y_prev_hsv = self.rgb_to_hsv(y_prev_rgb[0], y_prev_rgb[1], y_prev_rgb[2])
                y_next_hsv = self.rgb_to_hsv(y_next_rgb[0], y_next_rgb[1], y_next_rgb[2])
        
                Dy = y_next_hsv[2] - y_prev_hsv[2]

                x_this_rgb = pixels[x, y]
                x_prev_rgb = pixels[x-1, y]
                x_next_rgb = pixels[x+1, y]
                x_this_hsv = self.rgb_to_hsv(x_this_rgb[0], x_this_rgb[1], x_this_rgb[2])
                x_prev_hsv = self.rgb_to_hsv(x_prev_rgb[0], x_prev_rgb[1], x_prev_rgb[2])
                x_next_hsv = self.rgb_to_hsv(x_next_rgb[0], x_next_rgb[1], x_next_rgb[2])
            
                Dx = x_next_hsv[2] - x_prev_hsv[2]
            
                Grad = math.fabs(Dx) + math.fabs(Dy)
                img_output.putpixel((x,y), Grad > S and (0, 0, 0) or (255, 255, 255))
                    
        self.src = img_output
        return self.src
    
    
    def save_image(self, name, est):
        self.src.save(name, est)
