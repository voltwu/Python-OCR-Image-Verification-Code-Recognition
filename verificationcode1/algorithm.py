from PIL import Image
import pytesseract

def get_verification_code(path):
    #open the image
    image = Image.open(path)
    
    #convert it to grayscale 'L'
    gray_img = image.convert(mode='L')

    #binarization
    threshold = 94.35
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    #map the look up table into the image
    out_img = gray_img.point(lut=table,mode='1')

    custom_oem_psm_config = r'--psm 7'

    #pull the text out of image
    code = pytesseract.image_to_string(out_img, config=custom_oem_psm_config)

    return code
