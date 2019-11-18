import sqlite3
import base64
import webbrowser

conn = sqlite3.connect("week10.db")


while True:
    urlId = input("Enter a number between 1 and 29, enter q to quit")

    if urlId == "q":
        break


    if int(urlId) < 1 or int(urlId) > 29:
        print("This is not a valid input")
        continue

    cur = conn.cursor()
    queryToExecute = "SELECT id, Link FROM Lab10 WHERE id =", urlId
    joinedQuery = ''.join(queryToExecute)
    cur.execute(joinedQuery)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    url64 = row[1]
    decodedUrl = base64.urlsafe_b64decode(url64)
    webbrowser.open(decodedUrl)
    

    city = input("What city did the link lead you to?")
    country = input("In what country is that city?")

    sql = ''' UPDATE Lab10
              SET city = ? ,
                  country = ?
              WHERE id = ?'''
    task = (city, country, urlId)
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()



    