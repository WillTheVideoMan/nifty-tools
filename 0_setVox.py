import nibabel as nib
import sys

xVox = sys.argv[1]
yVox = sys.argv[2]
zVox = sys.argv[3]

filePath = sys.argv[4]

img = nib.load(filePath)

img.header['pixdim'][1] = xVox
img.header['pixdim'][2] = yVox
img.header['pixdim'][3] = zVox

nib.save(img, filePath)

print("Updated Voxels to {0}x{1}x{2} for {3}".format(xVox, yVox, zVox, filePath))