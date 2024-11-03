import img2pdf as i2p
import select_directory as sd
global file
def read_file():
    global file
    file=sd.select_file()
    with open(file,'r'):
        pass

def convert_img_to_pdf():
    global file
    print(file)
    print(type(file))
    with open(sd.save_file(),'wb') as f:
        page_size = (595, 842)
        f.write(i2p.convert(file,page_size=page_size))
        file.close()
        f.close()

