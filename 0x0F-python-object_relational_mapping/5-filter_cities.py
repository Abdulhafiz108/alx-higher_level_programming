#!/usr/bin/python3
"""
Lists all cities of the argument
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
            SELECT * FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            """
    )
    my_data = mycur.fetchall()
    print(", ".join([city[2]
                    for city in my_data
                    if city[4] == argv[4]]))
    mycur.close()
    mydb.close()
