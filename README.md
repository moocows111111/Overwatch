# Overwatch

This is a repo that'll contain all the important scripts in order to run the Overwatch/FPS video analyzer.

ConvertVid.py is the video to image converted which converts the video to a series of frames. As of right now it will continue until a command is given for it to stop. It natively extracts ALL frames but will be revised to only capture every other frame.

Crop.py is designed to crop the images from the center, but it's still being fleshed out. So far it works, but it skips frames randomly for some reason. # Turns out I just needed to run the program till the end even though it lags my PC since imread tends to skip frames but it will run over them again on other passes.

MoreBlend.py takes a the image directory and chunks it into groups of 10 images. Then it takes those 10 and then blends them additively so that the temporal changes are recorded in an instant!


