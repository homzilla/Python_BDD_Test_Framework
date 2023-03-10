# **Applitools Demo Web Application Testing**

This repository contains automated test scenarios for the Applitools demo web application using Python, Selenium, and Behave. 
The tests cover various features of the application such as login, expenses, chart display, and dynamic content.

### Requirements

To run the tests locally, you'll need the following:

`Python 3`

`Pip (the package installer for Python)`

`Selenium`

`Bevave`

`Chrome or Firefox web browser`

`ChromeDriver or GeckoDriver (the WebDriver for Chrome or Firefox)`

You can download `ChromeDriver` from the official website, and `GeckoDriver` from the Mozilla GitHub repository.
Make sure to add the WebDriver executable to your  system's PATH environment variable so that it can be found by Selenium.

You will also need to download the ChromeDriver executable and add it to your system's PATH. You can download the latest version of ChromeDriver from the following link: https://chromedriver.chromium.org/downloads

### Running the Tests

To run the tests, navigate to the project directory in your terminal and run the following command:

`behave`

This will run all the test scenarios in the project and generate an HTML report that shows the test results and the summary of the tests executed. You can view the report by opening the `reports/index.html` file in your web browser.

