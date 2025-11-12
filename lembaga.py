# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class lembaga(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file = QFile("lembaga.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formLembaga = loader.load(ui_file, self)
        ui_file.close()
        self.crud = my_cruddb()
        self.formLembaga.btnSimpan.clicked.connect(self.doSimpanLembaga)
        self.formLembaga.btnUbah.clicked.connect(self.doUbahLembaga)
        self.formLembaga.btnHapus.clicked.connect(self.doHapusLembaga)
        self.tampilData()
        self.formLembaga.editCari.textChanged.connect(self.doCariLembaga)


    def doSimpanLembaga(self):

        if not self.formLembaga.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Lembaga belum di isi")
            self.formLembaga.editID.setFocus()
        elif not self.formLembaga.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Lembaga belum di isi")
            self.formLembaga.editNama.setFocus()
        elif not self.formLembaga.editJenis.text().strip():
            QMessageBox.information(None,"Informasi","Jenis Lembaga belum di isi")
            self.formLembaga.editJenis.setFocus()
        elif not self.formLembaga.editNegara.text().strip():
            QMessageBox.information(None,"Informasi","Negara belum di isi")
            self.formLembaga.editNegara.setFocus()
        elif not self.formLembaga.editDeskripsi.toPlainText().strip():
            QMessageBox.information(None,"Informasi","Deskripsi belum di isi")
            self.formLembaga.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                tempID = self.formLembaga.editID.text()
                tempNama = self.formLembaga.editNama.text()
                tempJenis = self.formLembaga.editJenis.text()
                tempNegara = self.formLembaga.editNegara.text()
                tempDeskripsi = self.formLembaga.editDeskripsi.toPlainText()
                self.crud.simpanLembaga(tempID, tempNama, tempJenis, tempNegara, tempDeskripsi)
                self.tampilData()
            else:
                pass

    def doUbahLembaga(self):
        if not self.formLembaga.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Lembaga belum di isi. Klik data dari tabel.")
            self.formLembaga.editID.setFocus()
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Apakah Anda Yakin Mengubah Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formLembaga.editID.text()
                tempNama = self.formLembaga.editNama.text()
                tempJenis = self.formLembaga.editJenis.text()
                tempNegara = self.formLembaga.editNegara.text()
                tempDeskripsi = self.formLembaga.editDeskripsi.toPlainText()
                self.crud.ubahLembaga(tempID, tempNama, tempJenis, tempNegara, tempDeskripsi)
                self.tampilData()
            else:
                pass


    def doHapusLembaga(self):
        if not self.formLembaga.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Lembaga belum di isi. Klik data dari tabel.")
            self.formLembaga.editID.setFocus()
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Apakah Anda Yakin Menghapus Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formLembaga.editID.text()
                self.crud.hapusLembaga(tempID)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilData(self):
        baris = self.crud.dataLembaga()
        self.formLembaga.tabelLembaga.setRowCount(0)
        for r in baris:
            i = self.formLembaga.tabelLembaga.rowCount()
            self.formLembaga.tabelLembaga.insertRow(i)
            self.formLembaga.tabelLembaga.setItem(i,0, QTableWidgetItem(r ["id_lembaga"]))
            self.formLembaga.tabelLembaga.setItem(i,1, QTableWidgetItem(r ["nama"]))
            self.formLembaga.tabelLembaga.setItem(i,2, QTableWidgetItem(r ["jenis"]))
            self.formLembaga.tabelLembaga.setItem(i,3, QTableWidgetItem(r ["negara"]))
            self.formLembaga.tabelLembaga.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))

    def doCariLembaga(self):
        cari = self.formLembaga.editCari.text()
        baris = self.crud.CariLembaga(cari)
        self.formLembaga.tabelLembaga.setRowCount(0)
        for r in baris:
            i = self.formLembaga.tabelLembaga.rowCount()
            self.formLembaga.tabelLembaga.insertRow(i)
            self.formLembaga.tabelLembaga.setItem(i,0, QTableWidgetItem(r ["id_lembaga"]))
            self.formLembaga.tabelLembaga.setItem(i,1, QTableWidgetItem(r ["nama"]))
            self.formLembaga.tabelLembaga.setItem(i,2, QTableWidgetItem(r ["jenis"]))
            self.formLembaga.tabelLembaga.setItem(i,3, QTableWidgetItem(r ["negara"]))
            self.formLembaga.tabelLembaga.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))


