import tkinter as tk
from tkinter import messagebox


okno = tk.Tk()
okno.title('Izračun delovne dobe in zaslužka')
okno.geometry('750x350')
okno.resizable(width=False, height=False)


inputi = tk.Frame(okno)
outputi = tk.Frame(okno)
gumbi = tk.Frame(okno)

inputi.grid(row=0, column=0)
outputi.grid(row=1, column=0)
gumbi.grid(row=0, column=1, rowspan=2, pady=30)


# INPUTI

delana_leta = tk.IntVar()
mesecna_letna = tk.IntVar()
placa = tk.IntVar()
starost = tk.IntVar()
visanje = tk.IntVar()
spol = tk.IntVar()
predelana_leta = tk.IntVar()


delana_leta.set(0)
placa.set(0)
starost.set(0)
visanje.set(0)
spol.set(0)
mesecna_letna.set(0)
predelana_leta.set(0)


delana_leta_frame = tk.Frame(inputi)

tk.Label(delana_leta_frame, text='Čas dela').grid(row=0, columnspan=2)
tk.Entry(delana_leta_frame, textvariable=delana_leta).grid(row=1, column=0)
tk.Label(delana_leta_frame, text=' let').grid(row=1, column=1)

delana_leta_frame.grid(row=0, column=0, pady=10, padx=10)


placa_frame = tk.Frame(inputi)

tk.Label(placa_frame, text='Plača v €').grid(row=0, columnspan=2)
tk.Radiobutton(placa_frame, text='Mesečna', variable=mesecna_letna, value=0).grid(row=1, column=0)
tk.Radiobutton(placa_frame, text='Letna', variable=mesecna_letna, value=1).grid(row=1, column=1)
tk.Entry(placa_frame, textvariable=placa).grid(row=2, columnspan=2)

placa_frame.grid(row=0, column=1, pady=10, padx=10)


predelana_leta_frame = tk.Frame(inputi)

tk.Label(predelana_leta_frame, text='Delam že').grid(row=0, columnspan=2)
tk.Entry(predelana_leta_frame, textvariable=predelana_leta).grid(row=1, column=0)
tk.Label(predelana_leta_frame, text=' let').grid(row=1, column=1)

predelana_leta_frame.grid(row=1, column=0, pady=10, padx=10)


spol_frame = tk.Frame(inputi)

tk.Label(spol_frame, text='Spol').grid(row=0, columnspan=2)
tk.Radiobutton(spol_frame, text='Moški', variable=spol, value=0).grid(row=1, column=0)
tk.Radiobutton(spol_frame, text='Ženski', variable=spol, value=1).grid(row=1, column=1)

spol_frame.grid(row=1, column=1, pady=10, padx=10)


starost_frame = tk.Frame(inputi)

tk.Label(starost_frame, text='Starost').grid(row=0, columnspan=2)
tk.Entry(starost_frame, textvariable=starost).grid(row=1, column=0)
tk.Label(starost_frame, text=' let').grid(row=1, column=1)

starost_frame.grid(row=2, column=0, pady=10, padx=10)


visanje_frame = tk.Frame(inputi)

tk.Label(visanje_frame, text='Letna povišica').grid(row=0, columnspan=2)
tk.Entry(visanje_frame, textvariable=visanje).grid(row=1, column=0)
tk.Label(visanje_frame, text='€').grid(row=1, column=1)

visanje_frame.grid(row=2, column=1, pady=10, padx=10)

# KONEC INPUTI


# FUNKCIJE

def preverjanje(x):
    if x <= 0:
        return False
    else:
        return True


def spucaj():
    tk.Label(outputi, text='                                                             ').grid(row=0, column=0)
    tk.Label(outputi, text='                                                             ').grid(row=0, column=1)
    tk.Label(outputi, text='                                                             ').grid(row=1, column=0)
    tk.Label(outputi, text='                                                             ').grid(row=1, column=1)


def koliko_ze_zasluzil():
    spucaj()
    if preverjanje(delana_leta.get()) and preverjanje(placa.get()):
        if mesecna_letna.get() == 0:
            rezultat = placa.get() * 12 * delana_leta.get()
            tk.Label(outputi, text='V {0} letih zaslužite:'.format(delana_leta.get())).grid(row=0, column=0)
            tk.Label(outputi, text='{0} €'.format(rezultat)).grid(row=1, column=0)
        else:
            rezultat = placa.get() * delana_leta.get()
            tk.Label(outputi, text='V {0} letih zaslužite:'.format(delana_leta.get())).grid(row=0, column=0)
            tk.Label(outputi, text='{0}'.format(rezultat)).grid(row=1, column=0)
    else:
        return messagebox.showinfo('Pozor!', 'Pravilno morate izpolniti vsa zahtevana polja!')


def pametni_podatki(delovna_doba, starost):
    if delovna_doba > 40 or starost > 65:
        return False
    elif delovna_doba + 15 > starost:
        return False
    else:
        return True


