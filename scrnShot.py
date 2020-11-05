import pyautogui
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#region parameter: left, top, top, width, height
screenshot = pyautogui.screenshot(region = (600,0,400,100))
screenshot.save("screen.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

health = pytesseract.image_to_string(Image.open('screen.png'))#.strip()


#health = health[-5:].strip(" ")

print(health)
f1 = open("health.txt", "w")
f1.write(health)