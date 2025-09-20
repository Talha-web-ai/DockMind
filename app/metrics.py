from prometheus_client import Counter, Histogram, start_http_server
import time

# ------------------------
# Metrics definitions
# ------------------------
REQUEST_COUNT = Counter(
    "app_request_count",
    "Total number of requests",
    ["endpoint", "method"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

# ------------------------
# Start Prometheus metrics server
# ------------------------
def start_metrics_server(port: int = 8001):
    start_http_server(port)
    print(f"✅ Prometheus metrics server started on port {port}")

# ------------------------
# Decorator to track metrics
# ------------------------
def track_metrics(endpoint: str, method: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            response = func(*args, **kwargs)
            latency = time.time() - start_time

            REQUEST_COUNT.labels(endpoint=endpoint, method=method).inc()
            REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)

            return response
        return wrapper
    return decorator
