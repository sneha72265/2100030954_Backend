import mysql.connector as mysql
#establishing connectivity with mysql database
try:
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="safertek_exam"
    )

    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                    location_id INT AUTO_INCREMENT PRIMARY KEY,
                    street_address VARCHAR(255),
                    city VARCHAR(255),
                    state_province VARCHAR(255),
                    country_id VARCHAR(2)
                )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    country_id VARCHAR(2) PRIMARY KEY,
                    country_name VARCHAR(255),
                    region_id VARCHAR(255)
                )''')

    print("Location table:")
    print("Enter the locations table data")
    print()

    street_address = input("street address: ")
    city = input("city: ")
    state_province = input("state/province: ")
    country_id = input("country code: ")
    print()

    sql = "INSERT INTO locations (street_address, city, state_province, country_id) VALUES (%s, %s, %s, %s)"
    values = (street_address, city, state_province, country_id)
    cursor.execute(sql, values)

    print("Countries table data:")
    print("Enter the countries table data")
    print()
    country_id = input("country ID:")
    country_name = input("country Name:")
    region_id = input("region id:")
    sql = "INSERT INTO countries (country_id, country_name,region_id) VALUES (%s, %s, %s)"
    values = (country_id, country_name, region_id)
    cursor.execute(sql, values)
    connection.commit()

#acknowledging successfull insertion
    print("Data inserted successfully!!")
    print()

#Performing task1 that is join operation
    print("*****************Join Condition********************")
    country_name = input("Enter country name to perform join condition on that country name: ")
    cursor.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name, c.country_id
                   FROM locations l
                   JOIN countries c ON l.country_id = c.country_id
                   WHERE c.country_name = %s ''', (country_name,))
    results = cursor.fetchall()
    # Display results
    for i in results:
        print(i)

except mysql.Error as err:
    print("MySQL Error found:", err)

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection is not None:
        connection.close()
