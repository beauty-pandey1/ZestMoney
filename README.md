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
atomicwrites==1.4.0
attrs==19.3.0
certifi==2020.6.20
chardet==3.0.4
colorama==0.4.3
fake-useragent==0.1.11
idna==2.10
importlib-metadata==1.7.0
iniconfig==1.0.1
more-itertools==8.4.0
packaging==20.4
pluggy==0.13.1
py==1.9.0
pyparsing==2.4.7
pytest==6.0.1
pytest-ordering==0.6
requests==2.24.0
requests-file==1.5.1
selenium==3.141.0
selenium-firefox==0.5.18
six==1.15.0
tldextract==2.2.3
toml==0.10.1
urllib3==1.25.10
zipp==3.1.0
