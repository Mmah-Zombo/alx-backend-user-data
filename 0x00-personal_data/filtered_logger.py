#!/usr/bin/env python3
"""regex-ing"""
import re
import logging

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(?<=\b' + separator + r'|\b)(' + '|'.join(fields) + r')=[^' + separator + r']*', redaction, message)

fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

for message in messages:
    logger.info(filter_datum(fields, 'xxx', message, ';'))
