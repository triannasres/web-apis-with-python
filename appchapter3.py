from flask import Flask, jsonify, request
# Inisialisasi aplikasi
app = Flask ( __name__ )

# Mendefinisikan apa yang dilakukan aplikasi
@app.get("/tstChapter3")
def index():
    response = {"data" : "Halo, Dunia!",
                "pesan" : "Ini tugas praktikum materi Flask",
                "nama1" : "David Hugo Triannas",
                "nama2" : "Muhammad Rizky Pratama",
                "nim1" : 18220004,
                "nim2" : 18220110}
    return jsonify(response)