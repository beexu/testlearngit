# -*- coding: UTF-8 -*-
import re

string = 'b123.a223.a223.'
print(re.match('a\d{3}.', string))
print(re.search('a\d{3}.', string))
print(re.findall('a\d{3}.', string))
print(re.split(r'\.', string))
print(re.sub('a\d{2}','g', string))
# test learn
