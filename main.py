import time
def timer(sure):
    print(f"zamanlayici {sure} saniye basladi")
    time.sleep(sure)
    print("zamanlayici tamamlandi")

if __name__ == "__main__":
    try:
        sure = int(input("zamanlayici suresini saniye cinsinden girin: "))
        timer(sure)
    except ValueError:
        print("gecersiz sure tam sayi giriniz")
