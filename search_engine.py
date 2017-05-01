import RGBHistogram
import searcher
import cPickle
import glob
import cv2
import sys 
index = {}

desc = RGBHistogram.RGBHistogram([8,8,8])

for imagePath in glob.glob("images/*"):
	k = imagePath[imagePath.rfind("/")+1:]
	#k is name of image
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

#f = open('index_file',"w")
#f.write(cPickle.dumps(index))
#f.close()

#an instance 
search = searcher.Searcher(index)

#define a query image
query_image = sys.argv[1]

#calling search on instance 
matched_results = search.search(index[query_image])

cv2.imshow('image',cv2.imread('images/'+query_image))

for i in range(0,5):
	cv2.imshow('match'+str(i),cv2.imread('images/'+matched_results[i][1]))

cv2.waitKey(0)
cv2.destroyAllWindows()


