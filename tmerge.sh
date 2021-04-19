files=$(find $1 -name "*.nii*" | sort --version-sort)

/home/whall/fsl/bin/fslmerge -t $2.nii.gz $files
