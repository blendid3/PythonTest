import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Arduino')
config.set('Arduino', 'Port', 'COM4')
config.set('Arduino', 'Bitrate', '9800')
config.add_section('Socket')
config.set('Socket', 'Port', '9107')
# config.set('Arduino', 'Bitrate', '9800')

# config.set()


# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)

# https://docs.python.org/3/library/configparser.html