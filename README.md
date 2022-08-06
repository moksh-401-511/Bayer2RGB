# Bayer2RGB
Demosaicing (Conversion) of Raw 8-bit Bayer image into RGB image
<br>

**Input**: 
  - Binary file containing one or more bayer format images
  
**Parameters**: 
  - file name ``` --file / -f ```
  - bayer pattern ``` --pattern / -bp ```
  - height ``` --height / -ht ``` and widht ``` --widht / -wd ```
  - desired output image format ``` --format / -fo ```

**Output**: 
  - RGB image(s)

## Bayer Pattern
Bayer format images follow a sensor alignemnt (pattern) which is repeated over the image.
<br>
![bayer pattern explanation](<Bayer Pattern.jpg>)

## Installation
run the following command in terminal
```
git clone https://github.com/moksh-401-511/Bayer2RGB.git
```

## Example
Binary bayer format file: [bayer_image.bin](https://github.com/moksh-401-511/Bayer2RGB/blob/main/raw_image/bayer_image.bin) <br>
(this Raw image is taken from [here](https://www.bogotobogo.com/Matlab/images/MATLAB_DEMO_IMAGES/) then converted into binary file for testing purpose)
  - binary pattern 'bggr' | dimension 3039x2014 | desired format '.png'
 ```
 python bayer_to_rgb.py -f bayer_image.bin -bp bggr -wd 3039 -ht 2014 -fo png
 ```
 output [rgb image](https://github.com/moksh-401-511/Bayer2RGB/blob/main/rgb_image/bayer_image-rgb-1.png)
