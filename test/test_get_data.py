import pytest
import os
import shutil as sh
import requests
import io, zipfile


def fetch_data(url):
    zip_file = download_data(url)
    unzip_file(zip_file)
    return zip_file


def download_data(url):
    zip_file = "dataset.zip"
    if not os.path.isfile(zip_file):
        response = requests.get(url)
        with open(zip_file, "wb") as output_file:
            output_file.write(response.content)

        return zip_file


def unzip_file(file_name):
    with open(file_name, 'rb') as input_file:
        zip_file = input_file.read()
        z = zipfile.ZipFile(io.BytesIO(zip_file))
        z.extractall()


@pytest.mark.skip
def test_get_data_from_url():
    if os.path.isfile("dataset.zip"):
        sh.os.unlink("dataset.zip")
    url = "https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip"
    zip_file = download_data(url)
    assert os.path.isfile(zip_file)


def test_unzip_data_file():
    sh.rmtree("UCI HAR Dataset")
    assert os.path.isfile("dataset1.zip")
    unzip_file("dataset1.zip")
    assert os.path.isdir("UCI HAR Dataset")

