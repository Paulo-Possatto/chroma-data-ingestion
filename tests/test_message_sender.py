import pytest
from unittest.mock import patch, MagicMock
from ingestion.message_sender import RabbitMQSender
import datetime
import json
import pika

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "data-ingestion"

INPUT_DATA = {
    "transformer_identification": {
        "transformer_id": "T1234",
        "transformer_name": "LV Transformer 12",
        "location": "Substation 31",
        "installation_date": str(datetime.date(2021, 12, 25))
    },
    "chromatography_data": {
        "analysis_timestamp": str(datetime.datetime(2024, 11, 25, 14, 46, 0)),
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
    "history_and_observations": {
        "last_maintence_date": str(datetime.date(2023, 8, 12)),
        "maintenance_done": "Oil change",
        "observations": "No faults detected"
    }
}

@patch("ingestion.message_sender.pika.BlockingConnection")
def test_send_message_success(mock_blocking_connection):
    # Mockando conexão e canal
    mock_channel = MagicMock()
    mock_connection = MagicMock()
    mock_blocking_connection.return_value = mock_connection
    mock_connection.channel.return_value = mock_channel

    # Instanciar o RabbitMQSender
    sender = RabbitMQSender(RABBITMQ_HOST, QUEUE_NAME)
    message = INPUT_DATA

    # Enviar mensagem
    sender.send_message(message)

    # Verificar se a mensagem foi publicada corretamente
    mock_channel.basic_publish.assert_called_once_with(
        exchange='',
        routing_key=QUEUE_NAME,
        body=json.dumps(message),  # O corpo agora é serializado como JSON
        properties=pika.BasicProperties(delivery_mode=2)  # Propriedades duráveis
    )

    # Fechar conexão
    sender.close_connection()
    mock_connection.close.assert_called_once()

@patch("ingestion.message_sender.pika.BlockingConnection")
def test_send_message_connection_error(mock_blocking_connection):
    # Simular erro de conexão
    mock_blocking_connection.side_effect = Exception("Connection failed")

    with pytest.raises(Exception, match="Connection failed"):
        sender = RabbitMQSender(RABBITMQ_HOST, QUEUE_NAME)
        sender.send_message(INPUT_DATA)
