# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class admin(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file = QFile("admin.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formAdmin = loader.load(ui_file, self)
        ui_file.close()
        self.crud = my_cruddb()
        self.formAdmin.btnSimpan.clicked.connect(self.doSimpanAdmin)
        self.formAdmin.btnUbah.clicked.connect(self.doUbahAdmin)
        self.formAdmin.btnHapus.clicked.connect(self.doHapusAdmin)


    def doSimpanAdmin(self):
        tempID = self.formAdmin.editID.text()
        tempUser = self.formAdmin.editUser.text()
        tempPass = self.formAdmin.editPassword.text()
        tempNamaLengkap = self.formAdmin.editNama.text()
        self.crud.simpanAdmin(tempID, tempUser, tempPass, tempNamaLengkap)

    def doUbahAdmin(self):
        tempID = self.formAdmin.editID.text()
        tempUser = self.formAdmin.editUser.text()
        tempPass = self.formAdmin.editPassword.text()
        tempNamaLengkap = self.formAdmin.editNama.text()
        self.crud.ubahAdmin(tempID, tempUser, tempPass, tempNamaLengkap)

    def doHapusAdmin(self):
        tempID = self.formAdmin.editID.text()
        self.crud.hapusAdmin(tempID)
