import json

class JSONHandler:
    @staticmethod
    def process_json(json_data):
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

        if not all(key in json_data["transformer_identification"] for key in required_keys_identification):
            raise ValueError("The transformer ID and it's location must be defined!")
        if not all(key in json_data["chromatography_data"] for key in required_keys_chroma_data):
            raise ValueError("The analysis date and the gases values must be defined!")
        return json_data