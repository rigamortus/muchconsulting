```mermaid
flowchart LR
    Developer --> Input[Git Push]
    Input --> Configuration[Ansible]
    Configuration --> VM[GCP VM]
    VM -->API[Python Fast API]
    VM --> Prometheus
    VM --> Grafana
    Grafana --> Developer