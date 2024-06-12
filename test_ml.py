import pytest
import pandas as pd
import os
from ml.data import process_data
from ml.model import train_model
from sklearn.linear_model import LogisticRegression

# Implement the first test.

@pytest.fixture
def load_data():
    """
    Load the dataset
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data


# Implement the second test.
def dataset_info():
    """
    Test to see dataset form and size

    Parameters:
        load_data: Census dataset
    """
    assert isinstance(data, pd.DataFrame), "Data is not a pandas Dataframe"
    assert data.shape[0] > 0, "Data does not contain any rows"
    assert data.shape[1] > 0, "Data does not contain any columns"


# Implement the third test.
@pytest.fixture
def test_data_process(load_data):
    """
    Tests data processing
    """
    data = load_data

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_train, y_train, encoder, lb = process_data(
        data, categorical_features = cat_features, label='salary', training=True
    )
    return X_train, y_train, encoder, lb
