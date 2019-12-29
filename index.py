import os,shutil
from PIL import Image
import pytesseract
import sys







usr_txt = None
img_directory = "C:/Users/Angular_Nija_Avenger/Desktop/Content"
img_txt_directory = "C:/Users/Angular_Nija_Avenger/Desktop/Content/txt_content"


who = input('who is running ? (\'dev/dm\'): ')
print(who)
if who == 'dev':
    img_directory+='/dev/'
    img_txt_directory+='/dev/'
if who == 'dm':
    img_directory+='/dm/' 
    img_txt_directory+='/dm/'





def rename_img(img):
    for index,file in enumerate(img):
        old =img_directory + file
        new = img_directory + str(index) + '.png'
        os.rename(old,new)
        image_txt = get_img_txt(new);
        write_img_txt_to_directory(image_txt,index)
    return True

def get_img_txt(img):
    try:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        return pytesseract.image_to_string(Image.open(img),lang='eng')
    except:
        return "not an image"

def write_img_txt_to_directory(txt,index):
    txt_file = img_txt_directory + str(index) + '.txt'
    print(txt_file)
    print("text file")
    opened_file = open(txt_file,'w')
    opened_file.write(txt)
    opened_file.close()
    pass
def get_list_of_images():
    images = []
    for fn,subfn,file in os.walk(img_directory):
        images = file
        break
    return images

def main():
    print("main is running")
    images = get_list_of_images()
    rename_img(images)
    pass

main()













