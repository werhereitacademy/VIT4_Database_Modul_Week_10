import psycopg2

# Veritabanı bağlantı bilgileri
database_name = "postgres"
user = "postgres"
password = "Veenendaal"
host = "localhost"

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

    # employees tablosunu oluşturma SQL sorgusu
    create_employees_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        salary INT,
        job_title VARCHAR(100),
        gender VARCHAR(10),
        hire_date DATE
    );
    '''
    cursor.execute(create_employees_table_query)
    connection.commit()
    print("employees tablosu oluşturuldu.")

    # Mevcut departments_table tablosunu bırakma ve yeniden oluşturma
    drop_departments_table_query = '''
    DROP TABLE IF EXISTS departments_table;
    '''
    cursor.execute(drop_departments_table_query)
    connection.commit()
    print("departments_table tablosu bırakıldı.")

    create_departments_table_query = '''
    CREATE TABLE departments_table (
        emp_id INT,
        dept_name VARCHAR(50),
        dept_id INT,
        PRIMARY KEY (emp_id, dept_id)
    );
    '''
    cursor.execute(create_departments_table_query)
    connection.commit()
    print("departments_table tablosu yeniden oluşturuldu.")

    # employees tablosuna veri ekleme SQL sorgusu
    insert_employees_data_query = '''
    INSERT INTO employees (emp_id, first_name, last_name, salary, job_title, gender, hire_date) VALUES
    (17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
    (26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
    (30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
    (49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
    (51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
    (67323, 'Lisa', 'Weiner', 75000, 'Business Analyst', 'Female', '2018-12-20'),
    (70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2019-06-28'),
    (71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-01-21'),
    (76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2018-06-25'),
    (97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2019-01-21')
    ON CONFLICT (emp_id) DO NOTHING;
    '''
    cursor.execute(insert_employees_data_query)
    connection.commit()
    print("Veriler employees tablosuna eklendi.")

    # departments_table tablosuna veri ekleme SQL sorgusu
    insert_departments_data_query = '''
    INSERT INTO departments_table (emp_id, dept_name, dept_id) VALUES
    (17679, 'Operations', 13),
    (26650, 'Marketing', 14),
    (30840, 'Operations', 15),
    (49823, 'Technology', 16),
    (51821, 'Operations', 17),
    (67323, 'Marketing', 18),
    (71119, 'Administrative', 19),
    (76589, 'Operations', 20)
    ON CONFLICT (emp_id, dept_id) DO NOTHING;
    '''
    cursor.execute(insert_departments_data_query)
    connection.commit()
    print("Veriler departments_table tablosuna eklendi.")

    # employees tablosundan tüm verileri seçme ve yazdırma
    cursor.execute("SELECT * FROM employees;")
    employees = cursor.fetchall()
    
    print("employees tablosundaki veriler:")
    for i in employees:
        print(i)

    # departments_table tablosundan tüm verileri seçme ve yazdırma
    cursor.execute("SELECT * FROM departments_table;")
    departments = cursor.fetchall()
    
    print("departments_table tablosundaki veriler:")
    for i in departments:
        print(i) 

    # Bağlantıyı kapatın
    cursor.close()
    connection.close()
    print("Bağlantı kapatıldı.")
except Exception as e:
    print("Bağlantı hatası:", e)
