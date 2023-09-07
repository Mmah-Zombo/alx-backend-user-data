#!/usr/bin/env python3
"""regex-ing"""
import re


def filter_datum(fields, redaction, message, separator):
    """the filter_datum function"""
    regex = re.compile(f'({separator.join(map(re.escape, fields))})')
    return regex.sub(redaction, message)
