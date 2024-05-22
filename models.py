from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Petani(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200))
    telepon = db.Column(db.String(15))

class Lahan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_petani = db.Column(db.Integer, db.ForeignKey('petani.id'), nullable=False)
    lokasi = db.Column(db.String(100))
    tanggal_tanam = db.Column(db.Date)
    varietas = db.Column(db.String(50))
    jumlah_bibit = db.Column(db.Integer)
    luas_lahan = db.Column(db.Float)
