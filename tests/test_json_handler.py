import pytest
from ingestion.json_handler import JSONHandler
import datetime

INPUT_DATA = {
        "transformer_identification": {
            "transformer_id": "T1234",
            "transformer_name": "LV Transformer 12",
            "location": "Substation 31",
            "installation_date": datetime.date('2021', '12', '25')
        }, 
        "chromatography_data":{
            "analysis_timestamp": datetime.datetime('2024', '11', '25', '14', '46', '00'),
            "H2": 10,
            "CO": 25,
            "CO2": 335,
            "C2H4": 12,
            "C2H6": 10,
            "CH4": 4,
            "C2H2": 5,
            "oil_acidity": 0.04,
            "oil_temperature": 62,
            "oil_pressure": 1.02
        }, 
        "environment_parameters": {
            "environment_temperature": 32,
            "environment_humidity": 53,
            "atmospheric_pressure": 1.06
        },
        "history_and_observations":{
            "last_maintence_date": datetime.date('2023', '08', '12'),
            "maintenance_done": "Oil change",
            "observations": "No faults detected"
        }
    }

def test_process_full_json_success():
    assert JSONHandler.process_json(INPUT_DATA) == INPUT_DATA

def test_process_required_json():
    mod_data = INPUT_DATA
    del mod_data['transformer_identification']['transformer_name']
    del mod_data['transformer_identification']['installation_date']
    del mod_data['chromatography_data']['oil_acidity']
    del mod_data['chromatography_data']['oil_temperature']
    del mod_data['chromatography_data']['oil_pressure']
    del mod_data['environment_parameters']
    del mod_data['history_and_observations']
    assert JSONHandler.process_json(mod_data) == mod_data

def test_process_missing_required_json_key():
    mod_data = INPUT_DATA
    del mod_data['transformer_identification']['transformer_id']
    with pytest.raises(ValueError, match="The transformer ID and it's location must be defined!"):
        JSONHandler.process_json(mod_data)

def test_process_missing_json_value():
    mod_data = INPUT_DATA
    mod_data['transformer_identification']['transformer_id'] = ""
    with pytest.raises(ValueError, match="The transformer ID and it's location must be defined!"):
        JSONHandler.process_json(mod_data)
