#The Gatekeeper 

import time
from PIL import Image
import numpy as np

#Generating a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

#Print the generated number
print("Generated number (n):", generated_number)

#Loading the image and converting to a manageable format
img = Image.open("Question2/chapter1.jpg")
img_array = np.array(img)  

# Add the generated number to every color in every pixel to change the image's appearance
img_array = np.clip(img_array + generated_number, 0, 255)  
total_red_value = np.sum(img_array[:, :, 0])  

# Save the modified image to a png file
modified_img = Image.fromarray(img_array.astype('uint8')) 
modified_img.save("Question2/chapter1out.png")

# Print the total red color intensity in the changed image
print("Total sum of red values:", total_red_value)
