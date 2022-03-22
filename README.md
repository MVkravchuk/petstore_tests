# petstore_tests
Hi!  
I'm Max Kravchuck, and it's my demo project.  
It's based on Petstore API from Swagger: https://petstore.swagger.io/#/

# How to run

**Before you start install Python 3.10 or newer.**

```commandline
# Install dependensies
pip install -r requiremennts.txt

# Run tests without Allure report
pytest

# Run tests with Allure report
pytest --alluredir=./.my_allure_results

# To see Allrure report 
allure serve .my_allure_results    
```