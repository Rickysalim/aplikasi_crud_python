from tkinter import messagebox, ttk
from connector import db, mydb

import tkinter as tk 
from tkinter import *

gui = tk.Tk()

frm = Frame(gui)
frm2 = Frame(gui)

frm.pack(side=tk.LEFT, padx=20)
frm2.pack(side=tk.LEFT, padx=20, pady=20)

labelName = StringVar()
entryName = StringVar()
labelJurusan= StringVar()
entryJurusan = StringVar()
labelAlamat = StringVar()
entryAlamat = StringVar()
labelPerusahaan = StringVar()
entryPerusahaan = StringVar()
labelPicPerusahaan = StringVar()
entryPicPerusahaan= StringVar()
labelAlamatPerusahaan = StringVar()
entryAlamatPerusahaan = StringVar()


# label name
label = Label(frm, textvariable=labelName)
labelName.set("Nama:")
label.grid(row=0, column=1)

# entry name
entry = Entry(frm, textvariable=entryName)
entry.grid(row=0, column=2)


label = Label(frm, textvariable=labelJurusan)
labelJurusan.set("Jurusan:")
label.grid(row=1, column=1)

entry = Entry(frm, textvariable=entryJurusan)
entry.grid(row=1, column=2)

label = Label(frm, textvariable=labelAlamat)
labelAlamat.set("Alamat:")
label.grid(row=2, column=1)

entry = Entry(frm, textvariable=entryAlamat)
entry.grid(row=2, column=2)

label = Label(frm, textvariable=labelPerusahaan)
labelPerusahaan.set("Perusahaan:")
label.grid(row=3, column=1)

entry = Entry(frm, textvariable=entryPerusahaan)
entry.grid(row=3, column=2)

label = Label(frm, textvariable=labelPicPerusahaan)
labelPicPerusahaan.set("Pic Perusahaan:")
label.grid(row=4, column=1)

entry = Entry(frm, textvariable=entryPicPerusahaan)
entry.grid(row=4, column=2)

label = Label(frm, textvariable=labelAlamatPerusahaan)
labelAlamatPerusahaan.set("Alamat Perusahaan:")
label.grid(row=5, column=1)

entry = Entry(frm, textvariable=entryAlamatPerusahaan)
entry.grid(row=5, column=2)




tv = ttk.Treeview(frm2, column=(1,2,3,4,5,6,7), show="headings", height="20")
tv.grid(row=7, column=2)
tv.pack()

tv.heading(1, text="Id")
tv.heading(2, text="Nama")
tv.heading(3, text="Jurusan")
tv.heading(4, text="Alamat")
tv.heading(5, text="Nama Perusahaan")
tv.heading(6, text="Nama Pic Perusahaan")
tv.heading(7, text="Alamat Perusahaan")

def showMagang():
    for item in tv.get_children():
        tv.delete(item)
    sql = "select * from record_data"
    db.execute(sql)
    rows = db.fetchall()
    for i in rows:
       tv.insert('', 'end', values=i)

showMagang()

def onClickRows():
    item = tv.focus()
    values = tv.item(item, 'values')
    entryName.set(values[1])
    entryJurusan.set(values[2])
    entryAlamat.set(values[3])
    entryPerusahaan.set(values[4])
    entryPicPerusahaan.set(values[5])
    entryAlamatPerusahaan.set(values[6])
    

def updateMagang():
    item = tv.focus()
    values = tv.item(item, 'values')
    if entryName.get() == "":
       messagebox.showinfo( "Kesalahan", "Nama Tidak Boleh Kosong")
       return False
    if entryJurusan.get() == "":
       messagebox.showinfo( "Kesalahan", "Jurusan Tidak Boleh Kosong")
       return False
    if entryAlamat.get() == "":
       messagebox.showinfo( "Kesalahan", "Alamat Tidak Boleh Kosong")
       return False
    if entryPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Perusahaan Tidak Boleh Kosong")
       return False
    if entryPicPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Pic Perusahaan Tidak Boleh Kosong")
       return False
    if entryAlamatPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Alamat Perusahaan Tidak Boleh Kosong")
       return False
    sql = "update record_data set nama=%s, jurusan=%s, alamat=%s, nama_perusahaan=%s, nama_PIC_perusahaan=%s, alamat_perusahaan=%s where id=%s"
    val = (entryName.get(), entryJurusan.get(), entryAlamat.get(), entryPerusahaan.get(), entryPicPerusahaan.get(), entryAlamatPerusahaan.get(), values[0])
    db.execute(sql, val)
    mydb.commit()
    reset()
    showMagang()

def deleteMagang():
    item = tv.focus()
    values = tv.item(item, 'values')
    sql = "delete from record_data where id="+values[0]
    db.execute(sql)
    mydb.commit()
    reset()
    showMagang()

def reset():
    entryName.set("")
    entryJurusan.set("")
    entryAlamat.set("")
    entryPerusahaan.set("")
    entryPicPerusahaan.set("")
    entryAlamatPerusahaan.set("")

def insertMagang(): 
    if entryName.get() == "":
       messagebox.showinfo( "Kesalahan", "Nama Tidak Boleh Kosong")
       return False
    if entryJurusan.get() == "":
       messagebox.showinfo( "Kesalahan", "Jurusan Tidak Boleh Kosong")
       return False
    if entryAlamat.get() == "":
       messagebox.showinfo( "Kesalahan", "Alamat Tidak Boleh Kosong")
       return False
    if entryPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Perusahaan Tidak Boleh Kosong")
       return False
    if entryPicPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Pic Perusahaan Tidak Boleh Kosong")
       return False
    if entryAlamatPerusahaan.get() == "":
       messagebox.showinfo( "Kesalahan", "Alamat Perusahaan Tidak Boleh Kosong")
       return False
       
    sql = "insert into record_data(nama, jurusan, alamat, nama_perusahaan, nama_PIC_perusahaan, alamat_perusahaan) values(%s, %s, %s, %s, %s, %s)"
    val = (entryName.get(), entryJurusan.get(), entryAlamat.get(), entryPerusahaan.get(), entryPicPerusahaan.get(), entryAlamatPerusahaan.get())
    db.execute(sql, val)
    mydb.commit()
    reset()
    showMagang()
    
btn = Button(frm, text="Tambah", command=insertMagang)
btn.grid(row=6, column=1)

btn2 = Button(frm, text="Ganti", command=updateMagang)
btn2.grid(row=6, column=2)

btn3 = Button(frm, text="Pilih", command=onClickRows)
btn3.grid(row=6, column=3)

btn4 = Button(frm, text="Hapus", command=deleteMagang)
btn4.grid(row=6, column=4)

gui.title("Magang")
# gui.geometry("650x650")
# gui.resizable(False, False)
