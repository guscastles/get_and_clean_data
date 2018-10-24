import pytest
import os
import shutil as sh
import tidy.data_io as io
from . import SOURCE_FOLDER


URL = "https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip"
UNZIPED_FOLDER = "UCI HAR Dataset"
ZIPED_FILE = "dataset1.zip"


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_download_file_from_url():
    zip_file = io.download_data(URL)
    assert os.path.isfile(zip_file)
    sh.os.unlink(zip_file)


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_unzip_data_file():
    assert os.path.isfile(ZIPED_FILE)
    io.unzip_file(ZIPED_FILE)
    assert os.path.isdir(UNZIPED_FOLDER)
    sh.rmtree(UNZIPED_FOLDER)


@pytest.mark.skip(reason="Skipped to enhance test performance")
def test_fetch_data():
    data_file = io.fetch_remote_data(URL)
    assert os.path.isfile(data_file)
    sh.os.unlink(data_file)


def test_read_subjects():
    train_subjects = io.fetch_additional_data(SOURCE_FOLDER, 'subject_{}.txt', 'train')
    assert train_subjects.shape == (7352, 1)
    test_subjects = io.fetch_additional_data(SOURCE_FOLDER, 'subject_{}.txt', 'test')
    assert test_subjects.shape == (2947, 1)


def test_read_activities():
    activities = io.fetch_additional_data(SOURCE_FOLDER, 'activity_labels.txt')
    assert activities.shape == (6, 2)

