import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTextBrowser


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setStyleSheet('background-color: #32393a')
        self.Title_label.setStyleSheet('color: #fffcff;')
        self.Id_title_label.setStyleSheet('color: #fffcff;')
        self.Id_view_label.setStyleSheet('color: #fffcff;')
        self.Name_title_label.setStyleSheet('color: #fffcff;')
        self.Name_view_label.setStyleSheet('color: #fffcff;')
        self.Degree_title_label.setStyleSheet('color: #fffcff;')
        self.Degree_view_label.setStyleSheet('color: #fffcff;')
        self.Descript_name_label.setStyleSheet('color: #fffcff;')
        self.Price_title_label.setStyleSheet('color: #fffcff;')
        self.Price_view_label.setStyleSheet('color: #fffcff;')
        self.Volume_title_label.setStyleSheet('color: #fffcff;')
        self.Volume_view_label.setStyleSheet('color: #fffcff;')

        self.Id_spinBox.setStyleSheet('background: #466363; color: #fffcff;')

        self.Search_pushButton.clicked.connect(self.run_search)
        self.Search_pushButton.setStyleSheet('background: #466363; color: #fffcff;')

        self.Descript_textBrowser.setStyleSheet('background: #466363; color: #fffcff;')

    def run_search(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
