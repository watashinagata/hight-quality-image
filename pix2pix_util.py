import cv2
import numpy as np
from argparse import ArgumentParser
import glob
import os

if __name__ == "__main__":
    arg = ArgumentParser()
    arg.add_argument('-id', '--inputdir', help='select input directory', required=True)
    arg.add_argument('-od', '--outputdir', help='select output directory', required=True)
    args = arg.parse_args()

    os.makedirs(args.outputdir, exist_ok=True) 
    if os.path.exists(args.inputdir) == True:
        files = glob.glob(args.inputdir+"/*") 
        print("PIX2PIX_UTIL: Processing...")
        for i in files:
            file_name = os.path.basename(i) 
            img = cv2.imread(i) 
            if type(img) == np.ndarray: 
                height, width = img.shape[:2]
                for j in range(int(height / 256)):
                    for k in range(int(width / 256)):
                        splited_image = img[256 * j : 256 * j + 256, 256 * k : 256 * k + 256]
                        blurred_image = cv2.blur(splited_image, (10, 10))
                        margined_image = cv2.hconcat([splited_image, blurred_image]) 
                        cv2.imwrite("{0}/{1}_{2}_{3}.jpg".format(args.outputdir, file_name[:-4], str(j), str(k)), margined_image) 
            else:
                print("ERROR: {0} is not supported type".format(file_name)) 
        print("PIX2PIX_UTIL: Completed") 
    else:
        print("ERROR: No such directory \"{0}\"".format(args.inputdir)) 