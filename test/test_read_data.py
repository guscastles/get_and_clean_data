import pandas as pd


SOURCE_FOLDER = 'UCI HAR Dataset'


def fetch_additional_data(source_folder, file_name, data_type=''):
    return pd.read_table('/'.join([source_folder, data_type, file_name.format(data_type)]),
                         delim_whitespace=True,
                         header=None)


def fetch_data(source_folder, data_type):
    return pd.read_fwf('/'.join([source_folder, data_type, f'X_{data_type}.txt']),
                       widths=[16 for _ in range(561)],
                       header=None)


def test_read_train_data():
    features = fetch_additional_data(SOURCE_FOLDER, 'features.txt')
    assert features.shape == (561, 2)
    data = fetch_data(SOURCE_FOLDER, 'train')
    train_data = data.rename(features[1], axis=1)
    assert train_data.shape == (7352, 561)
    assert list(train_data.columns) == list(features[1])


def test_read_subjects():
    train_subjects = fetch_additional_data(SOURCE_FOLDER, 'subject_{}.txt', 'train')
    assert train_subjects.shape == (7352, 1)
    test_subjects = fetch_additional_data(SOURCE_FOLDER, 'subject_{}.txt', 'test')
    assert test_subjects.shape == (2947, 1)
