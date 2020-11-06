import pyautogui
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#normal text mode
#the defect: (0,0,300,50)
#the ironclad: (0,0,330,50)

#big text mode:
#the defect: (0,0,360,50)
#the ironclad: (0,0,360,50)


#region parameter: left, top, top, width, height
screenshot = pyautogui.screenshot(region = (0,0,360,50))
screenshot.save("screen.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

health = pytesseract.image_to_string(Image.open('screen.png')).strip()


health = health[-5:].strip(" ")

print(health)
f1 = open("health.txt", "w")
f1.write(health)