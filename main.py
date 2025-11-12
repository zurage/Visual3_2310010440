import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from lembaga import lembaga
from strategi import strategi
from admin import admin
from program import program
from regulasi import regulasi


class halamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # variabel untuk menampung file main.ui
        fileformutama = QFile("main.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        fileformutama.open(QFile.ReadOnly)
        # membuat objek loader Ui
        formloader = QUiLoader()
        self.formutama = formloader.load(fileformutama,self)
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())
        self.formutama.actionLembaga.triggered.connect(self.bukalembaga)
        self.formutama.actionStrategi.triggered.connect(self.bukastrategi)
        self.formutama.actionAdmin.triggered.connect(self.bukaadmin)
        self.formutama.actionProgram.triggered.connect(self.bukaprogram)
        self.formutama.actionRegulasi.triggered.connect(self.bukaregulasi)

    def bukalembaga(self):
        self.formlembaga = lembaga()
        self.formlembaga.show()

    def bukastrategi(self):
        self.formstrategi = strategi()
        self.formstrategi.show()

    def bukaadmin(self):
        self.formadmin = admin()
        self.formadmin.show()

    def bukaprogram(self):
         self.formprogram = program()
         self.formprogram.show()

    def bukaregulasi(self):
        self.formregulasi = regulasi()
        self.formregulasi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = halamanUtama()
    widget.show()
    sys.exit(app.exec())
