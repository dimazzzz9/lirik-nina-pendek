import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Aku tahu kamu hebat", 0.1),
        ("Namun, s'lamanya diriku pasti berkutat", 0.09),
        ("'Tuk s'lalu jauhkanmu dari dunia yang jahat", 0.07),
        ("Ini sumpahku padamu 'tuk biarkanmu", 0.09),
        ("Tumbuh lebih baik, cari panggilanmu", 0.09),
        ("Jadi lebih baik dibanding diriku", 0.09),
        ("'Tuk sementara kita tertawakan berbagai hal", 0.09),
        ("Yang lucu dan lara selepas lepasnya", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay= [0.3, 0.1, 0.09, 0.3, 0.3, 0.3, 0.3, 0.3]
    # Ubah judul lagu
    print("\n== nina-feast ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("// Code dimzzzzzzzz")


jalanin_lirik()