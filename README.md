# Prefect Scheduler Python

This project showcases the usage of Prefect, a powerful workflow automation tool in Python.

## Features
- Simplify workflow orchestration and automation
- Define complex workflows with ease using Python code
- Seamlessly integrate with various data sources, APIs, and services
- Monitor and track the progress of your workflows
- Handle error handling, retries, and notifications

### Install the required dependencies
```python
pip install -r requirements.txt
```


### Start the prefect server
```python
prefect start server
```


### Create flows and deployment on prefect
```python
python create_deployment.py
```


### Start or Create the agent
```python
prefect agent start --pool default-agent-pool --work-queue default
```

**You can now schedule the deployments from the UI or from the python script.
To schedule them from python script use the below script.**
```python
from prefect.server.schemas.schedules import CronSchedule

Deployment.build_from_flow(
    flow=flow_name,
    name="Deployment Name",
    schedule=CronSchedule(
        cron="0 0 * * *",
    ),
)
```

## Screenshots
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_flows.jpg)
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_block.png)
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_flow.png)
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_schedule_flow.png)
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_deployments.png)
![Screenshot](https://github.com/azharajmeri/prefect-scheduler-python/blob/main/screenshots/prefect_deployment_output.png)
