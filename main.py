
import yfinance as yf

def dolar():
    dolar_kuru = yf.Ticker("USDTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Amerikan Doları = {dolar_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Amerikan Doları ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Amerikan Doları")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * dolar_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / dolar_kuru:.2f} Amerikan Doları"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue

def euro():
    euro_kuru = yf.Ticker("EURTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Euro = {euro_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Euro ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Euro")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * euro_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / euro_kuru:.2f} Euro"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue

def ingiliz_strelini():
    ingiliz_strelini_kuru = yf.Ticker("GBPTRY=X").info.get("regularMarketPrice")
    print(f"1 adet İngiliz Sterlini = {ingiliz_strelini_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. İngiliz Sterlini ➔ Türk Lirası")
        print("2. Türk Lirası ➔ İngiliz Sterlini")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * ingiliz_strelini_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / ingiliz_strelini_kuru:.2f} İngiliz Sterlini"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue

def isvicre_frank():
    isvicre_franki_kuru = yf.Ticker("CHFTRY=X").info.get("regularMarketPrice")
    print(f"1 adet İsviçre Frangı = {isvicre_franki_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. İsviçre Frangı ➔ Türk Lirası")
        print("2. Türk Lirası ➔ İsviçre Frangı")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * isvicre_franki_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / isvicre_franki_kuru:.2f} İsviçre Frangı"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def suudi_arabistan_riyali():
    suudi_arabistan_riyali_kuru = yf.Ticker("SARTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Suudi Arabistan Riyali = {suudi_arabistan_riyali_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Suudi Arabistan Riyali ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Suudi Arabistan Riyali")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * suudi_arabistan_riyali_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / suudi_arabistan_riyali_kuru:.2f} Suudi Arabistan Riyali"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def japon_yeni():
    japon_yeni_kuru = yf.Ticker("JPYTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Japon Yeni = {japon_yeni_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Japon Yeni ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Japon Yeni")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * japon_yeni_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / japon_yeni_kuru:.2f} Japon Yeni"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def kanada_dolari():
    kanada_dolari_kuru = yf.Ticker("CADTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Kanada Doları = {kanada_dolari_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Kanada Doları ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Kanada Doları")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * kanada_dolari_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / kanada_dolari_kuru:.2f} Kanada Doları"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def avustralya_dolari():
    avustralya_dolari_kuru = yf.Ticker("AUDTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Avustralya Doları = {avustralya_dolari_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Avustralya Doları ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Avustralya Doları")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * avustralya_dolari_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / avustralya_dolari_kuru:.2f} Avustralya Doları"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def rus_rublesi():
    rus_rublesi_kuru = yf.Ticker("RUBTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Rus Rublesi = {rus_rublesi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Rus Rublesi ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Rus Rublesi")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * rus_rublesi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / rus_rublesi_kuru:.2f} Rus Rublesi"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def cin_yuani():
    cin_yuani_kuru = yf.Ticker("CNYTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Çin Yuanı = {cin_yuani_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Çin Yuanı ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Çin Yuanı")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * cin_yuani_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / cin_yuani_kuru:.2f} Çin Yuanı"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def kuveyt_dinari():
    kuveyt_dinari_kuru = yf.Ticker("KWDTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Kuveyt Dinarı = {kuveyt_dinari_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Kuveyt Dinarı ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Kuveyt Dinarı")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * kuveyt_dinari_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / kuveyt_dinari_kuru:.2f} Kuveyt Dinarı"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def katar_riyali():
    katar_riyali_kuru = yf.Ticker("QARTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Katar Riyali = {katar_riyali_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Katar Riyali ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Katar Riyali")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * katar_riyali_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / katar_riyali_kuru:.2f} Katar Riyali"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def birlesik_arap_emirlikleri():
    birlesik_arap_emirlikleri_kuru = yf.Ticker("AEDTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Birleşik Arap Emirlikleri Dirhemi = {birlesik_arap_emirlikleri_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Birleşik Arap Emirlikleri Dirhemi ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Birleşik Arap Emirlikleri Dirhemi")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * birlesik_arap_emirlikleri_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / birlesik_arap_emirlikleri_kuru:.2f} Birleşik Arap Emirlikleri Dirhemi"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def isvec_kronu():
    isvec_kronu_kuru = yf.Ticker("SEKTRY=X").info.get("regularMarketPrice")
    print(f"1 adet İsveç Kronu = {isvec_kronu_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. İsveç Kronu ➔ Türk Lirası")
        print("2. Türk Lirası ➔ İsveç Kronu")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * isvec_kronu_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / isvec_kronu_kuru:.2f} İsveç Kronu"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def norvec_kronu():
    norvec_kronu_kuru = yf.Ticker("NOKTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Norveç Kronu = {norvec_kronu_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Norveç Kronu ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Norveç Kronu")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * norvec_kronu_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / norvec_kronu_kuru:.2f} Norveç Kronu"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def danimarka_kronu():
    danimarka_kronu_kuru = yf.Ticker("DKKTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Danimarka Kronu = {danimarka_kronu_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Danimarka Kronu ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Danimarka Kronu")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * danimarka_kronu_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / danimarka_kronu_kuru:.2f} Danimarka Kronu"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def polonya_zlotisi():
    polonya_zlotisi_kuru = yf.Ticker("PLNTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Polonya Zlotisi = {polonya_zlotisi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Polonya Zlotisi ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Polonya Zlotisi")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * polonya_zlotisi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / polonya_zlotisi_kuru:.2f} Polonya Zlotisi"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def rumen_leyi():
    rumen_leyi_kuru = yf.Ticker("RONTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Rumen Leyi = {rumen_leyi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Rumen Leyi ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Rumen Leyi")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * rumen_leyi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / rumen_leyi_kuru:.2f} Rumen Leyi"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def cek_korunasi():
    cek_korunasi_kuru = yf.Ticker("CZKTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Çek Korunası = {cek_korunasi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Çek Korunası ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Çek Korunası")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * cek_korunasi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / cek_korunasi_kuru:.2f} Çek Korunası"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def bulgar_levasi():
    bulgar_levasi_kuru = yf.Ticker("BGNTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Bulgar Levası = {bulgar_levasi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Bulgar Levası ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Bulgar Levası")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * bulgar_levasi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / bulgar_levasi_kuru:.2f} Bulgar Levası"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def hindistan_rupisi():
    hindistan_rupisi_kuru = yf.Ticker("INRTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Hindistan Rupisi = {hindistan_rupisi_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Hindistan Rupisi ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Hindistan Rupisi")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * hindistan_rupisi_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / hindistan_rupisi_kuru:.2f} Hindistan Rupisi"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def meksika_pesosu():
    meksika_pesosu_kuru = yf.Ticker("MXNTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Meksika Pesosu = {meksika_pesosu_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Meksika Pesosu ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Meksika Pesosu")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * meksika_pesosu_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / meksika_pesosu_kuru:.2f} Meksika Pesosu"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def guney_kore_wonu():
    guney_kore_wonu_kuru = yf.Ticker("KRWTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Güney Kore Wonu = {guney_kore_wonu_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Güney Kore Wonu ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Güney Kore Wonu")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * guney_kore_wonu_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / guney_kore_wonu_kuru:.2f} İGüney Kore Wonu"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue


