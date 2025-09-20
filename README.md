```mermaid
flowchart LR
    Developer --> Input[Git Push]
    Input --> CI/CD[Github Actions]
    CI/CD --> Configuration[Ansible]
    Configuration --> VM[GCP VM]
    VM -->API[Python Fast API]
    VM --> Prometheus
    VM --> Grafana
    Grafana --> Developer