﻿# Pragmatic-Natural-Language-Generation-with-Neural-Language-Models
This report aims to evaluate pragmatic adequacy of image descriptions generated by GPT-4v.
The goal was to answer the question: How good this powerful neural image captioner is in
pragmatically describing pictures?
This paper is based on the "Evaluating pragmatic abilities of image captioners on A3DS" by Tsvilodub and Michael Franke (2023). https://aclanthology.org/2023.acl-short.110
The data used for this paper comes from: Chris Burgess and Hyunjik Kim. 2018. 
3d shapes dataset. https://github.com/deepmind/3dshapesdataset/.


The results can be found in the "results.pdf"
The code for calculating the metrics and the used images can be found in "pairing features.py"
The "image" folder contains the images cropped used in this experiment cropped.
The "images_uncropped" folder contains the images before cropping.
The "one-feature" folder contains an pair of two images, who share one feature.
The "two-features" folder contains an pair of two images, who share two features.
The "three-features" folder contains an pair of two images, who share three features.
