"""
Test module for tidy.data_transformation module.
"""
import pytest
from tidy.data_io import fetch_additional_data, fetch_data
from tidy.data_transformation import rename_columns, descriptive_activities
from . import SOURCE_FOLDER


def test_read_and_rename_columns_for_train_data():
    features = fetch_additional_data(SOURCE_FOLDER, 'features.txt')
    assert features.shape == (561, 2)
    data = fetch_data(SOURCE_FOLDER, 'train')
    train_data = rename_columns(data, features[1])
    assert train_data.shape == (7352, 561)
    assert list(train_data.columns) == list(features[1])


def test_create_descriptive_activities():
    labels = descriptive_activities(SOURCE_FOLDER, 'train')
    assert labels.loc[0] == 'STANDING'
