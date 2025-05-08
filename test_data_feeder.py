import requests
import json

data = [
    {"tool": "upgrader", "task": "healthchecks", "status": "completed", "duration": 120},
    {"tool": "scanner", "task": "vuln-scan", "status": "succeeded", "duration": 75},
    {"tool": "packer", "task": "build-image", "status": "failed", "duration": 45}
]

for item in data:
    response = requests.post("http://localhost:8000/api/tasks", json=item)
    print(response.json())
