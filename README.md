# Car Price Prediction Model

## Overview
An end-to-end car price prediction model developed using the Quikr Cars dataset, leveraging linear regression to estimate car prices with 85% accuracy.

## Features
- **Accurate Price Prediction**: 85% accuracy using linear regression
- **Data Preprocessing**: Comprehensive data cleaning and feature selection
- **User-Friendly Interface**: Flask-based web application
- **End-to-End Machine Learning Solution**

## Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Flask
- HTML/CSS
- Jupyter Notebook

## Dataset
The Quikr Cars dataset includes features such as:
- Car Name
- Year
- Kilometers Driven
- Fuel Type
- Transmission
- Owner Type
- Mileage
- Engine
- Power
- Seats
- Price (Target Variable)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
```bash
python app.py
```

### 4. Access the Web Interface
Open your browser and navigate to the local server address

## How to Use
1. Open the web interface
2. Enter car details
3. Click "Predict" to get the estimated car price

## Project Structure
```
car-price-predictor/
├── app.py           # Flask application
├── model/           # Trained model and preprocessing files
│   ├── model.pkl
│   └── preprocessor.pkl
├── templates/       # HTML templates
│   └── index.html
├── static/          # CSS files
│   └── styles.css
├── notebooks/       # Jupyter notebooks
│   └── car_price_prediction.ipynb
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

## Future Improvements
- Implement advanced ML models (Random Forest, Gradient Boosting)
- Expand dataset features
- Cloud platform deployment

## Contributions
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT License

## Contact
- **Name**: Rudra Kumar
- **Email**: rudra9603m@gmail.com

---
