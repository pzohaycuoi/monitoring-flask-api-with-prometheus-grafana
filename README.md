# Monitoring Flask API with Prometheus and Grafana

This project sets up a monitoring stack for a Flask API using Prometheus, Grafana, and Alertmanager. The stack includes the following components:

- Flask API
- Prometheus
- Grafana
- Alertmanager
- Node Exporter
- Blackbox Exporter

## Project Structure



## Components

### Flask API

The Flask API is a simple application that exposes a few endpoints and metrics.

- **File:** [app/app.py](app/app.py)
- **Dependencies:** [app/requirements.txt](app/requirements.txt)
- **Dockerfile:** [app/dockerfile](app/dockerfile)

### Prometheus

Prometheus is used to scrape metrics from the Flask API and other exporters.

- **Configuration:** [prometheus/prometheus.yml](prometheus/prometheus.yml)
- **Alert Rules:** [prometheus/alertrules.yml](prometheus/alertrules.yml)

### Grafana

Grafana is used to visualize the metrics collected by Prometheus.

- **Datasource Configuration:** [grafana/provisioning/datasources/datasource.yml](grafana/provisioning/datasources/datasource.yml)
- **Dashboards:**
  - [API Success Error Rate](grafana/dashboards/apisuccesserror.json)
  - [Average Response Time](grafana/dashboards/averageresponsetime.json)
  - [Node Resources](grafana/dashboards/noderesources.json)

### Alertmanager

Alertmanager handles alerts sent by Prometheus.

- **Configuration:** [alertmanager/alertmanager.yml](alertmanager/alertmanager.yml)

### Node Exporter

Node Exporter is used to collect hardware and OS metrics.

### Blackbox Exporter

Blackbox Exporter is used to probe endpoints over HTTP.

- **Configuration:** [blackbox/blackbox.yml](blackbox/blackbox.yml)

## Setup

1. **Setup Slack notifications**
- Follow this guide to setup slack web hook: [Slack Guide](https://api.slack.com/messaging/webhooks)
- Fill in field `slack_api_url` in `alertmanager/alertmanager.yml` with the newly created webhook url

2. **Build and run the Docker containers:**

   ```sh
   docker-compose up
3. Access the services:
- Flask API: http://localhost:5050
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (default login: admin / admin)
- Alertmanager: http://localhost:9093

## Usage
- **Flask API Endpoints:**
    - `GET /`: Returns a "Hello, World!" message.
    - `POST /`: Toggles the error return for the GET / endpoint.
- **Prometheus Metrics:**
    - Flask API metrics are available at http://localhost:5050/metrics.
- **Grafana Dashboards:**
    - Import the JSON files from the dashboards directory to visualize metrics.
- **Alerts:**
    - Prometheus is configured with alert rules to monitor CPU, memory, and disk usage, as well as API errors.
    - Alerts are sent to Alertmanager, which is configured to send notifications to Slack.