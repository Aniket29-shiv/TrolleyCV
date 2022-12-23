import torch
import cv2
import os


def object_detect(image, model_config: tuple, res_dict, pr_weight):
	output_string = []
	res_img = []
	
	# Model
	model = torch.hub.load(model_config[0], model_config[1], model_config[2])
	# model = torch.hub.load('ultralytics/yolov5', 'custom', 'path/to/last or best.pt')  # custom trained model
	
	# Images
	cv2.imwrite('opencv_' + '.png', image)
	im = 'D:\Search In\Trolley cv\TrolleyCV\opencv_.png'
	results = model(im)
	os.remove("opencv_.png")
	
	# Results
	results.print()
	results.xyxy[0]  # im predictions (tensor)
	res = results.pandas().xyxy[0]  # im predictions using (pandas)
	class_name = (res['name']).tolist()
	res_img.append(class_name)
	output_string.append(return_string(res_img, res_dict=res_dict, pr_weight=pr_weight))


def return_string(res, res_dict, pr_weight):
	flatList = [el for sublist in res for el in sublist]  # output array
	
	if len(flatList) > 0:
		result = max(flatList, key=flatList.count)
		print(result)
		weight = res_dict[result]  # print(weight)
		
		min_weight = abs(weight * 10 / 100 - weight)
		max_weight = weight * 10 / 100 + weight
		# print(f"min_weight = {min_weight}, max_weight = {max_weight}, Practical scaled weight = {pr_weight}")
		
		if min_weight <= pr_weight <= max_weight:
			print("true")  # -> green light
		else:
			print("false")  # -> red light -> buzzer
		
		return result
	
	else:
		print("No detection")  # -> yellow light
