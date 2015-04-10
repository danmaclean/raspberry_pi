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

def get_healthy_region_mask(img,lower=0.1, upper=0.9 ):
    tmp = img.copy()
    tmp[(tmp >= lower) & (tmp <= higher)] = 1
    tmp[tmp < 1] = 0
    return tmp

def get_unhealthy_region_mask(img, lower=-0.1, upper=0.1):
    tmp = img.copy()
    tmp[(tmp >= lower) & (tmp <= upper)] = 1
    tmp[tmp < 1] = 0
    return tmp

def get_cold_region(img, upper):
    tmp = img.copy()
    tmp[tmp <= upper] = 1
    tmp[tmp <1] = 0
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

def ndvi_filter(r,g,b):
    '''scales a single pixel for IR to give the NDVI value'''
    try:
        return (r-b)/(r+b)
    except ZeroDivisionError:
        return 0.0
    
def ndvi(im):
    '''takes image and returns np.ndarray of values scaled with ndvi_filter.
    Ensures the range of values is -1,1 by setting top left pixels manually.
    '''
    result = np.empty(shape=(im.shape[0],im.shape[1]))
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            result[i,j] = ndvi_filter(float(im[i,j][0]), float(im[i,j][1]), float(im[i,j][2]))
    #fix the range
    result[0,0]= -1.0
    result[0,1]= 1.0
    return result

def do_ndvi_plot(original_image, ndvi_im,fname='ndvi.png'):
    register_colour_maps()
    fig = plt.figure(figsize=(10,3))
    
    axes1 = fig.add_subplot(1,3,1)
    axes2 = fig.add_subplot(1,3,2)
    axes3 = fig.add_subplot(1,3,3)
    
    axes1.set_ylabel("Raw")
    axes2.set_ylabel('Grey')
    axes3.set_ylabel('GreyReds')
    
    axes1.imshow(original_image)
    axes2.imshow(scaled_image,cmap='GreyIntensity')
    axes3.imshow(scaled_image,cmap='RedSplit')
    
    plt.savefig(fname)
    plt.close()
    
def do_masking_plot(im,ndvi_im,healthy_im,unhealthy_im,cold_im,fname="mask_plot.png"):
    ims = [im,ndvi_im,healthy_im,unhealthy_im,cold_im]
    fig = plt.figure(figsize=(16,5))
    for i in range(1,6):
        img_ax = fig.add_subplot(1,5,i)
        if i == 1:
            img_ax.imshow(im[i]-1,cmap="GreyIntensity")
    plt.savefig(fname)
    plt.close()
    