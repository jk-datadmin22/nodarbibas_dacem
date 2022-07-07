import requests
import time
from bs4 import BeautifulSoup as bs
import csv

ADRESE = "https://www.ss.lv/lv/transport/cars/today/"


def saglabat_lapu(adrese, fails):
    pieprasijums = requests.get(adrese)

    if pieprasijums.status_code == 200:
        lapa = pieprasijums.text

        with open(fails, "w", encoding="utf-8") as f:
            f.write(lapa)
    else:
        print("Radās kļūda lapas pieprasīšanā! Kods:", pieprasijums.status_code)
        return

#saglabat_lapu(ADRESE, "7_diena/requests/lapas/lapa_1.html")

#ADRESE = "https://www.ss.com/lv/transport/cars/today/page1.html"
#ADRESE = "https://www.ss.com/lv/transport/cars/today/page2.html"
#ADRESE = "https://www.ss.com/lv/transport/cars/today/page3.html"
#ADRESE = "https://www.ss.com/lv/transport/cars/today/page4.html"

def atvilkt_lapas(daudzums):
    for i in range(1, daudzums + 1):
        adrese = f"{ADRESE}page{i}.html"
        fails = f"7_diena/requests/lapas/lapa_{i}.html"
       
        print("Pieprasījums uz", adrese, "--->", fails)
        saglabat_lapu(adrese, fails)

        time.sleep(2)

#atvilkt_lapas(46)
#kad atvilkts, aizkomentē, lai palaižot lapu, nesāk vilkt no jauna

def info(htmlDatne):
    with open(htmlDatne, "r", encoding='utf-8') as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    tabulas = zupa.find_all("table")
    
    
    #print(tabulas[4])
    autoTabula = tabulas[4]

    autoRindas = autoTabula.find_all("tr")

    dati = []

    for rinda in autoRindas[1:-1]:
        auto = {}
        # print(rinda)
        # print("============================")
        # print("============================")
        # print("============================")
        # print("============================")

        lauki = rinda.find_all("td")

        if lauki[4].text == "-" or lauki:
            continue

        auto['gads'] = lauki[4].text

        print(lauki[5].text)
        tilpums = lauki[5].text

        if "D" in tilpums:
            auto["dzinejs"] = "dīzelis"
            auto["tilpums"] = tilpums[:-1]
        elif "H" in tilpums:
            auto["dzinejs"] = "hibrīds"
            auto["tilpums"] = tilpums[:-1]
        elif "E" in tilpums:
            #ignorējam elektromobīļus
            continue
        else:
            auto["dzinejs"] = "benzins"
            auto["tilpums"] = tilpums 

        
        auto["nobraukums"] = lauki[6].text.replace("tūkst.", "")

        # auto["cena"] = lauki[7].text.replace(",", "").replace("  eiro", "")

        lauki[3].br.replace_with("!")
        auto["marka"] = lauki[3].text.replace("!", " ")
        auto["razotajs"] = lauki[3].text.split("!")[0]
        auto["modelis"] = lauki[3].text.split("!")[1]

        # print(auto)
        
        # exit()
    
        dati.append(auto)

    return dati


    # for tabula in tabulas:
    #     print(tabula)
    #     print("============================")
    #     print("============================")
    #     print("============================")
    #     print("============================")

def saglabat_datus(autoDati):
    with open("7_diena/requests/ss_auto.csv", "w", encoding = "uft-8", newline="") as f:
        kolonnas = ['razotajs', 'modelis']
        w = csv.DictWriter(f, fieldnames=kolonnas)
        w.writeheader


def izvilkt_datus(daudzums):
    visiDati = []
    for i in range(1, daudzums +1):
        fails = f"7_diena/requests/lapas/lapa_{i}.html"
        datnesDati = info(fails)
        visiDati = visiDati + datnesDati

        print(visiDati)
        saglabat_datus(visiDati)   

izvilkt_datus(46)


dati = info("7_diena/requests/lapas/lapa_1.html")
print(dati)