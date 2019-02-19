# -*- coding: utf-8 -*-
import csv

class CsvReader(object):
    @staticmethod
    def read():
        filename = "input.csv"
        dict_list = []
        reader = csv.DictReader(open(filename, "r"))
        for line in reader:
            dict_list.append(line)
        return dict_list
