# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'visual3_2310010440'
        )

    def simpanLembaga(self, id, nama, jenis, negara, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("insert into lembaga (id_Lembaga, nama, jenis, negara, deskripsi) value(%s,%s,%s,%s,%s)",(id, nama, jenis, negara, deskripsi))
        self.conn.commit()
        alamat.close()


    def ubahLembaga(self, id, nama, jenis, negara, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE lembaga SET nama=%s, jenis=%s, negara=%s, deskripsi=%s WHERE id_lembaga=%s",(nama, jenis, negara, deskripsi, id))
        self.conn.commit()
        alamat.close()

    def hapusLembaga(self, id):
        alamat = self.conn.cursor()
        alamat.execute("delete from lembaga where id_lembaga=%s",(id,))
        self.conn.commit()
        alamat.close()

    def dataLembaga(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from lembaga order by id_lembaga asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariLembaga(self,param):
        sql = "select * from lembaga where id_lembaga like %s or nama like %s or jenis like %s or negara like %s or deskripsi like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record



    def simpanProgram(self, id, nama, jenis, tahun, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO program (id_program, nama, jenis, tahun_mulai, deskripsi) VALUES (%s, %s, %s, %s, %s)", (id, nama, jenis, tahun, deskripsi))
        self.conn.commit()
        alamat.close()


    def ubahProgram(self, id, nama, jenis, tahun, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE program SET nama=%s, jenis=%s, tahun_mulai=%s, deskripsi=%s WHERE id_program=%s",(nama, jenis, tahun, deskripsi, id))
        self.conn.commit()
        alamat.close()


    def hapusProgram(self, id):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM program WHERE id_program=%s",(id,))
        self.conn.commit()
        alamat.close()

    def dataProgram(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from program order by id_program asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariProgram(self,param):
        sql = "select * from program where id_program like %s or nama like %s or jenis like %s or tahun_mulai like %s or deskripsi like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanAdmin(self, id, user, password, nama):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO Admin (id_admin, username, password, nama_lengkap) VALUES (%s, %s, %s, %s)",(id, user, password, nama))
        self.conn.commit()
        alamat.close()


    def ubahAdmin(self, id, user, password, nama):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE admin SET username=%s, password=%s, nama_lengkap=%s WHERE id_admin=%s",(user, password, nama, id))
        self.conn.commit()
        alamat.close()


    def hapusAdmin(self, id):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM admin WHERE id_admin=%s",(id,))
        self.conn.commit()
        alamat.close()


    def simpanRegulasi(self, id, nama, nomor, tahun, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO regulasi (id_regulasi, nama, nomor, tahun, deskripsi) VALUES (%s, %s, %s, %s, %s)",(id, nama, nomor, tahun, deskripsi))
        self.conn.commit()
        alamat.close()


    def ubahRegulasi(self, id, nama, nomor, tahun, deskripsi):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE regulasi SET nama=%s, nomor=%s, tahun=%s, deskripsi=%s WHERE id_reg=%s",(nama, nomor, tahun, deskripsi, id))
        self.conn.commit()
        alamat.close()

    def hapusRegulasi(self, id):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM regulasi WHERE id_reg=%s",(id,))
        self.conn.commit()
        alamat.close()

    def dataRegulasi(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from regulasi order by id_regulasi asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariRegulasi(self,param):
        sql = "select * from regulasi where id_regulasi like %s or nama like %s or nomor like %s or tahun like %s or deskripsi like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanStrategi(self, id, id_reg, judul, tujuan):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO strategi (id_strategi, id_regulasi, judul, tujuan) VALUES (%s, %s, %s, %s)",(id, id_reg, judul, tujuan))
        self.conn.commit()
        alamat.close()


    def ubahStrategi(self, id, id_reg, judul, tujuan):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE strategi SET id_regulasi=%s, judul=%s, tujuan=%s WHERE id_strategi=%s",(id_reg, judul, tujuan, id))
        self.conn.commit()
        alamat.close()


    def hapusStrategi(self, id):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM strategi WHERE id_strategi=%s",(id,))
        self.conn.commit()
        alamat.close()


    def dataStrategi(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from strategi order by id_strategi asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariStrategi(self,param):
        sql = "select * from strategi where id_strategi like %s or id_regulasi like %s or judul like %s or tujuan like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record
