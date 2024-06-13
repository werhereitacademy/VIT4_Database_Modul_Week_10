import psycopg2

# Veritabanı bağlantı bilgileri
database_name = "CRM"
user = "postgres"
password = "2713"
host = "localhost"  # Genellikle localhost veya 127.0.0.1

# PostgreSQL veritabanına bağlanma
try:
    connection = psycopg2.connect(
        dbname=database_name,
        user=user,
        password=password,
        host=host
    )
    print("Bağlantı başarılı!")

    # Bağlantı üzerinden bir işlem (cursor) oluşturun
    cursor = connection.cursor()
    
    # kursiyerler ve basvurular tablolarını JOIN ile birleştiren sorgu
    join_query = """
    SELECT k.AdSoyad, k.MailAdresi, k.TelefonNumarası, k.PostaKodu, b.ZamanDamgası, b.SuAnkiDurum
    FROM kursiyerler k
    INNER JOIN basvurular b ON k.KursiyerID = b.KursiyerID
    """
    cursor.execute(join_query)
    
    # Sonuçları alın
    combined_results = cursor.fetchall()
    
    # Sonuçları yazdırın
    for row in combined_results:
        print(row)

except Exception as e:
    print("Bağlantı hatası:", e)
finally:
    # Bağlantıyı kapatın
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Bağlantı kapatıldı.")
