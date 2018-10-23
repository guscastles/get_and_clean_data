import pandas as pd


def test_read_train_data():
    source_folder = 'UCI HAR Dataset'
    columns = pd.read_table('/'.join([source_folder, 'features.txt']), delim_whitespace=True, header=None)
    assert columns.shape == (561, 2)
    data = pd.read_fwf('/'.join([source_folder, 'train', 'X_train.txt']), widths=[16 for _ in range(561)], header=None)
    assert data.shape == (7352, 561)
