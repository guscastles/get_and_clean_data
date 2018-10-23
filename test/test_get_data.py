import pytest
import os
import shutil as sh
from tidy.data_io import download_data, unzip_file, fetch_data


URL = "https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip"
UNZIPED_FOLDER = "UCI HAR Dataset"
ZIPED_FILE = "dataset1.zip"


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_download_file_from_url():
    zip_file = download_data(URL)
    assert os.path.isfile(zip_file)
    sh.os.unlink(zip_file)


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_unzip_data_file():
    assert os.path.isfile(ZIPED_FILE)
    unzip_file(ZIPED_FILE)
    assert os.path.isdir(UNZIPED_FOLDER)
    sh.rmtree(UNZIPED_FOLDER)


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_fetch_data():
    data_file = fetch_data(URL)
    assert os.path.isfile(data_file)
    sh.os.unlink(data_file)

