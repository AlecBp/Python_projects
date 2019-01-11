import MySQLdb

db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd=""
)

cur = db.cursor()

while(True):
    query = input("Type your query:")
    try:
        cur.execute(str(query))
        rows = cur.fetchall()
        for row in rows:
            for col in row:
                print("%s," % col)
            print("\n")
    except:
        print("ERROR:\n"+Exception)
    