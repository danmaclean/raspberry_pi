import IRCamera as ir
import matplotlib.pyplot as plt

def do_ndvi_plot(original_image, ndvi_im,fname='ndvi.png'):
    IRCamera.register_colour_maps()
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


image = ir.get_rgb_array(100,100)
print "scaling image.."
ndvi_im = ir.ndvi(image)
print ndvi_im.shape
print "plotting.."
ir.do_ndvi_plot(image,ndvi_im)

healthy_mask = ir.get_healthy_region_mask(ndvi_im)
ill_mask = ir.get_unhealthy_region_mask(ndvi_im)
cold_mask = ir.get_cold_region_mask(ndvi_im)

ir.do_mask_plot(im,ndvi_im,healthy_mask,ill_mask,cold_mask)


