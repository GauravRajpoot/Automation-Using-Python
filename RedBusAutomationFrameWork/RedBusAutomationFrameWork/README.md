# Red Bus Automation Framework

This frame work is developed to test the functionality of ```REDBUS``` web page 
## 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install various libraries which are specified in ```requirements.txt```
example is shown bellow

```bash
pip install module_name
```

## Usage

```
1. Download the framework 
2. Install required packages
3. Use the comanad to execute the frame work using cmd 
```
``` 
py.test -v -s tests/ --browser chrome --html=Current_test_results/AutomationReport.html
```

## Compatibility
This framework is compatible with all browsers i.e Chrome,Ie and Firefox
however for better experience use ```Chrome Browser```
* For firefox and ie browser path setting would be required which depends of various parameters like version etc
* Selection of browser can be done through cmd by replacing the chrome browser with respective ones
## Result Analysis
* All the reusults are kept under ```Curent_test_results``` folder of the framework
* It contains following tools/file
     -  ScreenShot of failed method
     - Log file 
     - HTML report
 
## Project Under  
[Nagarro Software Training Program](https://www.nagarro.com/en)

