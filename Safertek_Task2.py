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

    c_name_input = input("Give Country name to find the adress: ")

    cursor.execute('''SELECT country_id
                   FROM countries
                   WHERE country_name = %s''', (c_name_input,))
    c_id = cursor.fetchone()

    if not c_id:
        print("Country not found.")
    else:
        country_id = c_id[0]

        cursor.execute('''SELECT location_id, street_address, city, state_province
                       FROM locations
                       WHERE country_id = %s''', (country_id,))
        results = cursor.fetchall()

#displaying the result
        for itr in results:
            print("Country:", c_name_input)
            print("Location ID:", itr[0])
            print("Street Address:", itr[1])
            print("City:", itr[2])
            print("State/Province:", itr[3])
            print()

except mysql.Error as err:
    print("MySQL Error found:", err)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection is not None:
        connection.close()
