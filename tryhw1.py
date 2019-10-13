from uwimg import *
im = load_image("data/dog.jpg");
a = nn_resize(im, 713,467)
save_image(a, "dog713467-nn")
free_image(im)

im = load_image("data/dogsmall.jpg")
a = bilinear_resize(im, im.w*4, im.h*4)
save_image(a, "dog4x-bl")
free_image(im)

im = load_image("data/dog.jpg")
a = nn_resize(im, im.w//7, im.h//7)
save_image(a, "dog7th-bl")
free_image(im)