from prometheus_client import Gauge

TASK_DURATION = Gauge(
    "task_duration",
    "Duration of tasks reported by external tools",
    ["tool", "task"]
)
