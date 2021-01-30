#!/usr/bin/env python3
import bs4
import math
import sys
import urllib.parse
import urllib.request

def to_db(x) :
    """Convert from linear power to decibels"""
    return 10.0 * math.log10(x)

def from_db(x) :
    """Convert from decibels to linear power"""
    return math.pow(10.0, x / 10.0)

def sum_db_values(table, row_start, row_stop, col) :
    """Sum values in given rows and column"""
    sum = 0.0
    for row in range(row_start, row_stop) :
        sum += from_db(float(get_value(table, row, col)))
    return to_db(sum)

def get_value(table, row, col) :
    """Get value in given row and column"""
    return table.find_all('tr')[row].find_all('td')[col].string

# Set default values
host = '192.168.0.1'
user = 'admin'
password = 'motorola'
downstream_power = 0.0
upstream_power = 0.0
corrected_errors = 0
uncorrected_errors = 0

# Get command line arguments
if len(sys.argv) > 1 :
    host = sys.argv[1]
if len(sys.argv) > 2:
    user = sys.argv[2]
if len(sys.argv) > 3:
    password = sys.argv[3]

# Log in
post_data = { 'loginUsername': user, 'loginPassword': password }
urllib.request.urlopen(
    'http://' + host + '/goform/login',
    data = urllib.parse.urlencode(post_data).encode())

# Request connection status
with urllib.request.urlopen('http://' + host + '/MotoConnection.asp') as response:
    soup = bs4.BeautifulSoup(response, 'html.parser')
    table_list = soup.find_all('table', class_='moto-table-content')
    downstream_power = round(sum_db_values(table_list[3], 1, 9, 5), 2)
    upstream_power = round(sum_db_values(table_list[4], 1, 5, 6), 2)
    corrected_errors = int(get_value(table_list[3], 9, 7))
    uncorrected_errors = int(get_value(table_list[3], 9, 8))

print('downstream:{0} upstream:{1} corrected:{2} uncorrected:{3}'.format(
    downstream_power, upstream_power, corrected_errors, uncorrected_errors))
