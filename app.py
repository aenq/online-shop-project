from flask import Flask, render_template, request, url_for, redirect
from models import Pengguna, Keranjang
import pymysql

#
db = pymysql.connect(host="localhost", user="root",
                     password="", database="toko_tembakau")
#
cursor = db.cursor()
#
cursor.execute("SELECT VERSION()")
#
data = cursor.fetchone()
print("Database version : %s" % data)
#
db.close()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    model = Pengguna()
    container = []
    container = model.selectDB()
    return render_template('landingpage.html', container=container)


@app.route('/produk', methods=['GET', 'POST'])
def produk():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('produk.html')


@app.route('/tembakau-original', methods=['GET', 'POST'])
def original():
    if request.method == 'POST':
        return redirect(url_for('original'))
    return render_template('original.html')


@app.route('/keranjang', methods=['GET', 'POST'])
def keranjang():
    model = Keranjang()
    container = []
    container = model.selectDB()
    if request.method == 'POST':
        return redirect(url_for('keranjang'))
    return render_template('keranjang.html', container=container)


@app.route('/form1', methods=['GET', 'POST'])
def daftar():
    if request.method == 'POST':
        return redirect(url_for('produk'))
    return render_template('daftar.html')


@app.route('/form2', methods=['GET', 'POST'])
def form2():
    return render_template('form2.html')


@app.route('/table', methods=['GET', 'POST'])
def table():
    return render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True)
