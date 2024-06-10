import psycopg2

# Veritabanı bağlantı bilgileri
database_name = "Employees"
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
    
    # Tablo oluşturma sorgusu
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employees_table(
        emp_id INT PRIMARY KEY,
        first_name VARCHAR(15),
        last_name VARCHAR(15),
        salary INT,
        job_title VARCHAR(20),
        gender VARCHAR(6),
        hire_date DATE
    )
    """
    
    # Sorguyu çalıştırma
    cursor.execute(create_table_query)
    connection.commit()  # Değişiklikleri kaydet

    print("Tablo oluşturuldu veya zaten mevcut.")

    insert_table_query = """
    INSERT INTO Employees_table(
        emp_id ,
        first_name ,
        last_name ,
        salary ,
        job_title ,
        gender ,
        hire_date 
    ) VALUES
    (17679,'Robert','Gilmore',110000,'Operation Director','Male','2018-09-04'),
    (26650,'Elvis','Ritter',86000,'Sales Manager','Male','2017-11-24')

    """
    cursor.execute(insert_table_query)
    connection.commit()  # Değişiklikleri kaydet
    print("veriler eklendi")


except Exception as e:
    print("Bağlantı hatası:", e)
finally:
    # Bağlantıyı kapatın"""  """
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Bağlantı kapatıldı.")
