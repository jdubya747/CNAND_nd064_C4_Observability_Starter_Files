**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run kubectl command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

I was unsuccessful through extensive efforts trying to get Jaeger to work at all in its own 'observability' namespace. Consequently, I installed it in the'default' namespace along with the traced applications. This follows the pattern of other students as recommended by mentors on the forum.

Prometheus has been installed in the 'monitoring namspace.

Kubectl diagram demonstrating this:

![Kubectl](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/kubectl_pods_services.png)

## Setup the Jaeger and Prometheus source

*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

Screenshot of Grafana homepage and a second of the data sources. Although not shown, both data sources connect without errors.

![Grafana](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana_data_sources.png?raw=true)

![Starter Board](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana_home.png?raw=true)

## Create a Basic Dashboard

*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

Not on Promethus, but also usinng flask metrics!

![Prometheus Dashboard](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/dashboard_prometheus.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

The SLOs are *monthly uptime* and *request response time*. But they should be more clearly defined. 

The SLO of *monthly uptime* will be that this service should be reliable and available when the user wants to user it. This means that the system is accepting and processing http requests on its endpoints and that the system is returning successful results via status 200.

The SLIs for *monthly uptime* are:
- The system is available and processing http requests on all endpoints 99% of the time over the span of a month.
- The system is returning http 200 results for requests at least 98% of the time over the span of a month.

The SLO of *request response time* will be that this service should be responsive by delivering http results in a timely manner to the user's http requests. This means that The system reliably returns responses within the accepted timeframe and that the system is timely even under increasing load.

The SLIs for *request response time* are:
- The system returns on average a response time of under 300ms inclusive of all endpoints in the course of a month.
- The system maintains this under load. The system can scale to a 1000 requests per minute on average on the month and maintain the above 300ms average response time during that montly span.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
The metrics are mainly around the "Four Golden Signals"
 - Latency
 - Traffic
 - Errors
 - Saturation

 The metrics will measure:
 - Average Response Time (latency)
 - Request time in a percentile (latency)
 - Request rate (trafffic)
 - Number of requests (traffic)
 - Error Rate (errors)
 - Number of erros (errors)
 - Uptime (foundational)
 - CPU utilzation rate and load (saturation)
 - Memory utilization rate and usage (saturation)

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![Uptime Dashboard](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/uptime_dash.png)

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![Jaeger Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger_span.png)

![Jaeger Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/span_python.png)

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![Jaeger Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger_dashboard.png)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.


Error Number One:

![Error Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/error_screen1.png)

TROUBLE TICKET

Name: 500 error on backup-service: add-star

Date: January 17, 2020

Subject: 500 error from software exception 'object is not subscriptable'

Affected Area: app/app.py, line 107, backend_star, name = request.get_json['name']

Severity: Severe

Description: Problem with subscripting on the json object. Could be data or code.


Error Number Two:

![Error Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/error_screen2.png)

TROUBLE TICKET

Name: 500 Error on trial-service: get-python-jobs

Date: January 17, 2022

Subject: 500 error from software exception 'expecting value'

Affected Area: /app/app.py, line 96, in trial_trace

Severity: Severe

Description: Problem with getting length of json object.

## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

I further define the SLO to bring more clarity to "uptime" by stating the goal is 'availbility'. In the SLO that will mean:
- That the system is 'available' because the services are physically up and running.
- That the system is 'available' as its CPU and memory is not overload.
- That the system is 'available' as it is responsive via response times to user requests.
- That the system is available because its processing requests without error.

To support This SLO, there will be the following SLIs:
- The system is physically 'up' 99% of the time over the course of a month
- The system averages below 70% utilization rate for memory and cpu during the monthly period.
- The system returns on average a response time of under 300ms inclusive of all endpoints in the course of a month.
- The system is returning http 200 status results at least 98% of the time over the span of a month.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. CPU utilization rate, CPU load, memory utilization rate, memory usage
2. Uptime for the three application services
3. Request rates per second
4. Request totals per minute
5. Average response times
6. Percentile analysis of response times
7. Error rates per second
8. Number of errors per second

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what 
graphs are represented in the dashboard. 

Pictured below is final dashboard. Its panels directly correspond to the numbered list of KPI above.

1. The top row of panels indicate CPU and memory.
2. The second row corresponds to 'Uptime for three application services'
3. Panel 'Request Rate (per second)' represents (3)
4. Panel 'Number of Requests[1m]' repressents (4)
5. Panel 'Average Response time[30]' represents (5)
6. Panel 'Request Duration[30][p100]' represents (6)
7. Panel 'Error Rate(per second) represents (7)
8. Panel 'Number of Errors(per Minute) represents (8)

![Final Dashboard](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/final_dashboard.png)
