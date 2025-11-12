# This Python file uses the following encoding: utf-8

import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class program(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file = QFile("program.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formProgram = loader.load(ui_file, self)
        ui_file.close()
        self.crud = my_cruddb()
        self.formProgram.btnSimpan.clicked.connect(self.doSimpanProgram)
        self.formProgram.btnUbah.clicked.connect(self.doUbahProgram)
        self.formProgram.btnHapus.clicked.connect(self.doHapusProgram)
        self.tampilData()
        self.formProgram.editCari.textChanged.connect(self.doCariProgram)

    def doSimpanProgram(self):

        if not self.formProgram.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Program belum di isi")
            self.formProgram.editID.setFocus()
        elif not self.formProgram.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Program belum di isi")
            self.formProgram.editNama.setFocus()
        elif not self.formProgram.editJenis.text().strip():
            QMessageBox.information(None, "Informasi", "Jenis Program belum di isi")
            self.formProgram.editJenis.setFocus()
        elif not self.formProgram.editDeskripsi.toPlainText().strip():
            QMessageBox.information(None, "Informasi", "Deskripsi Program belum di isi")
            self.formProgram.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan", "Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                tempID = self.formProgram.editID.text()
                tempNama = self.formProgram.editNama.text()
                tempJenis = self.formProgram.editJenis.text()
                tempTahun = self.formProgram.editTahun.date().toString("yyyy-MM-dd")
                tempDeskripsi = self.formProgram.editDeskripsi.toPlainText()
                self.crud.simpanProgram(tempID, tempNama, tempJenis, tempTahun, tempDeskripsi)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahProgram(self):   
        if not self.formProgram.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Program belum di isi. (Klik data dari tabel)")
            self.formProgram.editID.setFocus()
            return
            pesan = QMessageBox.question(None, "Konfirmasi Ubah","Apakah Anda Yakin Mengubah Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formProgram.editID.text()
                tempNama = self.formProgram.editNama.text()
                tempJenis = self.formProgram.editJenis.text()
                tempTahun = self.formProgram.editTahun.date().toString("yyyy-MM-dd")
                tempDeskripsi = self.formProgram.editDeskripsi.toPlainText()
                self.crud.ubahProgram(tempID, tempNama, tempJenis, tempTahun, tempDeskripsi)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Ubah")
            else:
                pass

    def doHapusProgram(self):

        tempID = self.formProgram.editID.text()
        if not tempID:
            QMessageBox.information(None, "Informasi", "ID Program belum di isi. (Klik data dari tabel)")
            self.formProgram.editID.setFocus()
            return
            pesan = QMessageBox.question(None, "Konfirmasi Hapus", "Apakah Anda Yakin Menghapus ID: {tempID}?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                self.crud.hapusProgram(tempID)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilData(self):
        baris = self.crud.dataProgram()
        self.formProgram.tabelProgram.setRowCount(0)
        for r in baris:
            i = self.formProgram.tabelProgram.rowCount()
            self.formProgram.tabelProgram.insertRow(i)
            self.formProgram.tabelProgram.setItem(i,0, QTableWidgetItem(r ["id_program"]))
            self.formProgram.tabelProgram.setItem(i,1, QTableWidgetItem(r ["nama"]))
            self.formProgram.tabelProgram.setItem(i,2, QTableWidgetItem(r ["jenis"]))
            self.formProgram.tabelProgram.setItem(i,3, QTableWidgetItem(str(r ["tahun_mulai"])))
            self.formProgram.tabelProgram.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))

    def doCariProgram(self):
        cari = self.formProgram.editCari.text()
        baris = self.crud.CariProgram(cari)
        self.formProgram.tabelProgram.setRowCount(0)
        for r in baris:
            i = self.formProgram.tabelProgram.rowCount()
            self.formProgram.tabelProgram.insertRow(i)
            self.formProgram.tabelProgram.setItem(i,0, QTableWidgetItem(r ["id_program"]))
            self.formProgram.tabelProgram.setItem(i,1, QTableWidgetItem(r ["nama"]))
            self.formProgram.tabelProgram.setItem(i,2, QTableWidgetItem(r ["jenis"]))
            self.formProgram.tabelProgram.setItem(i,3, QTableWidgetItem(str(r ["tahun_mulai"])))
            self.formProgram.tabelProgram.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))
