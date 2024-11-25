import json

class JSONHandler:
    @staticmethod
    def process_json(json_data: dict):
        required_keys_identification = [
            "transformer_id",
            "location"
        ]
        required_keys_chroma_data = [
            "analysis_timestamp",
            "H2",
            "CO",
            "CO2",
            "C2H4",
            "C2H6",
            "CH4",
            "C2H2"
        ]

        def validate_keys(data, required_keys):
            missing_keys = [key for key in required_keys if key not in data]
            empty_values = [
                key for key in required_keys 
                if key in data and (data[key] is None or data[key] == "")
            ]
            return not missing_keys and not empty_values

        if not validate_keys(json_data["transformer_identification"], required_keys_identification):
            raise ValueError("The transformer ID and its location must be defined!")
        if not validate_keys(json_data["chromatography_data"], required_keys_chroma_data):
            raise ValueError("The analysis date and the gases values must be defined!")

        return json_data
