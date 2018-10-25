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


@pytest.mark.wip
def test_merge_data():

    def fetch_subjects(data, source_folder, train_or_test):
        subjects = fetch_additional_data(source_folder, 'subject_{}.txt', train_or_test)
        data['subject'] = subjects[0]
        return data

    def fetch_activities(data, source_folder, train_or_test):
        labels = descriptive_activities(source_folder, train_or_test)
        data['activity'] = labels[1]
        return data
     
    def fetch_main_data(source_folder, train_or_test):
        raw_train_data = fetch_data(source_folder, train_or_test)
        features = fetch_additional_data(source_folder, 'features.txt')
        data = rename_columns(raw_train_data, features[1])
        return data

    train_data = fetch_main_data(SOURCE_FOLDER, 'train')
    data_with_subjects = fetch_subjects(train_data, SOURCE_FOLDER, 'train')
    data_with_subjects_and_activities = fetch_activities(train_data, SOURCE_FOLDER, 'train') 
    test_data = fetch_main_data(SOURCE_FOLDER, 'test')
    assert len(data_with_subjects_and_activities.columns) == 563
    assert 'subject' in data_with_subjects_and_activities.columns
