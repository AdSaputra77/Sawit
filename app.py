# Contoh kode untuk menjalankan aplikasi Flask
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Petani, Lahan
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db.init_app(app)

@app.route('/')
def index():
    return render_template('input_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama_petani = request.form['nama_petani']
    alamat = request.form.get('alamat')
    telepon = request.form.get('telepon')
    lokasi = request.form.get('lokasi')
    tanggal_tanam_str = request.form.get('tanggal_tanam')
    tanggal_tanam = None
    if tanggal_tanam_str:
        tanggal_tanam = datetime.strptime(tanggal_tanam_str, '%Y-%m-%d')
    varietas = request.form.get('varietas')
    jumlah_bibit = request.form.get('jumlah_bibit')
    luas_lahan = request.form.get('luas_lahan')

    # Validate input
    if not all([nama_petani, alamat, telepon, lokasi, tanggal_tanam_str, varietas, jumlah_bibit, luas_lahan]):
        flash('Semua field harus diisi!', 'error')
        return redirect(url_for('index'))

    if jumlah_bibit:
        try:
            jumlah_bibit = int(jumlah_bibit)
        except ValueError:
            flash('Jumlah bibit harus berupa angka!', 'error')
            return redirect(url_for('index'))

    if luas_lahan:
        try:
            luas_lahan = float(luas_lahan)
        except ValueError:
            flash('Luas lahan harus berupa angka!', 'error')
            return redirect(url_for('index'))

    # Proses penyimpanan data ke database menggunakan SQLAlchemy
    petani_baru = Petani(nama=nama_petani, alamat=alamat, telepon=telepon)
    db.session.add(petani_baru)
    db.session.commit()

    # Simpan informasi lahan juga
    lahan_baru = Lahan(id_petani=petani_baru.id, lokasi=lokasi, tanggal_tanam=tanggal_tanam, varietas=varietas, jumlah_bibit=jumlah_bibit, luas_lahan=luas_lahan)
    db.session.add(lahan_baru)
    db.session.commit()

    flash('Data berhasil disimpan!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Buat database jika belum ada
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
