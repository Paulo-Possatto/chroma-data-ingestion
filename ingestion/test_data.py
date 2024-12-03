import random
import datetime

class TestData:
    @staticmethod
    def get_test_data():
        return {
            "transformer_identification": {
                "transformer_id": TestData.generate_test_transformer_id(),
                "transformer_name": "Test transformer",
                "location": TestData.generate_test_location(),
                "installation_date": TestData.generate_test_installation_date()
            }, 
            "chromatography_data":{
                "analysis_timestamp": TestData.generate_analysis_timestamp(),
                "H2": random.randint(0, 1000),
                "CO": random.randint(0, 1000),
                "CO2": random.randint(0, 1000),
                "C2H4": random.randint(0, 1000),
                "C2H6": random.randint(0, 1000),
                "CH4": random.randint(0, 1000),
                "C2H2": random.randint(0, 1000),
                "oil_acidity": round(random.uniform(0, 0.5), 2),
                "oil_temperature": random.randint(40, 80),
                "oil_pressure": round(random.uniform(1, 1.5), 2)
            }, 
            "environment_parameters": {
                "environment_temperature": random.randint(10, 40),
                "environment_humidity": random.randint(40, 100),
                "atmospheric_pressure": round(random.uniform(1, 1.2), 2)
            },
            "history_and_observations":{
                "last_maintenance_date": TestData.generate_test_maintenance_date(),
                "maintenance_done": TestData.generate_test_maintenance_done(),
                "observations": "Test observation"
            }
        }
    
    def generate_test_transformer_id():
        generated_id = ""
        for _ in range(1, 5):
            generated_id += str(random.randint(1, 100))
        return "T{code}".format(code = generated_id)
    
    def generate_test_location():
        return "Substation {code}".format(code=str(random.randint(1, 500)))
    
    def generate_test_installation_date():
        year = random.randint(1990, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return datetime.date(year, month, day).strftime('%Y-%m-%d %H:%M:%S')
    
    def generate_analysis_timestamp():
        year = random.randint(2018, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return datetime.date(year, month, day).strftime('%Y-%m-%dT%H:%M:%S')
    
    def generate_test_maintenance_date():
        year = random.randint(2020, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return datetime.date(year, month, day).strftime('%Y-%m-%d %H:%M:%S')
    
    def generate_test_maintenance_done():
        reason = ["Oil Change", "Cleaning", "Verification", "Test Electrical Parameters", "Oil Analysis", "Replace Worn/Damaged Parts", "Repair/Replace Faulty Component(s)",
                  "Cleaning/Replacing Filters", "Monitor Operating Parameters"]
        return random.choice(reason)
