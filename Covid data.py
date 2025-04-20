import csv
from datetime import datetime
import matplotlib.pyplot as plt

covid_data = {}

def add_daily_data():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")
    cases = int(input("New cases: "))
    recoveries = int(input("Recoveries: "))
    deaths = int(input("Deaths: "))
    
    if city not in covid_data:
        covid_data[city] = []
    
    covid_data[city].append({
        "date": date,
        "cases": cases,
        "recoveries": recoveries,
        "deaths": deaths
    })
    print("Data added.")

def analyze_risk_zones():
    for city, records in covid_data.items():
        active_cases = sum([r["cases"] - r["recoveries"] - r["deaths"] for r in records])
        status = "Green"
        if active_cases > 100:
            status = "Red"
        elif active_cases > 20:
            status = "Orange"
        print(f"{city}: {active_cases} active cases → Risk: {status}")

def plot_city_trend():
    city = input("Enter city name: ").title()
    if city not in covid_data:
        print("No data available.")
        return
    
    dates = [datetime.strptime(r["date"], "%Y-%m-%d") for r in covid_data[city]]
    cases = [r["cases"] for r in covid_data[city]]
    recoveries = [r["recoveries"] for r in covid_data[city]]
    deaths = [r["deaths"] for r in covid_data[city]]

    plt.plot(dates, cases, label="Cases")
    plt.plot(dates, recoveries, label="Recoveries")
    plt.plot(dates, deaths, label="Deaths")
    plt.title(f"COVID Trend in {city}")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()
    plt.show()

def predict_hotspots():
    print("Potential Hotspots (cities with increasing trend):")
    for city, records in covid_data.items():
        if len(records) >= 3:
            last_three = records[-3:]
            if all(last_three[i]["cases"] < last_three[i+1]["cases"] for i in range(2)):
                print(f"{city} - Increasing case trend")

def import_csv(filename='covid_data.csv'):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                city, date, cases, recoveries, deaths = row
                if city not in covid_data:
                    covid_data[city] = []
                covid_data[city].append({
                    "date": date,
                    "cases": int(cases),
                    "recoveries": int(recoveries),
                    "deaths": int(deaths)
                })
        print("Data imported successfully.")
    except FileNotFoundError:
        print("CSV file not found.")

def menu():
    while True:
        print("\n1. Add Daily Data\n2. Analyze Risk Zones\n3. Show City Trend\n4. Predict Hotspots\n5. Import CSV\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1': add_daily_data()
        elif choice == '2': analyze_risk_zones()
        elif choice == '3': plot_city_trend()
        elif choice == '4': predict_hotspots()
        elif choice == '5': import_csv()
        elif choice == '6': break
        else: print("Invalid choice.")

menu()
