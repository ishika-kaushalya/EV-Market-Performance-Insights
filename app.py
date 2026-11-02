from flask import Flask, render_template_string, request

app = Flask(__name__)

TABLEAU_BASE = (
    "https://public.tableau.com/views/"
    "ElectricVehicleMarketPerformanceInsights_17934975913880/"
)

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>EV Market Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f4f7f6;
        }
        header {
            background: #176b55;
            color: white;
            padding: 22px;
            text-align: center;
        }
        nav {
            text-align: center;
            padding: 18px;
        }
        nav a {
            display: inline-block;
            padding: 12px 20px;
            margin: 5px;
            background: #176b55;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        iframe {
            width: 100%;
            height: 1100px;
            border: none;
        }
    </style>
</head>
<body>
<header>
    <h1>Electric Vehicle Market Performance &amp; Insights</h1>
    <p>Interactive Tableau Story</p>
</header>

<nav>
    <a href="/?story=Story1">Story 1</a>
    <a href="/?story=Story2">Story 2</a>
    <a href="/?story=Story3">Story 3</a>
    <a href="/?story=Story4">Story 4</a>
    <a href="/documentation">Documentation</a>
</nav>

<iframe src="{{ tableau_url }}"></iframe>
</body>
</html>
"""

DOC_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Project Documentation - EV Market Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background: #f4f7f6;
            color: #222;
        }
        .container {
            max-width: 1000px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }
        h1, h2 {
            color: #176b55;
        }
        h1 {
            text-align: center;
        }
        a {
            color: #176b55;
        }
    </style>
</head>
<body>
<div class="container">

<h1>Electric Vehicle Market Performance &amp; Insights</h1>

<h2>1. Project Overview</h2>
<p>The project focuses on exploring electric vehicle (EV) market data using Tableau. It presents information about EV sales, manufacturers, vehicle categories, battery technology, driving range, customer ratings and other performance indicators.</p>
<p>The project also integrates Tableau dashboards and stories into a web application using Python Flask.</p>

<h2>2. Problem Statement</h2>
<p>The electric vehicle market contains information about different manufacturers, vehicle categories, battery technologies, sales and customer preferences. Understanding this information through raw datasets can be difficult.</p>
<p>This project aims to organize and visualize EV market data to make it easier to explore patterns, compare categories and understand vehicle performance indicators.</p>

<h2>3. Project Objectives</h2>
<ul>
<li>Analyze electric vehicle market data.</li>
<li>Compare EV manufacturers and vehicle categories.</li>
<li>Explore annual sales and market regions.</li>
<li>Examine battery capacity, battery types and degradation.</li>
<li>Understand customer ratings and satisfaction.</li>
<li>Create interactive Tableau dashboards and stories.</li>
<li>Embed Tableau visualizations into a Flask web application.</li>
</ul>

<h2>4. Tools and Technologies</h2>
<ul>
<li>Tableau Public: Data visualization, dashboards and stories.</li>
<li>Microsoft Excel: Dataset handling.</li>
<li>Python 3.12.4: Web application development.</li>
<li>Flask: Web framework.</li>
<li>Visual Studio Code: Development environment.</li>
<li>Kaggle: Dataset source.</li>
</ul>

<h2>5. Data Collection</h2>
<p>The electric vehicle dataset was downloaded from Kaggle.</p>
<p>The downloaded archive contained training and testing datasets. The training dataset was extracted and saved as an Excel file named EV Market Train.xlsx.</p>
<p>The dataset used in Tableau contained 200,000 rows and 37 fields.</p>

<h2>6. Data Preparation</h2>
<p>The dataset was inspected and connected to Tableau using the Microsoft Excel data connection.</p>
<p>The course-provided dataset was already cleaned, so no additional data-cleaning operations were performed.</p>
<p>The available fields were reviewed to identify suitable measures and dimensions for analysis.</p>

<h2>7. Data Visualization</h2>
<p>Twelve worksheets were created in Tableau:</p>
<ol>
<li>Annual EV Sales by Model Year</li>
<li>EV Sales by Manufacturer</li>
<li>EV Sales by Vehicle Category</li>
<li>Average EV Driving Range by Category</li>
<li>Average Battery Capacity by Vehicle Category</li>
<li>EV Sales by Market Region</li>
<li>Customer Satisfaction by Manufacturer</li>
<li>EV Distribution by Battery Type</li>
<li>Average Battery Degradation by Battery Type</li>
<li>EV Distribution by Manufacturing Country</li>
<li>Customer Rating by EV Category</li>
<li>EV Market Performance at a Glance</li>
</ol>
<p>Different charts and summary visualizations were used to present the dataset.</p>

<h2>8. Dashboard Development</h2>
<p>Four dashboards were created:</p>

<p><b>Dashboard 1: EV Sales &amp; Market Trends</b></p>
<ul>
<li>Annual EV sales</li>
<li>EV sales by manufacturer</li>
<li>EV sales by vehicle category</li>
</ul>

<p><b>Dashboard 2: Vehicle Category &amp; Performance Analysis</b></p>
<ul>
<li>Average driving range</li>
<li>Average battery capacity</li>
<li>EV sales by market region</li>
</ul>

<p><b>Dashboard 3: Battery Technology &amp; Customer Insights</b></p>
<ul>
<li>Customer satisfaction by manufacturer</li>
<li>EV distribution by battery type</li>
<li>Average battery degradation by battery type</li>
</ul>

<p><b>Dashboard 4: EV Market Overview &amp; Customer Insights</b></p>
<ul>
<li>EV distribution by manufacturing country</li>
<li>Customer rating by EV category</li>
<li>EV market performance summary</li>
</ul>

<p>Filters for Manufacturer, Category and Model Year were added to Dashboard 1 and tested.</p>

<h2>9. Story Creation</h2>
<p>Four Tableau story points were created:</p>
<ol>
<li>EV Sales &amp; Market Trends</li>
<li>Vehicle Category &amp; Performance Analysis</li>
<li>Battery Technology &amp; Customer Insights</li>
<li>EV Market Overview &amp; Customer Insights</li>
</ol>
<p>The workbook was published to Tableau Public, and all four story points were checked online.</p>

<h2>10. Web Integration Using Flask</h2>
<p>A web application was developed using Python Flask.</p>
<ol>
<li>Creating an EV_Market_Analysis project folder.</li>
<li>Creating a Python virtual environment.</li>
<li>Installing Flask.</li>
<li>Creating the app.py file.</li>
<li>Adding the Tableau Public visualization URL.</li>
<li>Embedding the Tableau story using an HTML iframe.</li>
<li>Running the Flask application locally.</li>
<li>Adding navigation buttons for all four story points.</li>
<li>Testing the navigation and embedded visualizations.</li>
</ol>
<p>The application was opened locally at http://127.0.0.1:5000.</p>
<p>All four story navigation buttons were tested.</p>

<h2>11. Project Results</h2>
<p>The completed Tableau workbook contains:</p>
<ul>
<li>12 worksheets</li>
<li>4 dashboards</li>
<li>4 story points</li>
<li>Interactive filters on Dashboard 1</li>
<li>Tableau Public publication</li>
</ul>
<p>The Flask web application provides access to all four Tableau story points through navigation buttons.</p>
<p>The dataset summary sheet displays 199,999 distinct vehicle IDs and a total of 1,550,703,961 in the Annual sales unit field. These are dataset-level figures and should not be interpreted as independently verified real-world market totals.</p>

<h2>12. Conclusion</h2>
<p>This project demonstrates how electric vehicle market data can be explored and presented through data visualization and dashboards.</p>
<p>Tableau was used to analyze different EV market indicators, while Python Flask was used to integrate the published Tableau story into a web application.</p>
<p>The project provided practical experience with dataset exploration, data visualization, dashboard development, storytelling and basic web integration.</p>

<h2>13. Business Scenarios &amp; Analysis</h2>

<h3>Scenario 1: Emily Johnson – EV Market Strategy Director</h3>
<p>Emily Johnson wants to understand EV market performance, leading manufacturers, customer satisfaction, battery technology adoption and driving range across vehicle categories.</p>

<p><strong>Analysis included in this project:</strong></p>
<ul>
<li>Annual EV sales by model year</li>
<li>EV sales by manufacturer</li>
<li>EV sales by vehicle category</li>
<li>Customer satisfaction by manufacturer</li>
<li>EV distribution by battery type</li>
<li>Average driving range by vehicle category</li>
</ul>
<p><strong>Business value:</strong> Helps identify sales patterns, manufacturer performance and customer preferences.</p>

<hr>

<h3>Scenario 2: David Chen – Automotive Business Intelligence Manager</h3>
<p>David Chen wants to compare manufacturer performance, annual sales trends, battery technology distribution, manufacturing countries and customer ratings.</p>

<p><strong>Analysis included in this project:</strong></p>
<ul>
<li>EV sales by manufacturer</li>
<li>Annual EV sales trends</li>
<li>EV distribution by battery type</li>
<li>EV distribution by manufacturing country</li>
<li>Customer ratings by EV category</li>
</ul>
<p><strong>Business value:</strong> Helps compare manufacturer performance, battery adoption and geographic manufacturing distribution.</p>

<hr>

<h3>Scenario 3: Dr. Sarah Williams – Sustainable Mobility Research Analyst</h3>
<p>Dr. Sarah Williams wants to study battery technology, vehicle performance, manufacturing distribution and customer adoption.</p>

<p><strong>Analysis included in this project:</strong></p>
<ul>
<li>Average battery capacity by vehicle category</li>
<li>Average battery degradation by battery type</li>
<li>Average driving range by vehicle category</li>
<li>EV distribution by manufacturing country</li>
<li>Customer ratings by EV category</li>
</ul>
<p><strong>Business value:</strong> Helps compare battery technologies, vehicle performance and customer insights.</p>

<hr>

<p><strong>Note:</strong> These analyses are based on the available dataset and visualizations. The project does not directly measure carbon emissions or environmental impact.</p>

<p><a href="/">Back to Project</a></p>

</div>
</body>
</html>
"""


@app.route("/")
def home():
    story = request.args.get("story", "Story1")

    if story not in ["Story1", "Story2", "Story3", "Story4"]:
        story = "Story1"

    tableau_url = TABLEAU_BASE + story + "?:showVizHome=no"

    return render_template_string(
        HOME_HTML,
        tableau_url=tableau_url
    )


@app.route("/documentation")
def documentation():
    return render_template_string(DOC_HTML)


if __name__ == "__main__":
    app.run(debug=True)