import mysql.connector

def main():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pascal_16",
        database="4500final"
    )

    cursor = db.cursor()

    qIteration = input("Iteration #: ")
    qVariant = input("Variant (Control/Test): ")

    query = ("select AVG(Presence_Time) from userdata where Iteration=%s AND Variant=%s;")
    query_values = (qIteration, qVariant)
    cursor.execute(query, query_values)
    
    result = cursor.fetchall()
    print(f"Average: {result} seconds")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()