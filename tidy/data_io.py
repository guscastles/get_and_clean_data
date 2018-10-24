"""
IO module for the data analysis project.
"""
import io
import zipfile
import urllib
import requests
import pandas as pd


def fetch_remote_data(url):
    zip_file = download_data(url)
    unzip_file(zip_file)
    return zip_file


def download_data(url):

    def _get_file_name():
        unquoted = urllib.parse.unquote(url)
        return unquoted.split('/')[-1]

    data_file = _get_file_name()
    response = requests.get(url)
    with open(data_file, "wb") as output_file:
        output_file.write(response.content)

    return data_file


def unzip_file(file_name):
    with open(file_name, 'rb') as input_file:
        zip_file = zipfile.ZipFile(io.BytesIO(input_file.read()))
        zip_file.extractall()


def fetch_additional_data(source_folder, file_name, train_or_test=''):
    return pd.read_table('/'.join([source_folder, train_or_test, file_name.format(train_or_test)]),
                         delim_whitespace=True,
                         header=None)


def fetch_data(source_folder, train_or_test):
    return pd.read_fwf('/'.join([source_folder, train_or_test, f'X_{train_or_test}.txt']),
                       widths=[16 for _ in range(561)],
                       header=None)
