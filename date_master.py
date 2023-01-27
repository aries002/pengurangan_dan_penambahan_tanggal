import datetime

def pengurangan_bulan(datesi, months = 0):
    # WARNING!! TIDAK BISA MENGURANGI LEBIH DATI 1 TAHUN

    sixMonth = datesi.month - months
    
    if sixMonth<1:
        sixMonth +=12
        datesi = datesi.replace(year = datesi.year - 1)

    return datesi.replace(month = sixMonth)

def penambahan_bulan(datesi, months = 0):
    # WARNING!! TIDAK BISA MENAMBAH LEBIH DATI 1 TAHUN
    sixMonth = months + datesi.month
    if sixMonth>12:
        sixMonth -=12
        datesi = datesi.replace(year = datesi.year + 1)
    return datesi.replace(month = sixMonth)


# testing
today = datetime.date.today()
tgl = datetime.date(2016,5,12)
newdate = pengurangan_bulan(tgl, 12)
print(newdate.strftime("%y-%m-%d"))
