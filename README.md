# ZestMoney
Login to Facebook, post message "Hello World"

Developed a project for logging into Facebook, create a post and log out. 
Language: Python
Tool: Pycharm, Selenium Webdriver
Unit testing: pytest
POM structure

Description: Created a customLogger under utilities for generating logs, conftest for pytest configuration and invoking driver. Created POM model where pages had the methods related to Facebook
and test had the tests related to Facebook scenario. Decorated the tests with pytest fixtures (ordering).

Scenarios:
1. Intialiaze the browser
2. Launch Facebook page
3. Enter credentials and login to the application
4. Find the create post, enter "Hello World" in post box
5. Verify if the post has been created
6. Log out of the application
7. Quit the driver

Package Details:
Please refer to the requirements.txt file
