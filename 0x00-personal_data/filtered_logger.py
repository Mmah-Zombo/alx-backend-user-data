#!/usr/bin/env python3
"""regex-ing"""
import re


def filter_datum(fields, redaction, message, separator):
    """the filter_datum function"""
    regex = '|'.join(map(re.escape, fields))
    return re.sub(f'({regex}){re.escape(separator)}',
                  redaction + separator, message)
