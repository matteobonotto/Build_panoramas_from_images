import os
import sys
import matplotlib.pyplot as plt
# sys.path.append('/home/bonotto/workspace/miniconda3/envs/panorama-stitching/lib/python3.9/site-packages')

# os.system('export PYTHONPATH=/home/bonotto/workspace/miniconda3/envs/panorama-stitching/lib/python3.9/site-packages:$PYTHONPATH')

import cv2
import imutils
###
def main():
    path = r'./data/input/test_1/'
    dir_content = os.listdir(path)
    imagePaths = [path + f for f in dir_content]
    # for picture in dir_content:

    print("[INFO] loading images...")
    images = []
    # loop over the image paths, load each one, and add them to our
    # images to stitch list
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)

    plt.imshow(image)
    plt.show()

    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite(args["output"], stitched)
        # display the output stitched image to our screen
        cv2.imshow("Stitched", stitched)
        cv2.waitKey(0)
    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))


###
if __name__ == '__main__':
    main()