def brezilya_reali():
    brezilya_reali_kuru = yf.Ticker("BRLTRY=X").info.get("regularMarketPrice")
    print(f"1 adet Brezilya Reali = {brezilya_reali_kuru:.2f} TL")
    while True:
        print("Çevirmek istediginiz para birimi hangisidir")
        print("1. Brezilya Reali ➔ Türk Lirası")
        print("2. Türk Lirası ➔ Brezilya Reali")
        print("3. Çıkmak için basınız.")
        try:
            islem = input("yapmak istediğiniz işlem numarasını giriniz: ")
            if islem in ("1", "2", "3"):
                if islem == "3":
                    break
                elif islem == "1" or islem == "2":
                    cevirmek_istenen_kur_miktarı = float(input("Çevirmek istediğiniz mikatırı giriniz: "))
                    if islem == "1":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı * brezilya_reali_kuru:.2f} TL"
                    elif islem == "2":
                        return f"Miktarınız: {cevirmek_istenen_kur_miktarı / brezilya_reali_kuru:.2f} Brezilya Reali"
            else:
                print("Hatalı işlem geçeri bir veri giriniz.")
                continue
        except ValueError:
            print("Lütfen sayısal bir veri giriniz.")
            continue



def döviz_secme():
    while True:
        try: 
             secim = int(input("İşlem yapmak istediğini döviz biriminin numarasını giriniz. : "))
             print("Örn: 1. Amerikan Doları = 1 yazacaksınız")
             dövizler = ["Amerikan Doları","Euro","İngiliz Sterlini","İsviçre Frangı","Suudi Arabistan Riyali","Japon Yeni,Kanada Doları","Avustralya Doları","Rus Rublesi","Çin Yuanı","Kuveyt Dinarı","Katar Riyali","Birleşik Arap Emirlikleri Dirhemi","İsveç Kronu","Norveç Kronu","Danimarka Kronu","Polonya Zlotisi","Rumen Leyi","Çek Korunası","Bulgar Levası","Hindistan Rupisi","Meksika Pesosu","Güney Kore Wonu","Brezilya Reali","Çıkış"]
             for döviz in range(len(dövizler)) :
                 print(döviz + 1,".",dövizler[döviz])

             if  1<= secim <=24 :
                 if secim == 1:
                     print(dolar())
                     continue

                 elif secim == 2:
                     print(euro())
                     continue

                 elif secim == 3:
                     print(isvicre_frank())
                     continue

                 elif secim == 4:
                     print(suudi_arabistan_riyali())
                     continue

                 elif secim == 5:
                     print(japon_yeni())
                     continue

                 elif secim == 6:
                     print(kanada_dolari())
                     continue

                 elif secim == 7:
                     print(avustralya_dolari())
                     continue

                 elif secim == 8:
                     print(rus_rublesi())
                     continue

                 elif secim == 9:
                     print(cin_yuani())
                     continue

                 elif secim == 10: 
                     print(kuveyt_dinari())
                     continue

                 elif secim == 11:
                     print(katar_riyali())
                     continue

                 elif secim == 12:
                     print(birlesik_arap_emirlikleri())
                     continue

                 elif secim == 13:
                     print(isvec_kronu())
                     continue

                 elif secim == 14:
                     print(norvec_kronu())
                     continue
                     
                 elif secim == 15:
                     print(danimarka_kronu())
                     continue

                 elif secim == 16:
                     print(polonya_zlotisi())
                     continue

                 elif secim == 17:
                     print(rumen_leyi())
                     continue

                 elif secim == 18:
                     print(cek_korunasi())
                     continue

                 elif secim == 19:
                     print(bulgar_levasi())
                     continue

                 elif secim == 20:
                     print(hindistan_rupisi())
                     continue

                 elif secim == 21:
                     print(meksika_pesosu())
                     continue

                 elif secim == 22:
                     print(guney_kore_wonu())
                     continue
                 
                 elif secim == 23:
                     print(brezilya_reali())
                     continue
                 
                 elif secim == 24:
                     print("Çıkılıyor...")
                     break

             else: 
                 print("İşlem 1 ve 24 sayıları arasındadır." )
                 continue
        except ValueError:
            print("Lütfen bir numara/sayı giriniz.")
            continue

döviz_secme()