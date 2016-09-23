__author__ = 'ljd'
import re

str_a = """
[DIR] [162]12.2.1.2.0-160628.1792528/ 29-Jun-2016 03:18 -
"""

p = re.compile(r'.*\[\d{1,}\](\d{2}.\d.\d.\d.\d-\d{6}.\d{7})/')
m = p.search(str_a)
if m:
    print m.group(1)