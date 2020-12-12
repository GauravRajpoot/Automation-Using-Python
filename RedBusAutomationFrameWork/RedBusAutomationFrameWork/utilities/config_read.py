import configparser
config = configparser.RawConfigParser()
configFilePath = r'configFile/config.properties'
config.read(configFilePath)


def get_TestURL():
    return config.get('Global_Parameters', 'Test_Site_Name')


def get_Waits():
    return config.get('Global_Parameters', 'Wait')


def get_Browser():
    return config.get('Global_Parameters', 'BrowserName')
