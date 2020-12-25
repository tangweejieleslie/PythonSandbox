import cv2
import pytesseract
import os

# References
# https://stackoverflow.com/questions/42683517/loop-through-folder-in-python-and-open-files-throws-an-error
# https://www.youtube.com/watch?v=6DjFscX4I_c&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

imageFolder = "C:\\Users\\65909\\Documents\\Github\\PythonSandbox\\image processing\\trial-images\\guardian_tales_data"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def get_text(img):
    print(pytesseract.image_to_string(img))

    cv2.imshow('Result', img)
    cv2.waitKey(0)



for filename in os.listdir(imageFolder):
    if filename.endswith('.PNG'):
        image_path = os.path.join(imageFolder, filename)
        print(image_path)
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        get_text(img)




