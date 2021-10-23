#!/usr/bin/env python3
import math
import re
import requests
import sys

def to_db(x) :
    """Convert from linear power to decibels"""
    return 10.0 * math.log10(x)

def from_db(x) :
    """Convert from decibels to linear power"""
    return math.pow(10.0, x / 10.0)

def sum_db(values) :
    """Sum of decibel values"""
    sum = 0.0
    for v in values :
        sum += from_db(float(v))
    return to_db(sum) if sum > 0.0 else 0.0

def sum_int(values) :
    """Sum of integer values"""
    sum = 0
    for v in values :
        sum += int(v)
    return sum

def get_column(table, col) :
    """Get values in given column"""
    values = list()
    for row in range(len(table)) :
        if table[row][1] == 'Locked' :
            values.append(table[row][col])
    return values

def get_table(line, sep='|') :
    """Get table of separated values"""
    tokens = line.split(sep)
    rows = int(tokens[0]) # First token gives number of rows
    cols = (len(tokens)-1) // rows
    table = list()
    for r in range(rows) :
        start = 1 + (r * cols)
        stop = start + cols
        table.append(tokens[start:stop])
    return table

# Get command line arguments
host = sys.argv[1] if len(sys.argv) > 1 else '192.168.100.1'
user = sys.argv[2] if len(sys.argv) > 2 else 'admin'
password = sys.argv[3] if len(sys.argv) > 3 else 'password'

# Set default values
downstream_power = 0.0
upstream_power = 0.0
corrected_errors = 0
uncorrected_errors = 0

session = requests.Session()
session.auth = (user, password)
url = 'http://' + host + '/DocsisStatus.htm'
_ = session.get(url) # First request obtains authentication cookie
response = session.get(url, stream=True) # Second request gets actual content
up_expr = re.compile(r"^.*var tagValueList = '(.*ATDMA.*)';$")
down_expr = re.compile(r"^.*var tagValueList = '(.*QAM256.*)';$")
for line in response.iter_lines() :
    match = up_expr.match(line.decode('utf8'))
    if match :
        table = get_table(match.group(1))
        upstream_power = sum_db(get_column(table, 6))
    match = down_expr.match(line.decode('utf8'))
    if match :
        table = get_table(match.group(1))
        downstream_power = sum_db(get_column(table, 5))
        corrected_errors = sum_int(get_column(table, 7))
        uncorrected_errors = sum_int(get_column(table, 8))

print('downstream:{0} upstream:{1} corrected:{2} uncorrected:{3}'.format(
    round(downstream_power, 2),
    round(upstream_power, 2),
    corrected_errors,
    uncorrected_errors))
