# Building Data Pipeline Using Apache Airflow

### Introduction
Weather data APIs typically provide data for current conditions, forecast data, and historical data.They are used by businesses that need to integrate weather information into their business processes for improved operations, risk assessment, and safety. In today’s era of big data, it is important to laverage such API’s. The ability of analyze a large volume of weather data can yield critical insights, making operational efficiencies and strategic decision making.
In this project, I designed a data pipeline to extract weather data from the OpenWeather API using
Python, transform it into a structured format, and store it in an Amazon S3 bucket. The pipeline
is orchestrated using Apache Airflow running on an EC2 instance. This report outlines the design,
implementation, and outcomes of the project. The automation of the extraction, transformation
and storage of the data will help businesses to be able to integrate up-to-date weather information
into their systems. This integration is very vital in the era of big data, where acurate and current information can significantly impact operations and decision making.

### Project Overview
This project aimed to automate the extraction of weather data from the OpenWeather API, convert it into a CSV format using Python, and upload the CSV file to Amazon S3, reducing manual intervention and ensuring consistent data collection. Python's requests and pandas libraries were used for API calls and data manipulation, while Apache Airflow managed the workflow, ensuring each step was executed in the correct order and on a regular schedule. The automation streamlined the process, making weather data continuously available for further analysis or integration with other systems.

### Technology Used
