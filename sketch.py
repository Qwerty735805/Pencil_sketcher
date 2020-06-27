import cv2

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def load_img(image_path):
	picture = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
	return picture

def convert(pic):
	gray_picture = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
	inverted_picture = 255-gray_picture
	blur_picture = cv2.GaussianBlur(inverted_picture,ksize=(15,15),sigmaX=10,sigmaY=10) 
	sketch = cv2.divide(gray_picture,255-blur_picture,scale=256) 
	return sketch

# image=load_img('10.jpg')  #Image path 
# cv2.imshow('Uploaded image',image)
# cv2.waitKey(0)
# sketch=convert(image)
# cv2.imshow('sketch',sketch)
# cv2.waitKey(0)
# cv2.imwrite('sketch.jpg',sketch)