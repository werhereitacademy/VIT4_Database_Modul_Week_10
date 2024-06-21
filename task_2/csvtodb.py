import csv
import psycopg2
import chardet

# Dosyanın kodlamasını belirleme
with open(r'C:\Users\gebruiker\Desktop\009.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

conn = psycopg2.connect(
    host="localhost",
    database="dbcrm",
    user="postgres",
    password="123"
)

cur = conn.cursor()

# Belirlenen kodlamayla dosyayı okuma
with open(r'C:\Users\gebruiker\Desktop\009.csv', 'r', newline='', encoding=encoding) as f:
    reader = csv.reader((line.replace('\0', '') for line in f))
    header = next(reader)  # Skip the header row
    
    # Doğru sütun sayısını kontrol etmek için header'ın uzunluğunu alın
    expected_num_columns = len(header)
    print(f"Expected number of columns: {expected_num_columns}")

    for line_num, row in enumerate(reader, start=2):  # Start from 2 to account for the header
        if len(row) != expected_num_columns:
            print(f"Row {line_num} has {len(row)} columns, expected {expected_num_columns}.")
            continue  # Hatalı satırı atla
        
        try:
            cur.execute(
                "INSERT INTO app1 (timestamp, current_status, attending_itph_training, economical_situation, attend_language_course, english_level, dutch_level, under_pressure, finished_bootcamp, online_it_course, it_experience, project_included, desire_to_work, reason_for_joining, application_period) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )
        except Exception as e:
            print(f"Error on row {line_num}: {e}")

conn.commit()
cur.close()
conn.close()
