# Pencil_sketcher


This tool is made using cv2 library .

The process is pretty simple:

Grayscale the image
Invert it
Blur the inverted image
Dodge blend the blurred and grayscale image.

The Colour Dodge blend mode divides the bottom layer by the inverted top layer. This lightens the bottom layer depending on the value of the top layer. We have the blurred image, which highlights the boldest edges.

But we have used an optimized version of dodge in the code.

While running the file, makesure to change the image path while loading the image.
 
