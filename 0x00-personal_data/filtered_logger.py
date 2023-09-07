#!/usr/bin/env python3
import logging
import re


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super(RedactingFormatter,
                        self).format(record)
        return filter_datum(self.fields,
                            self.REDACTION, message, self.SEPARATOR)


def filter_datum(fields, redaction, message, separator):
    regex = re.compile(f'({separator.join(map(re.escape, fields))})')
    return regex.sub(redaction, message)
