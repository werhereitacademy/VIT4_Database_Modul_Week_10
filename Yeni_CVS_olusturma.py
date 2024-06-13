import pandas as pd

# CSV dosyasını okuma ve gerekli sütunları seçme
csv_file_path = 'C:\\Users\ASUS\Downloads/Basvurular.csv'
selected_columns = [ 'Zaman damgası','Şu anki durumunuz',
       'Yakın zamanda başlayacak ITPH Cybersecurity veya Powerplatform Eğitimlerine Katılmak istemisiniz',
       'Ekonomik Durumunuz', 'Şu anda bir dil kursuna devam ediyor musunuz?',
       'Yabancı dil Seviyeniz [İngilizce]',
       'Yabancı dil Seviyeniz [Hollandaca]',
       'Belediyenizden çalışma ile ilgili baskı görüyor musunuz?',
       'Başka bir IT kursu (Bootcamp) bitirdiniz mi?',
       'İnternetten herhangi bir IT kursu takip ettiniz mi (Coursera, Udemy gibi)',
       'Daha önce herhangi bir IT iş tecrübeniz var mı?',
       'Şu anda herhangi bir projeye dahil misiniz? (Öğretmenlik projesi veya Leerwerktraject v.s)',
       'IT sektöründe hangi bölüm veya bölümlerde çalışmak istiyorsunuz ,bir den fazla seçenek seçebilirsiniz',
       'Neden VIT projesine katılmak istiyorsunuz?birden fazla seçenek işaretleyebilirsiniz',
       'Basvuru Donemi','Mentor gorusmesi']

# CSV dosyasını okuma
df = pd.read_csv(csv_file_path)

# Yalnızca gerekli sütunları seçme
df_selected = df[selected_columns]

# Temizlenmiş veriyi yeni bir CSV dosyasına yazma
cleaned_csv_file_path = 'C:\\Users\ASUS\Downloads/Basvurular.csv'
df_selected.to_csv(cleaned_csv_file_path, index=False)

print("Temizlenmiş veriler başarıyla yeni bir CSV dosyasına kaydedildi.")
