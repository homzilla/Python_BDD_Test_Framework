This repository contains an automated testing framework for the web application located at https://demo.applitools.com/hackathon.html.

The framework uses Python as the programming language, Selenium for UI testing, and Behave for BDD-style test scenarios.

Prerequisites
Before running the tests, make sure you have the following installed on your system:

Python 3

Google Chrome browser

Installation

To install the necessary Python packages, run the following command in the project directory:


`pip install -r requirements.txt`
Running the tests
To run the tests, execute the following command in the project directory:


`python test_runner.py`
This will run all the test scenarios and generate an HTML report in the project directory. You can open the report in your web browser to view the results.

Configuration
The `behave.ini` file in the project directory contains the configuration for the test runner. You can modify the configuration options in this file to customize the behavior of the test runner.

Troubleshooting
If you encounter any issues while running the tests, please check the following:

Make sure the `Chrome browser` is installed and up-to-date.
Make sure you have the correct version of the Chrome driver installed. The version of the Chrome driver must match the version of the Chrome browser you are using.
Make sure the URL of the web application is correct in the base_page.py file.
License
This project is licensed under the MIT License. See the LICENSE file for details.

**Prerequisites**

Before running the tests, make sure you have the following installed on your system:

Python 3
Google Chrome browser
Installation
To install the necessary Python packages, run the following command in the project directory:

`pip install -r requirements.txt`

Running the tests

To run the tests, execute the following command in the project directory:

`python test_runner.py`

This will run all the test scenarios and generate an HTML report in the project directory. You can open the report in your web browser to view the results.

**Configuration**

The behave.ini file in the project directory contains the configuration for the test runner. You can modify the configuration options in this file to customize the behavior of the test runner.

**Troubleshooting**

If you encounter any issues while running the tests, please check the following:

Make sure the Chrome browser is installed and up-to-date.
Make sure you have the correct version of the Chrome driver installed. The version of the Chrome driver must match the version of the Chrome browser you are using.
Make sure the URL of the web application is correct in the base_page.py file.
**License**

This project is licensed under the MIT License. See the LICENSE file for details.

