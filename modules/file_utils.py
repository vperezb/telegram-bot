"""General functions usefull inside and out the project
"""

__author__ = '@vperezb'

import os
import json

import requests

import yaml
import csv


def read_file(filename, mode='r'):
    with open(filename, 'r') as myfile:
        return myfile()


def open_file(filename, mode='r'):
    with open(filename, mode) as openfile:
        return openfile.read()


def write_file(content, filename, mode='w'):
    with open(filename, mode) as openfile:
        return openfile.write(content)


def read_yml(filename):
    with open(filename, 'r') as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.FullLoader)


def write_file_from_dict(input_dict, filename, mode='w'):
    content = json.dumps(input_dict, sort_keys=True, separators=(',', ':'))
    return write_file(content, filename)


def read_json_file(filename, mode):
    return json.loads(open_file(filename, mode))


def read_csv_to_dict_list(filename):
    with open(filename, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def read_file_to_list(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]