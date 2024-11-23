import pytest
from ingestion.excel_reader import ExcelReader

def test_read_excel():
    data = ExcelReader.read_excel("tests/samples/sample_spreadsheet_v1.xlsx")
    params_data = data[0]
    assert len(data) == 6

    assert params_data["transformer_identification"]["transformer_id"] == "T01467"
    assert params_data["transformer_identification"]["transformer_name"] == "UHV transformer 3"
    assert params_data["transformer_identification"]["location"] == "Substation 351"
    assert str(params_data["transformer_identification"]["installation_date"]) == "2019-06-24"
    assert str(params_data["chromatography_data"]["analysis_timestamp"]) == "2024-11-19T13:35:00"
    assert params_data["chromatography_data"]["H2"] == 2
    assert params_data["chromatography_data"]["CO"] == 120
    assert params_data["chromatography_data"]["CO2"] == 320
    assert params_data["chromatography_data"]["C2H4"] == 50
    assert params_data["chromatography_data"]["C2H6"] == 20
    assert params_data["chromatography_data"]["CH4"] == 5
    assert params_data["chromatography_data"]["C2H2"] == 2
    assert params_data["chromatography_data"]["oil_acidity"] == 0.02
    assert params_data["chromatography_data"]["oil_temperature"] == 65
    assert params_data["chromatography_data"]["oil_pressure"] == 1.01
    assert params_data["environment_parameters"]["environment_temperature"] == 30
    assert params_data["environment_parameters"]["environment_humidity"] == 60
    assert params_data["environment_parameters"]["atmospheric_pressure"] == 1.01
    assert str(params_data["history_and_observations"]["last_maintence_date"]) == "2023-12-12"
    assert params_data["history_and_observations"]["maintenance_done"] == "Oil Change"
    assert params_data["history_and_observations"]["observations"] == "No faults detected"

    