def koliko_delal_skupaj(delana_leta, spol, starost):
    if spol == 0:
        if starost + (40 - delana_leta) >= 65:
            return 65 - starost + delana_leta
        else:
            return 40
    elif spol == 1:
        if starost + (40 - delana_leta) >= 64:
            return 64 - starost + delana_leta
        else:
            return 40


def koliko_zasluzil_skupaj():
    spucaj()
    if preverjanje(placa.get()) and preverjanje(starost.get()) and predelana_leta.get() >= 0:
        if pametni_podatki(predelana_leta.get(), starost.get()):
            if mesecna_letna.get() == 0:
                rezultat = koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get()) * placa.get() * 12
            else:
                rezultat = koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get()) * placa.get()
        else:
            return messagebox.showinfo('Pozor!', 'Popravite vrednosti delovne dobe ali starosti.')

        tk.Label(outputi, text='V {0} letih boste zaslužili:'
                 .format(koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get()))).grid(row=0, column=0)
        tk.Label(outputi, text='{0} €'
                 .format(rezultat)).grid(row=1, column=0)
        tk.Label(outputi, text='Delali boste še:').grid(row=0, column=1)
        tk.Label(outputi, text='{0} let.'.format(koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get()) -
                                                 predelana_leta.get())).grid(row=1, column=1)

    else:
        return messagebox.showinfo('Pozor!', 'Pravilno morate izpolniti vsa zahtevana polja!')


def zasluzil_s_povisico():
    spucaj()
    vsa_leta_dela = koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get())
    if predelana_leta.get() >= 0 and preverjanje(placa.get()) \
            and preverjanje(starost.get()) and preverjanje(visanje.get()):
        if pametni_podatki(predelana_leta.get(), starost.get()):
            if mesecna_letna.get() == 0:
                rezultat = round(vsa_leta_dela * placa.get() * 12 + vsa_leta_dela * visanje.get() *
                                 (vsa_leta_dela - 1) * 0.5, 2)
            else:
                rezultat = round(vsa_leta_dela * placa.get() + vsa_leta_dela * visanje.get() *
                                 (vsa_leta_dela - 1) * 0.5, 2)

            tk.Label(outputi, text='V {0} letih s povišico {1} € zaslužite:'.format(
                koliko_delal_skupaj(predelana_leta.get(), spol.get(), starost.get()), visanje.get()))\
                .grid(row=0, column=0)
            tk.Label(outputi, text='{0} €'.format(rezultat)).grid(row=1, column=0)
            tk.Label(outputi, text='Delali boste še:').grid(row=0, column=1)
            tk.Label(outputi, text='{0} let.'.format(koliko_delal_skupaj(predelana_leta.get(), spol.get(),
                                                        starost.get()) - predelana_leta.get())).grid(row=1, column=1)
        else:
            return messagebox.showinfo('Pozor!', 'Popravite vrednosti delovne dobe ali starosti.')

    else:
        return messagebox.showinfo('Pozor!', 'Pravilno morate izpolniti vsa zahtevana polja!')


def pobrisi_podatke():
    spucaj()
    delana_leta.set(0)
    predelana_leta.set(0)
    placa.set(0)
    starost.set(0)
    visanje.set(0)
    spol.set(0)
    mesecna_letna.set(0)


# KONEC FUNKCIJE


# GUMBI

tk.Label(gumbi, text='Koliko zaslužite v določenem času?').grid(row=0)
tk.Label(gumbi, text='(Vnesite čas dela in plačo)', fg='grey').grid(row=1)
tk.Button(gumbi, text='Izračunaj', command=koliko_ze_zasluzil).grid(row=2, pady=5)

tk.Label(gumbi, text='Koliko boste zaslužili v življenju?').grid(row=3)
tk.Label(gumbi, text='(Vnesite opravljeno delovno dobo, plačo, spol in starost)', fg='grey').grid(row=4)
tk.Button(gumbi, text='Izračunaj', command=koliko_zasluzil_skupaj).grid(row=5, pady=5)

tk.Label(gumbi, text='Koliko boste zaslužili v življenju s povišico?').grid(row=6)
tk.Label(gumbi, text='(Vnesite opravljeno delovno dobo, plačo, starost, spol in povišico)', fg='grey').grid(row=7)
tk.Button(gumbi, text='Izračunaj', command=zasluzil_s_povisico).grid(row=8, pady=5)

tk.Label(gumbi, text='Želite pobrisati vnešene podatke?').grid(row=9)
tk.Button(gumbi, text='Pobriši', fg='red', command=pobrisi_podatke).grid(row=10, pady=5)

tk.Label(outputi, text='                                                        ').grid(row=0, column=0)
tk.Label(outputi, text='                                                        ').grid(row=0, column=1)
tk.Label(outputi, text='                                                        ').grid(row=1, column=0)
tk.Label(outputi, text='                                                        ').grid(row=1, column=1)

# KONEC GUMBI


okno.mainloop()