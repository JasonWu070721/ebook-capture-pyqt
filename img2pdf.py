from PIL import Image
import os
import re


def get_file_name(file_all_name):
    split_file =  os.path.splitext(file_all_name)
    file_name = split_file[0].zfill(5)

    return file_name

def sort_file_name(files):
    files.sort(key=get_file_name)
    return files
    
def combine_imgs_pdf(folder_path, pdf_file_path):

    files = os.listdir(folder_path)
    # print(files)
    files = sort_file_name(files)

    png_files = []
    sources = []
    for file in files:
        if 'png' in file or 'jpg' in file:
            print(file)
            png_files.append(os.path.join(folder_path, file))
    output = Image.open(png_files[0])
    png_files.pop(0)
    for file in png_files:
        png_file = Image.open(file)
        if png_file.mode == "RGB":
            png_file = png_file.convert("RGB")
        sources.append(png_file)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)
    
if __name__ == "__main__":
    
    boot_name = "5分鐘征服英文法 [有聲書]"
    
    root_path = "G:/我的雲端硬碟/課程/英文/文法"
    folder = os.path.join(root_path, boot_name)
    pdfFile = os.path.join(root_path, f"{boot_name}.pdf")
    combine_imgs_pdf(folder, pdfFile)