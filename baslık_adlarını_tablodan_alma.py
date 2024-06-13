import pandas as pd

# CSV dosyasının başlıklarını ve ilk birkaç satırını okuma
csv_file_path = 'C:\\Users\ASUS\Downloads/Basvurular.csv'
df = pd.read_csv(csv_file_path)

# Başlıkları ve ilk birkaç satırı yazdırma
print(df.head())
print(df.columns)
