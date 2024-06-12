import pytest
import pandas as pd
import os
from ml.data import process_data
from ml.model import train_model
from sklearn.linear_model import LogisticRegression

# Create fixture to load data.

@pytest.fixture
def load_data():
    """
    Load the dataset
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data


# Implement the first test.
def test_dataset_info(load_data):
    """
    Test to see dataset form and size

    Parameters:
        load_data: Census dataset
    """
    data = load_data
    assert isinstance(data, pd.DataFrame), "Data is not a pandas DataFrame"
    assert data.shape[0] > 0, "Data does not contain any rows"
    assert data.shape[1] > 0, "Data does not contain any columns"


# Implement the second test.
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
    assert X_train.shape[0] > 0, "Processed data does not contain any rows"
    assert y_train.shape[0] > 0, "Processed labels fo not contain any rows"

#Implement the third test
def test_model_type(load_data):
    """
    Test to see if model is a Logistic Regression model.

    Parameters:
        load_data: Census dataset
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
        data, categorical_features=cat_features, label='salary', training=True
    )

    model = train_model(X_train, y_train)
    assert isinstance(model, LogisticRegression), "Model is not a Logistic Regression instance"