from configparser import ConfigParser


# The value of the key or category it would send the function
def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)