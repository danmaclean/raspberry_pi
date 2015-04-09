import picamera
import picamera.array
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def register_colour_maps():
    cdict = {'red':   ((0.0,  0.0, 0.0),
                       (0.0,  0.0, 0.0),
                       (1.0,  1.0, 1.0)),
                       
         'green': ((0.0,  0.0, 0.0),
                   (0.0,  0.0, 0.0),
                   (1.0,  1.0, 1.0)),
                   
         'blue':  ((0.0,  0.0, 0.0),
                   (0.0,  0.0, 0.0),
                   (1.0,  1.0, 1.0))}
    
    plt.register_cmap(name='GreyIntensity', data=cdict)
    
    cdict2 = {'red': ((0.0, 0.0, 0.0),
                 (0.5, 1.0, 0.7),
                 (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 0.0),
                   (0.5, 1.0, 0.0),
                   (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (0.5, 1.0, 0.0),
                  (1.0, 0.5, 1.0))}
    
    plt.register_cmap(name='RedSplit', data=cdict2)

def make_hot_ones(img):
    tmp = img.copy()
    tmp[tmp > 0.2] = 1
    tmp[tmp < 1] = 0
    return tmp

def make_cold_ones(img):
    tmp = img.copy()
    tmp[(tmp < 0.2) & (tmp > 0.0)] = 1
    tmp[tmp < 1] = 0
    return tmp

def get_rgb_array(width,height):
    '''returns a 3D numpy array of image RGB values '''
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution = (width, height)
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, 'rgb')
            # Show size of RGB data
            return stream.array

def blue_filter(r,g,b):
    '''scales a single pixel for IR'''
    try:
        return (r-b)/(r+b)
    except ZeroDivisionError:
        return 0.0
    
def enhance_ir(im):
    '''takes image and returns np.ndarray of values scaled with blue_filter'''
    result = np.empty(shape=(im.shape[0],im.shape[1]))
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            result[i,j] = blue_filter(float(im[i,j][0]), float(im[i,j][1]), float(im[i,j][2]))
    return result

