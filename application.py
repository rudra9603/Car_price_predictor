from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv("cleaned car data.csv")


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    # Create DataFrame with input data
    data = [[car_model, company, year, kms_driven, fuel_type]]
    columns = ['name', 'company', 'year', 'kms_driven', 'fuel_type']
    data_df = pd.DataFrame(data, columns=columns)

    try:
        print("Input data:")
        print(data_df)

        # Perform prediction using the model and transformed input data
        prediction = model.predict(data_df)
        result = np.round(prediction[0], 2)
        print("Prediction result:")
        print(result)

        return result
    except Exception as e:
        print("Error occurred:", e)
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
