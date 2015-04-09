import picamera
import numpy

width = 2592
height = 1944


def get_rgb_array(width,height):
    '''returns a 3D numpy array of image RGB values '''
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution = (width, height)
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, 'rgb')
            # Show size of RGB data
            print(stream.array.shape)