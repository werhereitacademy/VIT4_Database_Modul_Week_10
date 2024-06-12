import pandas as pd

# CSV dosyasını okuma ve gerekli sütunları seçme
csv_file_path = 'C:\\Users\ASUS\Downloads/Basvurular.csv'
selected_columns = [ 'Adınız Soyadınız', 'Mail adresiniz',
       'Telefon Numaranız', 'Posta Kodunuz', 'Yaşadığınız Eyalet']

# CSV dosyasını okuma
df = pd.read_csv(csv_file_path)

# Yalnızca gerekli sütunları seçme
df_selected = df[selected_columns]

# Temizlenmiş veriyi yeni bir CSV dosyasına yazma
cleaned_csv_file_path = 'C:\\Users\ASUS\Downloads/Kursiyerler.csv'
df_selected.to_csv(cleaned_csv_file_path, index=False)

print("Temizlenmiş veriler başarıyla yeni bir CSV dosyasına kaydedildi.")
