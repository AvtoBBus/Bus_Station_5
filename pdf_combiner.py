from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon

from PyPDF2 import PdfMerger

import sys
import os


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.path_to_get_origin = os.path.abspath("origin")
        self.path_to_save = ""
        self.file_was_checked = False
        self.list_file = []
        self.font_in_label = QFont("Times", 12)
        self.button_size_x = 280
        self.button_size_y = self.button_size_x / 4
        self.border_style = "border-style: outset; border-width: 3px; border-radius: 10px;"

        while self.path_to_save == "":
            if not os.path.isfile("config.txt"):
                while self.path_to_save == "":
                    self.path_to_save = QtWidgets.QFileDialog.getExistingDirectory(
                        self, 'Выберите путь сохранения')
                    with open("config.txt", "w", encoding="utf-8") as f:
                        f.write(str(self.path_to_save))
            else:
                with open("config.txt", "r", encoding="utf-8") as f:
                    self.path_to_save = f.read()
            if self.path_to_save == "":
                os.remove("config.txt")

        self.setWindowTitle("Объединение PDF")
        self.setFixedSize(1000, 500)
        self.move(320, 180)

        self.label_path_to_save = QLabel(self)
        self.label_path_to_save.setFont(self.font_in_label)
        self.label_path_to_save.setText(
            "Папка для сохранения: " + self.path_to_save)
        self.x_coord = int(340 - (len(self.path_to_save) + 22) / 2)
        if self.x_coord % 2 == 1:
            self.x_coord -= 1
        self.label_path_to_save.move(self.x_coord, 10)
        self.label_path_to_save.adjustSize()

        self.label_list_file = QLabel(self)
        self.label_list_file.setFont(self.font_in_label)
        self.label_list_file.move(100, 200)

        self.label_file_merged = QLabel(self)
        self.label_file_merged.setFont(self.font_in_label)
        self.label_file_merged.move(600, 50)

        self.button_check_file = QtWidgets.QPushButton(self)
        self.button_check_file.setFont(self.font_in_label)
        self.button_check_file.setText("Проверить папку с файлами")
        self.button_check_file.setStyleSheet(
            f"background: rgb(240, 230, 140); {self.border_style}")
        self.button_check_file.setGeometry(
            100, 70, self.button_size_x, int(self.button_size_y))

        self.button_start_merge = QtWidgets.QPushButton(self)
        self.button_start_merge.setFont(self.font_in_label)
        self.button_start_merge.setText("Объединить файлы")
        self.button_start_merge.setStyleSheet(
            f"background: rgb(178, 34, 34); {self.border_style}")
        self.button_start_merge.setGeometry(
            600, 70, self.button_size_x, int(self.button_size_y))

        self.button_repeat = QtWidgets.QPushButton(self)
        self.button_repeat.setFont(self.font_in_label)
        self.button_repeat.setText("Сбросить файлы")
        self.button_repeat.setStyleSheet(
            f"background: rgb(178, 34, 34); {self.border_style}")
        self.button_repeat.setGeometry(
            600, 150, self.button_size_x, int(self.button_size_y))

        self.button_set_new_path_to_save = QtWidgets.QPushButton(self)
        self.button_set_new_path_to_save.setFont(self.font_in_label)
        self.button_set_new_path_to_save.setText(
            "Выбрать новый путь для сохранения")
        self.button_set_new_path_to_save.setStyleSheet(
            f"background: rgb(240, 230, 140); {self.border_style}; padding: 5px")
        self.button_set_new_path_to_save.move(10, 5)
        self.button_set_new_path_to_save.adjustSize()

        self.button_check_file.clicked.connect(self.check_file)
        self.button_start_merge.clicked.connect(self.start_merge)
        self.button_repeat.clicked.connect(self.clear_and_repeat)
        self.button_set_new_path_to_save.clicked.connect(
            self.set_new_path_to_save)

    def check_file(self) -> None:
        self.list_file = os.listdir("origin")
        str_list_file = "Файлы для объединения:\n\n"
        if not len(self.list_file) == 0:
            i = 1
            for elem in self.list_file:
                str_list_file += f"{i}) {elem}\n"
                i += 1
            str_list_file += "\n\n!!  Внимание! В каком порядке здесь расположены файлы  !!\n!!  В таком же они и будут в итоговом  !!"
            self.label_list_file.setText(f"{str_list_file}")
            self.file_was_checked = True
            self.button_start_merge.setStyleSheet(
                f"background: rgb(0, 255, 127); {self.border_style}")
            self.button_repeat.setStyleSheet(
                f"background: rgb(0, 255, 127); {self.border_style}")
        else:
            str_list_file += "Папка \"origin\" пустая("
            self.label_list_file.setText(f"{str_list_file}")
        self.label_list_file.adjustSize()

    def start_merge(self) -> None:
        if self.file_was_checked:
            merger = PdfMerger()
            for file in self.list_file:
                merger.append(f"origin/{file}")
            merger.write(f"{self.path_to_save}/result_merger.pdf")
        self.label_file_merged.setText("Файлы объединены в result_merger.pdf")
        self.label_file_merged.adjustSize()

    def clear_and_repeat(self) -> None:
        self.list_file.clear()
        self.button_start_merge.setStyleSheet(
            f"background: rgb(178, 34, 34); {self.border_style}")
        self.button_repeat.setStyleSheet(
            f"background: rgb(178, 34, 34); {self.border_style}")
        self.label_list_file.clear()
        self.label_file_merged.clear()
        self.file_was_checked = False

    def set_new_path_to_save(self) -> None:
        self.path_to_save = ""
        while self.path_to_save == "":
            self.path_to_save = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Выберите новый путь сохранения')
            with open("config.txt", "w", encoding="utf-8") as f:
                f.write(str(self.path_to_save))
        self.label_path_to_save.setText(
            "Папка для сохранения: " + self.path_to_save)
        self.x_coord = int(350 - (len(self.path_to_save) + 22) / 2)
        self.label_path_to_save.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        "#MainWindow{border-image:url(background.png)}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
