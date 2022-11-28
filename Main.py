import keyboard
import time
import numpy as np
import cv2
from PIL import ImageGrab


class Main:

    img_width = 0
    img_height = 0
    save_img_id = 0
    white_threshold = 243

    def get_corner_point(self, img, x1, x2, y1, y2):

        row_move = True
        newImg = img.copy()

        array_y = []
        array_x = []

        if x1 < x2 and y1 < y2:
            if x2 > y2:
                row_move = False

            array_x = list(range(x1, x2))
            array_y = list(range(y1, y2))
        else:
            if x1 > y1:
                row_move = False
            array_x = list(range(x1 - 1, x2 - 1, -1))
            array_y = list(range(y1 - 1, y2 - 1, -1))

        blank_count = 0
        for i in array_x:
            blank_count = blank_count + 1
            for j in array_y:
                if row_move:
                    x = i
                    y = j
                else:
                    x = j
                    y = i

                if (img[x, y] > self.white_threshold):
                    newImg[x, y] = 0

                else:
                    cv2.imwrite(f'test_{self.save_img_id}.png', newImg)
                    self.save_img_id = self.save_img_id + 1

                    return blank_count

        return blank_count

    def get_4corner_point(self, img):
        upper_x = 0
        upper_y = 0

        lower_x = 0
        lower_y = 0

        upper_x = self.get_corner_point(img, 0, self.img_width,
                                        0, self.img_height)

        upper_y = self.get_corner_point(img, 0, self.img_height,
                                        0, self.img_width)

        lower_x = self.get_corner_point(img,  self.img_width, 0,
                                        self.img_height, 0)

        lower_y = self.get_corner_point(img,  self.img_height, 0,
                                        self.img_width, 0)

        print("upper_x, upper_y, lower_x, lower_y: ",
              [upper_x, upper_y, lower_x, lower_y])

        return upper_x, upper_y, lower_x, lower_y

    def get_windows_info(self):
        for m in get_monitors():
            self.img_width = m.width
            self.img_height = m.height

            break

    def read_img(self, path):
        img = cv2.imread(path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        self.img_width = img_gray.shape[1]
        self.img_height = img_gray.shape[0]

        return img_gray

    def capture_windows(self):
        img_rgb = ImageGrab.grab()
        img_gray = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2GRAY)
        pixel_sum = 0

        x = 0
        y = 0

        w = self.img_width
        h = self.img_height

        crop_img = img_gray[y:y+h, x:x+w]

        for img_arr in crop_img:
            for value in img_arr:
                pixel_sum = pixel_sum + value

        print(pixel_sum)

        return crop_img

    def next_page(self):
        keyboard.press_and_release('right')

    def copy_all_page(self):
        process_count = 0
        while process_count < 400:

            keyboard.press_and_release('f5')
            print("f5")
            time.sleep(1)

            keyboard.press_and_release('right')
            print("right")

            time.sleep(2)
            process_count = process_count + 1

    def capture_img(self, img, x, y, w, h):

        crop_img = img[y:h, x:w]
        cv2.imwrite(f'test_crop.png', crop_img)

        return crop_img

    def draw_edge(self, img, upper_x, upper_y, lower_x, lower_y):

        cv2.line(img, (upper_x, upper_y),
                 (main.img_width - lower_x, upper_y), (0, 0, 0), 2)
        cv2.line(img, (upper_x, upper_y),
                 (upper_x, main.img_height - lower_y), (0, 0, 0), 2)

        cv2.line(img, (main.img_width - lower_x, main.img_height - lower_y),
                 (upper_x, main.img_height - lower_y), (0, 0, 0), 2)

        cv2.line(img, (main.img_width - lower_x, main.img_height - lower_y),
                 (main.img_width - lower_x, upper_y), (0, 0, 0), 2)

        cv2.imwrite(f'test_line.png', img)

        return img


if __name__ == '__main__':

    img_path = "test/1.png"

    main = Main()

    main.get_windows_info()

    img = main.read_img(img_path)
    upper_x, upper_y, lower_x, lower_y = main.get_4corner_point(img)
    crop_img = main.capture_img(
        img, upper_x, upper_y, main.img_width - lower_x,  main.img_height - lower_y)

    edge_img = main.draw_edge(img, upper_x, upper_y, lower_x, lower_y)

    exit()

    if keyboard.read_key() == "p":
        print("Screen capture starting.")

        while True:
            # img = main.capture_windows()

            break
            time.sleep(2)
            main.next_page()
            time.sleep(1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
