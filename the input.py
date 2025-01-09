import pandas as pd
from datetime import datetime, timedelta
import pickle
import matplotlib.pyplot as plt

model = pickle.load(open('model.pkl', 'rb'))

def predict_energy_consumption(start_date_str, end_date_str):


    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid datetime format. Please use YYYY-MM-DD."

    if start_date > end_date:
        return "Start date cannot be after end date."

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
    else:  # Predicting for a period longer than one day
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

    # Create the plot (outside the loop)
    plt.figure(figsize=(10, 6))  # Moved outside the loop
    plt.plot(dates, predictions)
    plt.ylabel("Predicted Energy Consumption")
    plt.title("Predicted Energy Consumption over Time")
    plt.tight_layout()
    plt.show()

while True:
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    result = predict_energy_consumption(start_date_str, end_date_str)
    if result is not None: 
        print(result)