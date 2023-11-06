# PIP INSTALL REQUIRED
# pillow, easyocr, opencv-python, matplotlib, spellchecker
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['ch_sim','en'], gpu = False)
from PIL import Image
import matplotlib.pyplot as plt
img_plot = Image.open('algorithms/optical_character_recognition/cabinet_test_1.jpg')
plt.imshow(img_plot)
plt.title('Original Image')
plt.show()

#TESTING EASYOCR WITH NO PREPROCESS
image_path = 'algorithms/optical_character_recognition/cabinet_test_1.jpg'
img = Image.open(image_path)
img.save("algorithms/optical_character_recognition/preprocessed_image1.jpg")
img_plot = Image.open('algorithms/optical_character_recognition/preprocessed_image1.jpg')
plt.imshow(img_plot)
plt.title('Original Image')
result = reader.readtext('algorithms/optical_character_recognition/preprocessed_image1.jpg', detail = 0)
print(result)

#TESTING WITH ROTATION AND GRAYSCALE
# Load the original image
image_path = 'algorithms/optical_character_recognition/cabinet_test_1.jpg'
img = Image.open(image_path)

# Rotate the image by -90 degrees
img = img.rotate(-90)

# Convert the image to grayscale
img = img.convert("L")

# Save the preprocessed image
img.save("algorithms/optical_character_recognition/preprocessed_image2.jpg")

# Plot the preprocessed image
img_plot = Image.open('algorithms/optical_character_recognition/preprocessed_image2.jpg')
plt.imshow(img_plot, cmap='gray')  # Use 'gray' colormap for grayscale images
plt.title('Preprocessed Image')
plt.show()
result = reader.readtext('algorithms/optical_character_recognition/preprocessed_image2.jpg',detail=0)
print(result)


#TESTING EASYOCR WITH ROTATION PREPROCESS 
# Load the original image
image_path = 'algorithms/optical_character_recognition/cabinet_test_1.jpg'
img = Image.open(image_path)

# Rotate the image by -90 degrees
img = img.rotate(-90)

# Save the preprocessed image
img.save("algorithms/optical_character_recognition/preprocessed_image3.jpg")

# Plot the preprocessed image
img_plot = Image.open('algorithms/optical_character_recognition/preprocessed_image3.jpg')
plt.imshow(img_plot) 
plt.title('Preprocessed Image')
plt.show()
result = reader.readtext('algorithms/optical_character_recognition/preprocessed_image3.jpg',detail=1)
print(result)

#DISPLAYING RESULTS
for detection in result:
    if (detection[2] > 0.4):
        text = detection[1]
        weight = detection[2]
        print(f"Text: {text}, Confidence: {weight}")

#TESTING BOUNDING BOX DISPLAY
import cv2
image_path = 'algorithms/optical_character_recognition/preprocessed_image3.jpg'
image = cv2.imread(image_path)
for details in result:
    if (details[2] > 0.4): #Confidence threshold
        x = int(details[0][0][0]) # first zero represents the 2d vector in details
        y = int(details[0][0][1]) # second zero represents which pair of (x,y) points
        w = int(details[0][1][0])-x #third zero represents x or y
        h = int(details[0][2][1])-y
        print(f"Word: {details[1]}")
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Image with Rectangle')
plt.show()


# TESTING WITH SPELL CHECKER
# CURRENTLY NOT WORKING ON VSCODE/LAPTOP (AVAILABLE ON DESKTOP)
# from spellchecker import SpellChecker
# spell = SpellChecker()

# for details in result:
#     if (details[2] > 0.4): #confidence threshold
#         x = int(details[0][0][0]) # first zero represents the 2d vector in details
#         y = int(details[0][0][1]) # second zero represents which pair of (x,y) points
#         w = int(details[0][1][0])-x #third zero represents x or y
#         h = int(details[0][2][1])-y
#         words = details[1].split()
#         misspelled = spell.unknown(words)
#         corrected_text = ' '.join(spell.correction(word) for word in words)
#         print(f"Word: {corrected_text}")