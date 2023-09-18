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
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id ASC;
            """
    )
    my_data = mycur.fetchall()
    for i in my_data:
        print(i)
    mycur.close()
    mydb.close()
