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

def convertPercentage(fraction):
		numerator = 0
		denominator = 0
		splitFraction = fraction.split("/")
		numerator = int(splitFraction[0])
		denominator = int(splitFraction[1])
		percentage = numerator / denominator
		#int gets rid of trailing 0, and * 100 turns it into a whole #
		return(int(round(percentage,2)*100))
#region parameter: left, top, top, width, height
while True:

	screenshot = pyautogui.screenshot(region = (0,0,360,50))
	screenshot.save("screen.png")

	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

	health = pytesseract.image_to_string(Image.open('screen.png')).strip()


	health = health[-5:].strip(" ")

	print(health)


	

	print(convertPercentage(health))

	f1 = open("health.txt", "w")
	f1.write(str(convertPercentage(health)))
	f1.close()

