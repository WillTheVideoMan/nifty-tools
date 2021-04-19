files=$(find $1 -name "*.hdr" | sort --version-sort)

/home/whall/fsl/bin/fslmerge -z $2.nii.gz $files
