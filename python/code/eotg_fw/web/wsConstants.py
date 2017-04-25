# (c) EOTG, LLC 2017
# Author: Nathan Muller

# Base URL
BASE_URL = 'http://espressotg.info/eotg/api'

# Brew Setting Types
GET_BS_TYPES = '/brewSettingTypes'

# Devices
REGISTER_DEVICE = '/devices/registerDevice'
GET_BREW_SETTINGS = '/devices/getBrewSettings'
SET_BREW_SETTINGS = '/devices/setBrewSettings'
#    Brew Enable
SET_BREW_ENABLE = '/devices/setBrewEnable'
SHOULD_BREW = '/devices/shouldBrew'

# Presets
GET_PRESETS = '/presets/getPresets'
SET_DEVICE_PRESET = '/presets/setDevicePreset'

# Status
GET_DEVICE_STATUS = '/status/getDeviceStatus'
SET_DEVICE_STATUS = '/status/setDeviceStatus'

# --------------------------------------------------------------------
# getWs(serviceName)
#     Builds a web service url for the EOTG API.
#
# Parameters:
#     serviceName - The name of the service to get the URL for.  See
#                   function definition for a valid list of service
#                   names.
#
# Useage Example:
#     webServiceCall = wsConstants.getWs('registerDevice')
#     print(str(webServiceCall))
#     Console output: http://espressotg.info/eotg/api/devices/registerDevice
# --------------------------------------------------------------------
def getWs(serviceName):
    svcUrl = BASE_URL
    return {
        'brewSettingTypes': svcUrl + GET_BS_TYPES,
        'registerDevice': svcUrl + REGISTER_DEVICE,
        'getBrewSettings': svcUrl + GET_BREW_SETTINGS,
        'setBrewSettings': svcUrl + SET_BREW_SETTINGS,
        'setBrewEnable': svcUrl + SET_BREW_ENABLE,
        'shouldBrew': svcUrl + SHOULD_BREW,
        'getDevicePresets': svcUrl + GET_PRESETS,
        'setDevicePreset': svcUrl + SET_DEVICE_PRESET,
        'getDeviceStatus': svcUrl + GET_DEVICE_STATUS,
        'setDeviceStatus': svcUrl + SET_DEVICE_STATUS
    }[serviceName]
