#Jessica De Mota Munoz
#September 24 2019
#jessica.demotamunoz86@myhunter.cuny.edu


import matplotlib.pyplot as plt
import numpy as np 

inputfile = input('Enter name of the input file:')
outputfile =input('Enter name of the output file:')

img =plt.imread(inputfile)
#plt.show(img)
#plt.show 

img2 = img.copy()
img2[:,:,1] = 0
img2[:,:,0] = 0

#plt.imshow(img2)
#plt.show()

plt.imsave(outputfile, img2)
