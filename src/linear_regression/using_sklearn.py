import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


def run():
    data = get_data()
    house_data = clean_data(data)
    X = extract_features(house_data)
    y = house_data.price

    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=10, random_state=2)

    model = LinearRegression()
    model.fit(train_X, train_y)

    calculate_mas_error(model, val_X, val_y)


def calculate_mas_error(model, val_X, val_y):
    val_predictions = model.predict(val_X)
    mas_err = mean_absolute_error(val_y, val_predictions)
    print("Mean absolute error : ", mas_err)


def get_data():
    file_path = '/Users/brillap/downloads/kc_house_data.csv'
    data = pd.read_csv(file_path)
    return data


def extract_features(data):
    features = [
        'bedrooms',
        'bathrooms',
        'sqft_living',
        'sqft_lot',
        'floors',
        'grade',
        'sqft_above',
        'sqft_basement',
        'yr_built',
        'yr_renovated',
        'sqft_living15',
        'sqft_lot15']
    X = data[features]
    return X


def clean_data(data):
    cleaned_data = data
    cleaned_data['sqft_above'].fillna((data['sqft_above'].mean()), inplace=True)
    return cleaned_data


if __name__ == "__main__":
    run()
