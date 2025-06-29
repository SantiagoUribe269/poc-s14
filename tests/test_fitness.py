import time
from src.input import input_service
from src.data_processing import processor

def test_latency():
    start = time.perf_counter()
    data = input_service.get_random_data()
    processor.stream_processor(data)
    end = time.perf_counter()
    latency = end - start
    print(f"Latency: {latency:.4f} seconds")
    assert latency < 1


def test_throughput():
    count = 10
    start = time.perf_counter()
    for _ in range(count):
        data = input_service.get_random_data()
        processor.stream_processor(data)
    end = time.perf_counter()
    throughput = count / (end - start)
    print(f"Throughput: {throughput:.2f} ops/sec")
    assert throughput > 1


def test_error_rate():
    total = 10
    errors = 0
    for _ in range(total):
        try:
            data = input_service.get_random_data()
            processor.stream_processor(data)
        except Exception:
            errors += 1
    error_rate = errors / total
    print(f"Error rate: {error_rate*100:.2f}%")
    assert error_rate < 0.1
