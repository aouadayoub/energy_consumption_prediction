from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime, timedelta
import pickle
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))  # Load your model

def predict_energy_consumption(start_date_str, end_date_str):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid datetime format. Please use YYYY-MM-DD.", None

    if start_date > end_date:
        return "Start date cannot be after end date.", None

    dates = []
    predictions = []
    current_date = start_date

    if start_date == end_date:  # Predicting for a single day
        hours = list(range(24))
        for hour in hours:
            features = {
                'hour': hour,
                'dayofweek': start_date.weekday(),
                'quarter': (start_date.month - 1) // 3 + 1,
                'month': start_date.month,
                'year': start_date.year,
                'dayofyear': start_date.timetuple().tm_yday,
                'dayofmonth': start_date.day,
            }
            input_df = pd.DataFrame([features])
            prediction = model.predict(input_df)[0]
            predictions.append(prediction)
            dates.append(hour)
        plt.xlabel("Hour of Day")

    else:  
        while current_date <= end_date:
            dates.append(current_date)
            features = {
                'hour': current_date.hour,
                'dayofweek': current_date.weekday(),
                'quarter': (current_date.month - 1) // 3 + 1,
                'month': current_date.month,
                'year': current_date.year,
                'dayofyear': current_date.timetuple().tm_yday,
                'dayofmonth': current_date.day,
            }
            input_df = pd.DataFrame([features])
            prediction = model.predict(input_df)[0]
            predictions.append(prediction)
            current_date += timedelta(days=1)
        plt.xlabel("Date")
        plt.xticks(rotation=45)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, predictions)
    plt.ylabel("Predicted Energy Consumption")
    plt.title("Predicted Energy Consumption over Time")
    plt.tight_layout()

    # Save plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()  

    return "Prediction successful", plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    plot_url = None 

    if request.method == 'POST':
        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']
        message, plot_url = predict_energy_consumption(start_date_str, end_date_str)

    return render_template('index.html', message=message, plot_url=plot_url) 
@app.route('/results', methods=['POST'])
def show_results():
    start_date_str = request.form['start_date']
    end_date_str = request.form['end_date']
    message, plot_url = predict_energy_consumption(start_date_str, end_date_str)

    return render_template('results.html', message=message, plot_url=plot_url) 


if __name__ == '__main__':
    app.run(debug=True)