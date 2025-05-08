A Python application to collect task metrics from external tools and expose them for Prometheus scraping.

Features:
- Accepts task status and duration via `/api/tasks`
- Exposes Prometheus metric `task_duration` on `/metrics`
- Configurable via environment variables or `.env`
- Dockerized for easy deployment

How to run Locally:
1. Clone the Repository
bash
git clone <your-repo-url>
cd task-metrics-exporter

2. Run using Docker:

docker build -t task-metrics-exporter .
docker run -p 8000:8000 --env-file .env task-metrics-exporter

3. Feed Test Data
python test_data_feeder.py

Note:
Environment Variables:
| Variable   | Description      | Default |
| ---------- | ---------------- | ------- |
| APP\_HOST  | Host for the app | 0.0.0.0 |
| APP\_PORT  | Port for the app | 8000    |
| LOG\_LEVEL | Logging level    | INFO    |

