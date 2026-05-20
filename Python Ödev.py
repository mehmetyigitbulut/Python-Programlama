from abc import ABC, abstractmethod

class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self.baslik = baslik
        self.kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value

class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"Kitap -> Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"

class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self.yayin_donemi = yayin_donemi
        self.sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"Dergi -> Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"

class Islem(ABC):
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self, kayitNo):
        pass

    @abstractmethod
    def guncelle(self, kayitNo):
        pass

    @abstractmethod
    def listele(self):
        pass

class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def ekle(self):
        baslik = input("Kitabın başlığını girin: ")
        kayitNo = input("Kitabın kayıt numarasını girin: ")
        
        for k in self.kitaplar:
            if k.kayitNo == kayitNo:
                print("Hata: Bu kayıt numarasına sahip bir kitap zaten var!")
                return

        yazar = input("Kitabın yazarını girin: ")
        sayfa = input("Kitabın sayfa sayısını girin: ")
        
        yeni_kitap = Kitap(baslik, kayitNo, yazar, sayfa)
        self.kitaplar.append(yeni_kitap)
        print("Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {len(self.kitaplar)}")

    def sil(self, kayitNo):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)
                print(f"{kayitNo} numaralı kitap silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self, kayitNo):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                print("Yeni bilgileri girin (Değiştirmek istemiyorsanız boş bırakın):")
                yeni_baslik = input(f"Yeni başlık ({kitap.baslik}): ")
                yeni_yazar = input(f"Yeni yazar ({kitap.yazar}): ")
                
                if yeni_baslik: kitap.baslik = yeni_baslik
                if yeni_yazar: kitap.yazar = yeni_yazar
                
                print("Kitap güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        if not self.kitaplar:
            print("Kayıt bulunamadı.")
            return
        
        print("\n--- KİTAPLAR LİSTESİ ---")
        for kitap in self.kitaplar:
            print(kitap)

class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def ekle(self):
        baslik = input("Derginin başlığını girin: ")
        kayitNo = input("Derginin kayıt numarasını girin: ")
        
        for d in self.dergiler:
            if d.kayitNo == kayitNo:
                print("Hata: Bu kayıt numarasına sahip bir dergi zaten var!")
                return

        donem = input("Yayın dönemi (Aylık/Haftalık vb.): ")
        sayi = input("Sayı numarası: ")
        
        yeni_dergi = Dergi(baslik, kayitNo, donem, sayi)
        self.dergiler.append(yeni_dergi)
        print("Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {len(self.dergiler)}")

    def sil(self, kayitNo):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)
                print(f"{kayitNo} numaralı dergi silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self, kayitNo):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                yeni_donem = input(f"Yeni dönem ({dergi.yayin_donemi}): ")
                if yeni_donem: dergi.yayin_donemi = yeni_donem
                print("Dergi güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        if not self.dergiler:
            print("Kayıt bulunamadı.")
            return
        
        print("\n--- DERGİLER LİSTESİ ---")
        for dergi in self.dergiler:
            print(dergi)

class Menu:
    def __init__(self):
        self.kitap_islem = KitapIslem()
        self.dergi_islem = DergiIslem()

    def goster(self):
        print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")

    def calistir(self):
        while True:
            self.goster()
            secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

            if secim == '1':
                self.kitap_islem.ekle()
            elif secim == '2':
                k_no = input("Silinecek kitabın kayıt numarası: ")
                self.kitap_islem.sil(k_no)
            elif secim == '3':
                k_no = input("Güncellenecek kitabın kayıt numarası: ")
                self.kitap_islem.guncelle(k_no)
            elif secim == '4':
                self.kitap_islem.listele()
            elif secim == '5':
                self.dergi_islem.ekle()
            elif secim == '6':
                d_no = input("Silinecek derginin kayıt numarası: ")
                self.dergi_islem.sil(d_no)
            elif secim == '7':
                d_no = input("Güncellenecek derginin kayıt numarası: ")
                self.dergi_islem.guncelle(d_no)
            elif secim == '8':
                self.dergi_islem.listele()
            elif secim == '9':
                print("Sistemden çıkılıyor. İyi günler!")
                break
            else:
                print("Geçersiz seçim. Lütfen 1-9 arası bir sayı girin.")

if __name__ == "__main__":
    uygulama = Menu()
    uygulama.calistir()