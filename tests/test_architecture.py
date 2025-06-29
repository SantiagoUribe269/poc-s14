import pytest
from src.input import input_service
from src.data_processing import processor
from src.storage import replica

def test_data_flow():
    data = input_service.get_random_data()
    assert data

    processed = processor.dead_letter_queue(data)
    assert processed

    streamed = processor.stream_processor(data)
    assert streamed["validated"]

    saved = processor.process_and_save(data)
    assert saved

def test_replicas_and_failover():
    data = {"id": 1, "value": "test"}
    for i in range(1, 4):
        result = replica.save_replica(data, i)
        assert f"replica_{i}_saved" == result

    failover_result = replica.failover()
    assert failover_result == "failover_activated"

def test_data_consistency():
    data = input_service.get_random_data()
    assert isinstance(data, dict)
    assert "id" in data
    assert "value" in data