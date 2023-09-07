#!/usr/bin/env python3
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    # ...

# Other functions as before...

def main():
    logger = get_logger()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    
    for row in cursor.fetchall():
        filtered_row = {key: '***' if key in PII_FIELDS else value for key, value in row.items()}
        logger.info("Filtered fields:\n%s", "\n".join(filtered_row.keys()))
        logger.info("Data:\n%s", filtered_row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
