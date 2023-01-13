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

        self.button_add_file_1 = QtWidgets.QPushButton(self)
        self.button_add_file_1.setFont(self.font_in_label)
        self.button_add_file_1.setText("Добавить первый файл")
        self.button_add_file_1.setGeometry(
            100, 70, self.button_size_x, int(self.button_size_y))

        self.button_add_file_2 = QtWidgets.QPushButton(self)
        self.button_add_file_2.setFont(self.font_in_label)
        self.button_add_file_2.setText("Добавить второй файл")
        self.button_add_file_2.setGeometry(
            900 - self.button_size_x, 70, self.button_size_x, int(self.button_size_y))

        self.label_show_file_1 = QLabel(self)
        self.label_line_file_1 = QLineEdit(self)
        self.label_line_file_1.setGeometry(100, 150, self.button_size_x, 25)

        self.label_show_file_2 = QLabel(self)
        self.label_line_file_2 = QLineEdit(self)
        self.label_line_file_2.setGeometry(
            900 - self.button_size_x, 150, self.button_size_x, 25)

        self.button_add_file_1.clicked.connect(self.set_file)

    def set_file(self) -> None:
        pass


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
