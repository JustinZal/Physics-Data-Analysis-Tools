import numpy as np
import csv


def read_csv_data(file_path):
    file = open(file_path, 'r')
    csv_file = csv.DictReader(file)

    elements = {}

    for row in csv_file:
        if len(elements.keys()) == 0:
            for k in row.keys():
                elements[k] = []

        for k in row.keys():
            elements[k].append(float(row[k]))

    return elements
