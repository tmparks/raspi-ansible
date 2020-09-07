#!/usr/bin/env python3
import bs4
import math
import sys
import urllib.parse
import urllib.request

def to_db(x) :
    return 10.0 * math.log10(x)

def from_db(x) :
    return math.pow(10.0, x / 10.0)

def sum_values(table, row_start, row_stop, col) :
    """Sum values in given rows and column"""
    sum = 0.0
    row_list = table.find_all('tr')
    for row in row_list[row_start:row_stop] :
        col_list = row.find_all('td')
        sum += from_db(float(col_list[col].string))
    return to_db(sum)

# Set default values
host = '192.168.0.1'
user = 'admin'
password = 'motorola'
downstream_power = 0.0
upstream_power = 0.0

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
    downstream_power = round(sum_values(table_list[3], 1, 9, 5), 2)
    upstream_power = round(sum_values(table_list[4], 1, 5, 6), 2)

print('downstream:{0} upstream:{1}'.format(downstream_power, upstream_power))
