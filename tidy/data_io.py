"""
IO module for the data analysis project.
"""
import os
import requests
import io
import zipfile
import urllib


def fetch_data(url):
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
        zip_file = input_file.read()
        z = zipfile.ZipFile(io.BytesIO(zip_file))
        z.extractall()



