

import cv2
import easyocr
import matplotlib.pyplot as plt
image_paths = ['i1.jpg' ,  'i2.jpg'] 
image = []
# instancing text detector  en for english detection
reader = easyocr.Reader(['en'],gpu = False)    
for path in image_paths:
 img = cv2.imread(path)
 image.append(img)
# DISPLAYING THE IMAGE
i = 0
threshold = 0.25
for img in image:
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    text = reader.readtext(img)
    for t in text:
        bbox, text, score = t
        text_position = (int(bbox[0][0]) + 20, int(bbox[0][1]) - 20)  # Slightly offset from the top-left corner
        if score > threshold:
           
            cv2.putText(img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # Drawing bounding box around the text region
            cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
            # Display the image
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
        else:
            text = " not so accurate"
            # Put the text on the image
            cv2.putText(img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # Display the image
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
         
#   i+=1 
