from obdet import *
import warnings

warnings.filterwarnings('ignore')

d = {"lifebuoy": 44, "indulekha": 137, "aqualens": 86, 'voyage': 105}
scale_weight = 50


# main code
def run_model():
	vidcap = cv2.VideoCapture(0)
	
	while True:
		success, frame = vidcap.read()  # read method
		print("Scanning")  # -> blue light
		
		if not success:
			break
		if cv2.waitKey(2):
			object_detect(frame, ('WongKinYiu/yolov7', 'custom', 'last_.pt'), d, scale_weight)
			# object_detect(frame object, tuple('github repo', 'model type(pretrained / custom)', 'path/to/best/pt'), \d, scale_weight)
			break


# driver function
if __name__ == '__main__':
	run_model()


# camera = cv2.VideoCapture(0)
# i = 0
# while i < 10:
#     input('Press Enter to capture')
#     return_value, image = camera.read()
#     cv2.imwrite('opencv'+str(i)+'.png', image)
#     i += 1
# del(camera)


# driver code
# while True:
# 	success, frame = vidcap.read()  # read method
# 	print("Scanning")  # -> blue light
#
# 	if not success:
# 		break
# 	if cv2.waitKey(2):
# 		object_detect(frame)
# 		break
