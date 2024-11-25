import openpyxl
from datetime import datetime

class ExcelReader:

    @staticmethod
    def read_excel(file_path:str):

        FIRST_ROW = 7

        workbook = openpyxl.load_workbook(filename=file_path)
        sheet = workbook.active
        data = []

        for row in sheet.iter_rows(min_row=FIRST_ROW, values_only=True):
            #TODO: Verificar turnery operation ...
            if row[4] != "" and row[5] != "":
                analysis_timestamp = datetime.strptime(str(row[4]).split(" ")[0] + '-' + str(row[5]), "%Y-%m-%d-%H:%M:%S")
            else:
                analysis_timestamp= ""

            data.append({
                "transformer_identification": {
                    "transformer_id": row[0],
                    "transformer_name": row[1],
                    "location": row[2],
                    "installation_date": str(row[3])
                }, 
                "chromatography_data":{
                    "analysis_timestamp": analysis_timestamp.isoformat(),
                    "H2": row[6],
                    "CO": row[7],
                    "CO2": row[8],
                    "C2H4": row[9],
                    "C2H6": row[10],
                    "CH4": row[11],
                    "C2H2": row[12],
                    "oil_acidity": row[13],
                    "oil_temperature": row[14],
                    "oil_pressure": row[15]
                }, 
                "environment_parameters": {
                    "environment_temperature": row[16],
                    "environment_humidity": row[17],
                    "atmospheric_pressure": row[18]
                },
                "history_and_observations":{
                    "last_maintenance_date": str(row[19]),
                    "maintenance_done": row[20],
                    "observations": row[21]
                }
            })

        return data