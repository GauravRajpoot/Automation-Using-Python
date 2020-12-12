from datetime import datetime
import os
'''
Screen Shot method for getting the screen shot
'''

def take_screenshot(driver, name):
    dirName = 'Current_test_results'
    if not os.path.exists(dirName):
        # Create folder with name "Current test result" if don't exists
        os.makedirs(dirName)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.save_screenshot('%s\\screenshot-%s%s-.png' % (dirName, name, now))