# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class regulasi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file = QFile("regulasi.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formRegulasi = loader.load(ui_file, self)
        ui_file.close()
        self.crud = my_cruddb()
        self.formRegulasi.btnSimpan.clicked.connect(self.doSimpanRegulasi)
        self.formRegulasi.btnUbah.clicked.connect(self.doUbahRegulasi)
        self.formRegulasi.btnHapus.clicked.connect(self.doHapusRegulasi)
        self.tampilData()
        self.formStrategi.editCari.textChanged.connect(self.doCariRegulasi)

    def doSimpanRegulasi(self):
        if not self.formRegulasi.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Regulasi belum di isi")
            self.formRegulasi.editID.setFocus()
        elif not self.formRegulasi.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Regulasi belum di isi")
            self.formRegulasi.editNama.setFocus()
        elif not self.formRegulasi.editNomor.text().strip():
            QMessageBox.information(None, "Informasi", "Nomor Regulasi belum di isi")
            self.formRegulasi.editNomor.setFocus()
        elif not self.formRegulasi.editDeskripsi.toPlainText().strip():
            QMessageBox.information(None, "Informasi", "Deskripsi Regulasi belum di isi")
            self.formRegulasi.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                tempID = self.formRegulasi.editID.text()
                tempNama = self.formRegulasi.editNama.text()
                tempNomor = self.formRegulasi.editNomor.text()
                tempTahun = self.formRegulasi.editTahun.date().toString("yyyy-MM-dd")
                tempDeskripsi = self.formRegulasi.editDeskripsi.toPlainText()
                self.crud.simpanRegulasi(tempID, tempNama, tempNomor, tempTahun, tempDeskripsi)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass


    def doUbahRegulasi(self):
        if not self.formRegulasi.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Regulasi belum di isi. (Klik data dari tabel)")
            self.formRegulasi.editID.setFocus()
        return
        pesan = QMessageBox.question(None, "Konfirmasi Ubah","Apakah Anda Yakin Mengubah Data Ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            tempID = self.formRegulasi.editID.text()
            tempNama = self.formRegulasi.editNama.text()
            tempNomor = self.formRegulasi.editNomor.text()
            tempTahun = self.formRegulasi.editTahun.date().toString("yyyy-MM-dd")
            tempDeskripsi = self.formRegulasi.editDeskripsi.toPlainText()
            self.crud.ubahRegulasi(tempID, tempNama, tempNomor, tempTahun, tempDeskripsi)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data Berhasil di Ubah")
        else:
            pass


    def doHapusRegulasi(self):
        tempID = self.formRegulasi.editID.text()
        if not tempID:
            QMessageBox.information(None, "Informasi", "ID Regulasi belum di isi. (Klik data dari tabel)")
            self.formRegulasi.editID.setFocus()
        return
        pesan = QMessageBox.question(None, "Konfirmasi Hapus","Apakah Anda Yakin Menghapus ID: {tempID}?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            self.crud.hapusRegulasi(tempID)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        else:
            pass


    def tampilData(self):
        baris = self.crud.dataRegulasi()
        self.formRegulasi.tabelRegulasi.setRowCount(0)
        for r in baris:
            i = self.formRegulasi.tabelRegulasi.rowCount()
            self.formRegulasi.tabelRegulasi.insertRow(i)
            self.formRegulasi.tabelRegulasi.setItem(i,0, QTableWidgetItem(r ["id_regulasi"]))
            self.formRegulasi.tabelRegulasi.setItem(i,1, QTableWidgetItem(r ["nama"]))
            self.formRegulasi.tabelRegulasi.setItem(i,2, QTableWidgetItem(r ["nomor"]))
            self.formRegulasi.tabelRegulasi.setItem(i,3, QTableWidgetItem(str(r ["tahun"])))
            self.formRegulasi.tabelRegulasi.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))


    def doCariRegulasi(self):
            cari = self.formRegulasi.editCari.text()
            baris = self.crud.CariRegulasi(cari)
            self.formRegulasi.tabelRegulasi.setRowCount(0)
            for r in baris:
                i = self.formRegulasi.tabelRegulasi.rowCount()
                self.formRegulasi.tabelRegulasi.insertRow(i)
                self.formRegulasi.tabelRegulasi.setItem(i,0, QTableWidgetItem(r ["id_regulasi"]))
                self.formRegulasi.tabelRegulasi.setItem(i,1, QTableWidgetItem(r ["nama"]))
                self.formRegulasi.tabelRegulasi.setItem(i,2, QTableWidgetItem(r ["nomor"]))
                self.formRegulasi.tabelRegulasi.setItem(i,3, QTableWidgetItem(str(r ["tahun"])))
                self.formRegulasi.tabelRegulasi.setItem(i,4, QTableWidgetItem(r ["deskripsi"]))

