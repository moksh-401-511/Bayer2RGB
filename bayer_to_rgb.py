#----------------- Image parsing Task--------------------------------
# Converting 8-bit Bayer format images into RGB and saving into disk
#---------------------------------------------------------------------

import numpy as np
import cv2
import argparse

def main():
    
    # parsing arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",   type=str, help = "Input binary file name")
    parser.add_argument("-ht", "--height", type=int, help = "Height of image")
    parser.add_argument("-wd", "--width",  type=int, help = "Width of image")
    parser.add_argument("-bp", "--pattern", type=str, help = "Bayer pattern")
    parser.add_argument("-fo", "--format", type=str, help = "RGB image format")
    args = parser.parse_args()
    
    # set variables
    file_name    =  args.file
    bayer_pattern=  args.pattern
    rgbformat    =  args.format
    h, w         =  args.height, args.width
    total_pixels =  h*w
    
    if bayer_pattern == 'rggb':
        col, row, g = 0, 0, 1
    elif bayer_pattern == 'bggr':
        col, row, g = 1, 1, 1
    elif bayer_pattern == 'grbg':
        col, row, g = 1, 0, 0
    elif bayer_pattern == 'gbrg':
        col, row, g = 0, 1, 0

    # loading binary file
    bayer = np.fromfile('raw_image/'+file_name, dtype=np.uint8)

    # total images in binary file
    total_images = bayer.shape[0]//(total_pixels)

    for i in range(total_images):
        # extracting current image part
        img = bayer[total_pixels*i : total_pixels*(i+1)]
        
        # resizing
        img = img.reshape((h,w))
        
        # extracting each color layer
        R_img  = img[abs(col)  ::2, abs(row)  ::2]
        B_img  = img[abs(1-col)::2, abs(1-row)::2]
        G0_img = img[0         ::2, abs(g)    ::2]
        G1_img = img[1         ::2, abs(g-1)  ::2]
        
        # total pixels of each RBGG layer
        oh, ow = h//2, w//2
        
        # Excluding out-of-frame edges
        R = R_img[:oh,:ow]
        B = B_img[:oh,:ow]
        #  average green values
        G = G0_img[:oh,:ow]//2 + G1_img[:oh,:ow]//2

        # Formulate image by stacking R, G and B and save
        final_img = np.dstack((B,G,R))
        
        # Linear Interpolation
        resized_img = cv2.resize(final_img, (w, h), interpolation = cv2.INTER_LINEAR)
        
        # saving to drive
        cv2.imwrite(f"rgb_image/{file_name.rpartition('.')[0]}-rgb-{i+1}.{rgbformat}", resized_img)
    print("RGB Conversion Successfully Completed\nImages saved to disk")
        
if __name__ == '__main__':
    main()
