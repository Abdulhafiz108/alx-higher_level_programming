#!/usr/bin/python3
"""
Displays all values where name matches argument
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    mydb = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
    )
    mycur = mydb.cursor()
    mycur.execute(
            """
            SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC;
            """.format(argv[4])
    )
    my_data = mycur.fetchall()
    for i in my_data:
        print(i)
    mycur.close()
    mydb.close()
