**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run kubectl command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

I was unsuccessful in extensive efforts at trying to ket Jaeger to work at all in its own 'obersability' namespace. Consequently I install it in 'default' along with the traced applications. This follows the pattern of other students as recommended by metors on the forum.

Prometheus has been installed in the 'monitoring namspace.

Kubectl out demonstrating this:

![Kubectl](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/kubectl_pods_services.png)

## Setup the Jaeger and Prometheus source

*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

Screenshot of Grafano homepage and a second of data sources. Although not shown, both data sources connect without errors.

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
- The system is available and proceesing http requests on all endpoints 99% of the time over the span of a month.
- The system is returning http 200 status results at least 98% of the time over the span of a month.

The SLO of *request response time* will be that this service should be responsive by delivering http results in a timely manner to the user's http requests. This means that The system reliably returns responses within the accepted timeframe and that The system is timely even under increasing load.

The SLIs for *request response time* are:
- The system returns on average a response time of under 300ms inclusive of all endpoints in the course of a month.
- The system system maintains this under load. The system can scale to a 1000 requests per minute on average on the month and maintain the above 300ms average response time during that montly span.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
 My metrics are mainly around the "Four Golden Signals"
 - Latency
 - Traffic
 - Errors
 - Saturation

 Specifically my metrics will measure:
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

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


Error Number One:

![Error Span](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/error_screen2.png)

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:

## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
![Final Dashboard](https://github.com/jdubya747/CNAND_nd064_C4_Observability_Starter_Files/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/final_dashboard.png)
