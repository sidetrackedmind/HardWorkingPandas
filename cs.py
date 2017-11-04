import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def make_lookup_set(csvfile):
    """return lookup set based on major and minor in real estate data"""
    ids = []
    f = open(csvfile, 'r')
    has_header = csv.Sniffer().has_header(f.read(1024))
    f.seek(0)  # rewind
    reader = csv.reader(f)
    if has_header:
        next(reader)
    for row in reader:
        ids.append(str(row[0]) + str(row[1]))
    f.close()
    ids = set(ids)
    return ids

def get_rel_prices(csvfile, id_set, min_sale_price):
    """return dict of prices for a year"""
    prices = defaultdict(list)
    f = open(csvfile, 'r')
    has_header = csv.Sniffer().has_header(f.read(1024))
    f.seek(0)  # rewind
    reader = csv.reader(f)
    if has_header:
        next(reader)
    for row in reader:
        if str(row[1]) + str(row[2]) in id_set and int(row[4]) > min_sale_price:
            prices[int(row[3][-4:])].append(int(row[4]))
    f.close()
    return prices

def get_price_summary(price_dict, summary_stat):
    """return list of tuples of (year, summary stat) for
    all years in price_dict"""
    summary_list = []
    for key in price_dict:
        summary_list.append(tuple([key, summary_stat(price_dict[key])]))
    return summary_list
