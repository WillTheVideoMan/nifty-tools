import nibabel as nib


img = nib.load("/home/whall/Pictures/SARS-CoV-2/UK_Intravenous/intravenous-T[before-30m-1h-2h-12h].nii.gz")

print(img.header)

img.header['bitpix'] = 16
img.header['datatype'] = 4

nib.save(img, "/home/whall/Pictures/SARS-CoV-2/UK_Intravenous/debug-16bit.nii.gz")
