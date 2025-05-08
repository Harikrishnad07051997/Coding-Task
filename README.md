A Python application to collect task metrics from external tools and expose them for Prometheus scraping.

Features:
- Accepts task status and duration via `/api/tasks`
- Exposes Prometheus metric `task_duration` on `/metrics`
- Configurable via environment variables or `.env`
- Dockerized for easy deployment

How to run Locally:
1. Clone the Repository
bash:
git clone 
cd task
3. Run using Docker:

docker build -t task-metrics-exporter .


docker run -p 8000:8000 --env-file .env task-metrics-exporter

View metrics: http://localhost:8000/metrics

Run Prometheus in Docker:

docker run -d -p 9090:9090 --name prometheus `
  -v "D:\Task\prometheus.yml:/etc/prometheus/prometheus.yml" `
  prom/prometheus

Open Prometheus UI:
http://localhost:9090

Click on "Status" > "Targets" to verify Prometheus is successfully scraping task-metrics-exporter.

You should see the job named task-metrics-exporter with the state UP.
