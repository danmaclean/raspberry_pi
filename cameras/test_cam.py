import IRCamera as ir

def do_plot(original_image, scaled_image):
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
    
    fig.tight_layout()
    plt.show(fig)


image = ir.get_rgb_array(2592,1944)
print "scaling image.."
scaled_image = ir.enhance_ir(image)
print "plotting.."
do_plot(image,scaled_image)