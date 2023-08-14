import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import keyboard


def get_keyboard_input():
    while True:  # Loop to capture keys continuously
        event = keyboard.read_event()  # Capture a keyboard event

        if event.name == 'q' and event.event_type == 'down':
            print("Q key was pressed.")
            break
        elif event.event_type == 'down':
            print(f"{event.name} key was pressed")

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    input = QLineEdit(widget)   
    input.setGeometry(20,20,100,20)   
    
    mybutton = QPushButton('button', widget)
    mybutton.move(60, 50)

    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   window()