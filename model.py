import cv2
# from IPython.display import Image, display
import torch
import numpy as np
import os
# camera = cv2.VideoCapture(0)
# i = 0
# while i < 10:
#     input('Press Enter to capture')
#     return_value, image = camera.read()
#     cv2.imwrite('opencv'+str(i)+'.png', image)
#     i += 1
# del(camera)

res_img =[]
output_string =[]
d = {"lifebuoy":44 , "indulekha":137 , "aqualens":86}
pr_weight = 48

def object_detect(image):
    """
    in Colab, run_algo function gets invoked by the JavaScript, that sends N images every second
  
    params:
      image: image
    """
        # Model
    model = torch.hub.load('WongKinYiu/yolov7', 'custom' ,'last_.pt')  # or yolov5m, yolov5l, yolov5x, etc.
    # model = torch.hub.load('ultralytics/yolov5', 'custom', 'path/to/best.pt')  # custom trained model

    # Images
    cv2.imwrite('opencv_'+'.png', image)
    im ="E:\Downloads\TrolleyCV\opencv_.png"
    # or file, Path, URL, PIL, OpenCV, numpy, list2
    # cv2.imwrite('opencv_'+'.png', image)
    # Inference
    results = model(im)
    os.remove("opencv_.png")

    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

    results.xyxy[0]  # im predictions (tensor)
    res =results.pandas().xyxy[0]  # im predictions (pandas)
    class_name =(res['name']).tolist()
    res_img.append(class_name)
    output_string.append(return_string(res_img))

def return_string(res_img):
  flatList = [el for sublist in res_img for el in sublist]
  if len(flatList) >0:
            result = max(flatList, key = flatList.count)
            print(result)
            weight = d[result]
            # print(weight)
            min_weight = abs(weight*10/100-weight)
            max_weight = weight*10/100+weight
            # print(min_weight, " ", max_weight," ", pr_weight)
            if min_weight<= pr_weight <= max_weight:
              print("true")
            else:
              print("false")
            return result
        
vidcap = cv2.VideoCapture(0)

while True:
    success, frame = vidcap.read()
    if not success:
         break
    if cv2.waitKey(2):
        object_detect(frame)
        break