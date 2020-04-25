# -*- coding: UTF-8 -*-
import re


def test1():
    f = open('/Users/beexu/Documents/wengao/requests/learnpython/t.log', 'r')
    num = 0
    topic1 = []
    topic2 = []
    for line in f.readlines():
        # print(line)
        match = re.search('c: (\S*)', line)
        num = num + 1
        # print(num)
        # print(match.groups(num)[0])
        if match.groups(num)[0] == 'KAFKA_PRODUCER_TOPIC':
            match1 = re.search('s: (\S*)', line)
            # print(match1.groups(num)[0])
            topic1.append(match1.groups(num)[0])
            # print(topic1)
        else:
            match1 = re.search('s: (\S*)', line)
            topic2.append(match1.groups(num)[0])
            # print(topic2)
    dict = {}
    dict['KAFKA_PRODUCER_TOPIC'] = topic1
    dict['__consumer_offsets'] = topic2
    print(dict)


if __name__ == '__main__':
    test1()
