# loads all the saved weights into a tensorflow variable

import os
import numpy as np


def run():
	params_dict = {}

	for file in os.listdir("./"):
	    if file.endswith(".npy"):
	        filename = os.path.join("./", file)
	        filename = filename
	        params_dict[filename[2:-4]] = np.load(filename)

	return params_dict

if __name__ == "__main__":
	run()






