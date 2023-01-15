from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QThread, QObject

from PyPDF2 import PdfReader, PdfMerger

import sys
import os

# def main():
#     merger = PdfMerger()
#     merger.append("Учебник_1.pdf")
#     merger.append("Учебник_2.pdf")
#     merger.write("result_merger.pdf")


# if __name__ == "__main__":
#     main()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.path_to_get_origin = os.path.abspath("origin")
        self.path_to_save = ""
        self.list_file = []
        self.list_file_path = []
        self.font_in_label = QFont("Times")
        self.button_size_x = 280
        self.button_size_y = self.button_size_x / 4

        if not os.path.isfile("config.txt"):
            while self.path_to_save == "":
                self.path_to_save = QtWidgets.QFileDialog.getExistingDirectory(
                    self, 'Выберите путь сохранения')
                with open("config.txt", "w", encoding="utf-8") as f:
                    f.write(str(self.path_to_save))
        else:
            with open("config.txt", "r", encoding="utf-8") as f:
                self.path_to_save = f.read()

        self.setWindowTitle("Объединение PDF")
        self.setFixedSize(1000, 500)
        self.move(320, 180)

        self.label_pts = QLabel(self)
        self.label_pts.setFont(self.font_in_label)
        self.label_pts.setText("Папка для сохранения: " + self.path_to_save)
        self.x_coord = int(250 - (len(self.path_to_save) + 22) / 2)
        if self.x_coord % 2 == 1:
            self.x_coord -= 1
        self.label_pts.move(self.x_coord, 0)
        self.label_pts.adjustSize()

        self.button_check_file = QtWidgets.QPushButton(self)
        self.button_check_file.setFont(self.font_in_label)
        self.button_check_file.setText("Добавить первый файл")
        self.button_check_file.setGeometry(
            100, 70, self.button_size_x, int(self.button_size_y))

        self.button_check_file.clicked.connect(self.check_file)

    def check_file(self) -> None:
        self.list_of_file


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
