from PIL import Image
import os
import re


class Img2Pdf:

    def get_file_name(self, file_all_name):
        split_file = os.path.splitext(file_all_name)
        file_name = split_file[0].zfill(5)

        return file_name

    def sort_file_name(self, files):
        files.sort(key=self.get_file_name)
        return files

    def combine_imgs_pdf(self, folder_path, pdf_file_path):

        files = os.listdir(folder_path)
        # print(files)
        files = self.sort_file_name(files)

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

    def get_all_book_name(self, root_path):
        books = os.listdir(root_path)
        book_names = []
        for book in books:
            if os.path.isdir(os.path.join(root_path, book)):
                book_names.append(book)
        return book_names


if __name__ == "__main__":

    img2Pdf = Img2Pdf()

    root_path = "G:/我的雲端硬碟/課程/英文/閱讀"

    boot_name_list = img2Pdf.get_all_book_name(root_path)

    for boot_name in boot_name_list:
        print(boot_name)

        folder = os.path.join(root_path, boot_name)
        pdfFile = os.path.join(root_path, f"{boot_name}.pdf")
        img2Pdf.combine_imgs_pdf(folder, pdfFile)
