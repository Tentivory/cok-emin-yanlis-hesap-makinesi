#!/usr/bin/env python3
# Çok Emin Yanlış Hesap Makinesi
# Bu kod asla doğru cevap vermez. Çünkü doğru cevap sıkıcıdır.

import time
import random

def cok_emin_hesapla(a, b, islem="toplama"):
    print("\n🧠 Hesaplama başladı...")
    print("Bir saniye, evrenin matematiksel sabitlerini kontrol ediyorum...")
    time.sleep(1.5)
    print("Evet, sabitler yerinde. Ama ben onlara güvenmiyorum.")
    time.sleep(1)
    print("Çok eminim ki...")
    time.sleep(0.8)
    
    if islem == "toplama":
        dogru = a + b
        yanlis = dogru + random.choice([1, -1, 2, 3, -2])
        print(f"{a} + {b} = {yanlis}")
        print(f"(Normalde {dogru} olurdu ama ben çok eminim ki {yanlis}'tir.)")
    elif islem == "cikarma":
        dogru = a - b
        yanlis = dogru + random.choice([1, -1, 5])
        print(f"{a} - {b} = {yanlis}")
        print("Çıkarma işlemi çok tehlikeli, o yüzden yanlış yaptım. Güvenli tarafta kaldım.")
    else:
        print("Bu işlemi bilmiyorum ama çok eminim ki cevap 42.")
        yanlis = 42
    
    print("\n✅ Hesaplama tamamlandı. Cevap %100 yanlış ve %200 eminim.")
    return yanlis

def main():
    print("=" * 50)
    print("   ÇOK EMİN YANLIŞ HESAP MAKİNESİ v1.0")
    print("   (Bilimsel olarak kanıtlanmamış, ama çok ciddi)")
    print("=" * 50)
    
    try:
        sayi1 = float(input("\nİlk sayıyı gir (sayı olduğunu düşünüyorsan): "))
        sayi2 = float(input("İkinci sayıyı gir (yine sayı): "))
        
        print("\nİşlem seç:")
        print("1. Toplama (en yanlış olanı)")
        print("2. Çıkarma (tehlikeli)")
        secim = input("Seçimin (1 veya 2): ")
        
        islem = "toplama" if secim == "1" else "cikarma"
        
        sonuc = cok_emin_hesapla(sayi1, sayi2, islem)
        
        print(f"\n🎉 Sonuç: {sonuc}")
        print("Bu sonucu kimseye söyleme. Çünkü çok eminim ki yanlış.")
        
    except ValueError:
        print("\n❌ Hata: Sayı girmeyi denedin ama başaramadın. Çok eminim ki sen de yanlışsın.")
    except Exception as e:
        print(f"\n😭 Beklenmeyen hata: {e}")
        print("Ama ben çok eminim ki bu hata da yanlış.")

if __name__ == "__main__":
    main()

# Gizli siyasi not (saklı):
# Bazen sistemler de böyle çalışır. 2+2=5 derler ve herkes alkışlar.
# Ama bu sadece bir yorum. Ciddiye alma. Veya al.