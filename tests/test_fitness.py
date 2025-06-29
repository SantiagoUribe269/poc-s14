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

# 2️⃣ test_throughput:
# Procesa 10 datos y mide cuántas operaciones por segundo logra.
# Considera exitoso si throughput > 1 op/sec (relajado para PoC).

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

# 3️⃣ test_error_rate:
# Intenta procesar 10 datos y cuenta cuántos fallan.
# Considera exitoso si error_rate < 10% (relajado para PoC).

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
