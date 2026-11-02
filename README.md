Electric Vehicle Market Performance & Insights

1. Project Overview

The project, Electric Vehicle Market Performance & Insights, focuses on exploring electric vehicle (EV) market data using Tableau. It presents information about EV sales, manufacturers, vehicle categories, battery technology, driving range, customer ratings, and other performance indicators.

The project also integrates Tableau dashboards and stories into a web application using Python Flask.

2. Problem Statement

The electric vehicle market contains information about different manufacturers, vehicle categories, battery technologies, sales, and customer preferences. Understanding this information through raw datasets can be difficult.

This project aims to organize and visualize EV market data to make it easier to explore patterns, compare categories, and understand different vehicle performance indicators.

3. Project Objectives

- Analyze electric vehicle market data.
- Compare EV manufacturers and vehicle categories.
- Explore annual sales and market regions.
- Examine battery capacity, battery types, and degradation.
- Understand customer ratings and satisfaction.
- Create interactive Tableau dashboards and stories.
- Embed Tableau visualizations into a Flask web application.

4. Tools and Technologies

- Tableau Public: Data visualization, dashboards, and stories.
- Microsoft Excel: Dataset handling.
- Python 3.12.4: Web application development.
- Flask: Web framework.
- Visual Studio Code: Development environment.
- Kaggle: Dataset source.

5. Data Collection

The electric vehicle dataset was downloaded from Kaggle.

The downloaded archive contained training and testing datasets. The training dataset was extracted and saved as an Excel file named "EV Market Train.xlsx".

The dataset used in Tableau contained 200,000 rows and 37 fields.

6. Data Preparation

The dataset was inspected and connected to Tableau using the Microsoft Excel data connection.

The course-provided dataset was already cleaned, so no additional data-cleaning operations were performed.

The available fields were reviewed to identify suitable measures and dimensions for analysis.

7. Data Visualization

Twelve worksheets were created in Tableau:

1. Annual EV Sales by Model Year
2. EV Sales by Manufacturer
3. EV Sales by Vehicle Category
4. Average EV Driving Range by Category
5. Average Battery Capacity by Vehicle Category
6. EV Sales by Market Region
7. Customer Satisfaction by Manufacturer
8. EV Distribution by Battery Type
9. Average Battery Degradation by Battery Type
10. EV Distribution by Manufacturing Country
11. Customer Rating by EV Category
12. EV Market Performance at a Glance

Different charts and summary visualizations were used to present the dataset.

8. Dashboard Development

Four dashboards were created:

Dashboard 1: EV Sales & Market Trends

- Annual EV sales
- EV sales by manufacturer
- EV sales by vehicle category

Dashboard 2: Vehicle Category & Performance Analysis

- Average driving range
- Average battery capacity
- EV sales by market region

Dashboard 3: Battery Technology & Customer Insights

- Customer satisfaction by manufacturer
- EV distribution by battery type
- Average battery degradation by battery type

Dashboard 4: EV Market Overview & Customer Insights

- EV distribution by manufacturing country
- Customer rating by EV category
- EV market performance summary

Filters for Manufacturer, Category, and Model Year were added to Dashboard 1 and tested.

9. Story Creation

Four Tableau story points were created to organize the dashboards:

1. EV Sales & Market Trends
2. Vehicle Category & Performance Analysis
3. Battery Technology & Customer Insights
4. EV Market Overview & Customer Insights

The workbook was successfully published to Tableau Public, and all four story points were checked online.

10. Web Integration Using Flask

A web application was developed using Python Flask.

The development process included:

1. Creating an "EV_Market_Analysis" project folder.
2. Creating a Python virtual environment.
3. Installing Flask.
4. Creating the "app.py" file.
5. Adding the Tableau Public visualization URL.
6. Embedding the Tableau story using an HTML iframe.
7. Running the Flask application locally.
8. Adding navigation buttons for all four story points.
9. Testing the navigation and embedded visualizations.

The application was successfully opened locally at:

"http://127.0.0.1:5000"

All four story navigation buttons were tested.

11. Project Results

The completed Tableau workbook contains:

- 12 worksheets
- 4 dashboards
- 4 story points
- Interactive filters on Dashboard 1
- Tableau Public publication

The Flask web application provides access to all four Tableau story points through navigation buttons.

The dataset summary sheet displays 199,999 distinct vehicle IDs and a total of 1,550,703,961 in the Annual sales unit field. These are dataset-level figures and should not be interpreted as independently verified real-world market totals.

12. Conclusion

This project demonstrates how electric vehicle market data can be explored and presented through data visualization and dashboards.

Tableau was used to analyze different EV market indicators, while Python Flask was used to integrate the published Tableau story into a web application.

The project provided practical experience with dataset exploration, data visualization, dashboard development, storytelling, and basic web integration.

13. Business Scenarios & Analysis

This project explores electric vehicle market performance through three business scenarios.

Scenario 1: Emily Johnson – EV Market Strategy Director

Business need: Understand EV sales trends, leading manufacturers, vehicle categories, customer satisfaction, battery technology adoption, and driving range.

Project analysis:

- Annual EV sales by model year
- EV sales by manufacturer and vehicle category
- Customer satisfaction by manufacturer
- EV distribution by battery type
- Average driving range by vehicle category

Business value: Helps identify sales patterns, manufacturer performance, and customer preferences.

Scenario 2: David Chen – Automotive Business Intelligence Manager

Business need: Understand manufacturer performance, battery distribution, manufacturing countries, and customer ratings.

Project analysis:

- EV sales by manufacturer
- EV distribution by battery type
- EV distribution by manufacturing country
- Customer ratings by EV category
- Annual EV sales trends

Business value: Supports comparisons of manufacturer performance, battery adoption, and geographic manufacturing distribution.

Scenario 3: Dr. Sarah Williams – Sustainable Mobility Research Analyst

Business need: Explore battery technologies, vehicle driving range, manufacturing distribution, and customer insights.

Project analysis:

- Average battery capacity by vehicle category
- Average battery degradation by battery type
- Average EV driving range by category
- EV distribution by manufacturing country
- Customer ratings by EV category

Business value: Provides information for comparing battery technologies, vehicle performance, and customer insights.

Note: The analysis is based on the available dataset and visualizations. It does not independently measure carbon emissions or prove environmental impact.