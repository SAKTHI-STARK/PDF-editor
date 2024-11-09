import img2pdf as i2p
import select_directory as sd
from PIL import Image
global file
#function to get the image files which are converte into pdf
def read_file():
    global file
    file=sd.select_file()
    print(file)
#function to convert single or multiple images to pdf
def convert_img_to_pdf():
    global file
    save_dir=sd.save_file()
    with open(save_dir,'ab') as f:
        page_size = (595, 842)
        f.write(i2p.convert(file,page_size=page_size))
             
            
