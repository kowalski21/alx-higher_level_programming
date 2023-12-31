#!/usr/bin/python3
# Displays all cities of a given state from the
# states table of the database hbtn_0e_4_usa.
# Safe from SQL injections.
# Usage: ./5-filter_cities.py <mysql username> \
#                             <mysql password> \
#                             <database name> \
#                             <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM `cities` as `cursor` \
                INNER JOIN `states` as `s` \
                   ON `cursor`.`state_id` = `s`.`id` \
                ORDER BY `cursor`.`id`"
    )
    print(", ".join([ct[2] for ct in cursor.fetchall() if ct[4] == sys.argv[4]]))
