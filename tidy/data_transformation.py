"""
Transformation module for the data analysis project.
"""
import tidy.data_io as io


def rename_columns(data, column_names):
    return data.rename(column_names, axis=1)


def descriptive_activities(source_folder, train_or_test):
    raw_train_labels = io.fetch_additional_data(source_folder, 'y_{}.txt', train_or_test)
    labels = io.fetch_additional_data(source_folder, 'activity_labels.txt')
    indexed_labels = labels.set_index(0)
    return raw_train_labels.loc[:, 0].map(indexed_labels[1])
