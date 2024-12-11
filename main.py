from fastapi import FastAPI, HTTPException
from ingestion.json_handler import JSONHandler
from ingestion.excel_reader import ExcelReader
from ingestion.message_sender import RabbitMQSender
from ingestion.mongodb_client import MongoDBClient
from ingestion.test_data import TestData
import yaml
import os

app = FastAPI()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
QUEUE_NAME = "data-ingestion"

with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

mongo_config = config["mongo"]
MONGO_URI = os.getenv("MONGO_URI", mongo_config["uri"])
mongo_client = MongoDBClient(
    uri=MONGO_URI,
    database_name=mongo_config["database_name"],
    collection_name=mongo_config["collection_name"]
)

@app.post("/ingest-json/")
def ingest_json(data: dict):
    try:
        processed_data = JSONHandler.process_json(data)

        document_id = mongo_client.save_data(processed_data)

        processed_data["document_id"] = document_id

        del processed_data["_id"]

        sender = RabbitMQSender(RABBITMQ_HOST, QUEUE_NAME)
        sender.send_message(processed_data)
        sender.close_connection()

        return {"status": "success",
                "message": "Data successfully sent!",
                "document_id": document_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error: " + str(e))
    
@app.post("/ingest-excel/")
def ingest_excel(file_data: dict):
    try:
        file_path = "input_sheets/" + file_data["file_name"]
        if os.path.exists(file_path):
            excel_data = ExcelReader.read_excel(file_path)
        else:
            raise ValueError("File not found in path!")
        document_ids = []

        for data in excel_data:
            processed_data = JSONHandler.process_json(data)

            document_id = mongo_client.save_data(processed_data)

            processed_data["document_id"] = document_id

            del processed_data["_id"]
            sender = RabbitMQSender(RABBITMQ_HOST, QUEUE_NAME)
            print(processed_data)
            sender.send_message(processed_data)
            document_ids.append(document_id)
            sender.close_connection()

        return {"status": "success",
                "message": "Data successfully sent!",
                "document_ids": document_ids}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error: " + str(e))
    
@app.post("/ingest-dummy/")
def ingest_dummy_data():
    try:
        processed_data = JSONHandler.process_json(TestData.get_test_data())
        print(processed_data)

        document_id = mongo_client.save_data(processed_data)

        processed_data["document_id"] = document_id
        del processed_data["_id"]

        print("RabbitMQ Host: {}".format(RABBITMQ_HOST))

        sender = RabbitMQSender(RABBITMQ_HOST, QUEUE_NAME)
        sender.send_message(processed_data)
        sender.close_connection()

        return {"status": "success",
                "message": "Data successfully sent!",
                "document_id": document_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error: " + str(e))