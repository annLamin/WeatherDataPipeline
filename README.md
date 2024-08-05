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
![Architecture Diagram](https://github.com/annLamin/WeatherDataPipeline/blob/main/workflow_diagram.jpg)

### Technology Used
- Python3
- Apache-Airflow
- Amazon EC2
- Amazon S3
###   Implementation
#### Data Extraction from OpenWeather API
OpenWeather Ltd provides global weather data via API, including current weather data, forecasts,
nowcasts, and historical weather data. Python and the requests library were utilized to interact with
the OpenWeather API. The API key was securely managed using environment variables to ensure
security and prevent unauthorized access. Data extraction was scheduled to run daily to fetch the
latest weather information
#### Data Transformation and CSV Export
Once the data was retrieved from the API, it was transformed into a structured CSV format using
Python’s pandas library. This transformation included selecting relevant fields, cleaning data, and 
formatting it appropriately for storage. The relevant features that are needed for this project for
now are the:
 - TimeZone: This is the location from which we want to extract the data which is Rome.
- Date: The day we are extracting the data.
- Temperature: The temperature of that particular day.
The extraction can be done minutely, hourly or daily but for simplicity, I chose daily.

#### Integration with Apache Airflow
Apache Airflow was employed to orchestrate the entire data pipeline. We configured a DAG (Directed Acyclic Graph) that defined the workflow
- Task 1: Data extraction from the OpenWeather API.
- Task 2: Transformation of raw data into a CSV format.
- Task 3: Uploading the CSV file to an Amazon S3 bucket.
Airflow’s scheduling feature ensured that the pipeline ran automatically at a one day intervals,
adhering to the project’s requirements for regular updates of weather data.
