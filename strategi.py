# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class strategi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file = QFile("strategi.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formStrategi = loader.load(ui_file, self)
        ui_file.close()
        self.crud = my_cruddb()
        self.isiComboBoxRegulasi()
        self.formStrategi.btnSimpan.clicked.connect(self.doSimpanStrategi)
        self.formStrategi.btnUbah.clicked.connect(self.doUbahStrategi)
        self.formStrategi.btnHapus.clicked.connect(self.doHapusStrategi)
        self.tampilData()
        self.formStrategi.editCari.textChanged.connect(self.doCariStrategi)

    def isiComboBoxRegulasi(self):
        data_regulasi = self.crud.dataRegulasi()
        self.formStrategi.comboBox.clear()
        if data_regulasi:
            for regulasi in data_regulasi:
                teks_tampilan = str(regulasi["id_regulasi"])
                data_id = regulasi["id_regulasi"]
                self.formStrategi.comboBox.addItem(teks_tampilan, data_id)

    def doSimpanStrategi(self):
        if not self.formStrategi.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Strategi belum di isi")
            self.formStrategi.editID.setFocus()
        elif not self.formStrategi.editNomor.text().strip():
            QMessageBox.information(None, "Informasi", "Judul Strategi belum di isi")
            self.formStrategi.editNomor.setFocus()
        elif not self.formStrategi.comboBox.currentData():
            QMessageBox.information(None, "Informasi", "Regulasi belum dipilih")
            self.formStrategi.comboBox.setFocus()
        elif not self.formStrategi.editDeskripsi.toPlainText().strip():
            QMessageBox.information(None, "Informasi", "Tujuan Strategi belum di isi")
            self.formStrategi.editDeskripsi.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                tempID = self.formStrategi.editID.text()
                tempJudul = self.formStrategi.editNomor.text()
                tempTujuan = self.formStrategi.editDeskripsi.toPlainText()
                tempRegulasi = self.formStrategi.comboBox.currentData()
                self.crud.simpanStrategi(tempID, tempRegulasi, tempJudul, tempTujuan)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass


    def doUbahStrategi(self):
        f not self.formStrategi.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Strategi belum di isi. (Klik data dari tabel)")
            self.formStrategi.editID.setFocus()
            return
        pesan = QMessageBox.question(None, "Konfirmasi Ubah","Apakah Anda Yakin Mengubah Data Ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            tempID = self.formStrategi.editID.text()
            tempJudul = self.formStrategi.editNomor.text()
            tempTujuan = self.formStrategi.editDeskripsi.toPlainText()
            tempRegulasi = self.formStrategi.comboBox.currentData()
            self.crud.ubahStrategi(tempID, tempRegulasi, tempJudul, tempTujuan)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data Berhasil di Ubah")
        else:
            pass


    def doHapusStrategi(self):
        tempID = self.formStrategi.editID.text()
        if not tempID:
            QMessageBox.information(None, "Informasi", "ID Strategi belum di isi. (Klik data dari tabel)")
            self.formStrategi.editID.setFocus()
            return
        pesan = QMessageBox.question(None, "Konfirmasi Hapus" f"Apakah Anda Yakin Menghapus ID: {tempID}?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            self.crud.hapusStrategi(tempID)
            self.tampilData()
            QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        else:
            pass

    def tampilData(self):
        baris = self.crud.dataStrategi()
        self.formStrategi.tabelStrategi.setRowCount(0)
        for r in baris:
            i = self.formStrategi.tabelStrategi.rowCount()
            self.formStrategi.tabelStrategi.insertRow(i)
            self.formStrategi.tabelStrategi.setItem(i,0, QTableWidgetItem(r ["id_strategi"]))
            self.formStrategi.tabelStrategi.setItem(i,1, QTableWidgetItem(r ["id_regulasi"]))
            self.formStrategi.tabelStrategi.setItem(i,2, QTableWidgetItem(r ["judul"]))
            self.formStrategi.tabelStrategi.setItem(i,3, QTableWidgetItem(r ["tujuan"]))
