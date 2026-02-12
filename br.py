import cv2 
import numpy as np 
from PIL import Image, ImageEnhance 
from matplotlib import pyplot as plt 
p = r"C:\Users\sahan\Desktop\SMD\input.jpg"
imcv = cv2.imread(p) 
if imcv is None: 
    raise FileNotFoundError(f"Image not found: {image_path}") 
rgb = cv2.cvtColor(imcv, cv2.COLOR_BGR2RGB) 
pil = Image.fromarray(rgb) 
er = ImageEnhance.Brightness(pil) 
br = er.enhance(0.05) 
er = ImageEnhance.Contrast(br)
con = er.enhance(2.0) 
er = ImageEnhance.Sharpness(con) 
sharp = er.enhance(2.5) 
ed = cv2.cvtColor(np.array(sharp), cv2.COLOR_RGB2BGR) 
plt.figure(figsize=(12, 6)) 
plt.subplot(1, 2, 1) 
plt.title('Original Image') 
plt.imshow(rgb) 
plt.axis('off') 
plt.subplot(1, 2, 2) 
plt.title('Enhanced Image') 
plt.imshow(cv2.cvtColor(ed, cv2.COLOR_BGR2RGB)) 
plt.axis('off') 
plt.show() 
cv2.imwrite('enhanced_image.jpg', ed)
