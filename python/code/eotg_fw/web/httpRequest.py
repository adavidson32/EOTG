# (c) EOTG, LLC 2017
# Author: Nathan Muller

import requests
import urllib.parse
import urllib.request
import json
import wsConstants

# --------------------------------------------------------------------
# httpRequest(url, reqParams, urlParams)
#     Builds, sends, and retireves responses for HTTP
#     GET and POST requests.
#
# Parameters:
#     url - The request url.  Use wsConstants.buildUrl
#           to create.
#     reqParams - A dictionary object containing the
#                 request parameters.  Pass in 'None' if
#                 there are none.
#     urlParams - An array containing the url parameters
#                 as strings.  Pass in an empty array if
#                 there are none.
#
# Useage Example 1:
#     webServiceCall = wsConstants.getWs('registerDevice')
#     requestParams =
#       {'deviceIdentifier': '002442', 'macAddress': '00:00:00:FF:AA:AB:EF:47'}
#     response = httpRequest(webServiceCall, requestParams, [])
#     print(str(response))
#       --> Console output: {'deviceId': 29}
#
# Useage Example 2:
#     webServiceCall = wsConstants.getWs('setBrewSettings')
#     # Notice how the json is encoded within the dictionary object.
#     requestParams =
#       {'settings': '{"settings":[{"id": 3, "value": "0:0530,1:0530,2:0600"},{"id": 1, "value": "185"}]}'}
#     response = httpRequest(webServiceCall, requestParams, ['13'])
#     print(str(response))
#       --> Console output: {"error":false,"data":{"brewSettingsUpdateTs": 1492488058016}}
#
# Useage Example 3:
#     webServiceCall = wsConstants.getWs('shouldBrew')
#     response = httpRequest(webServiceCall, None, [])
#     print(str(response))
#       --> Console output: {"shouldBrew": 1}
# --------------------------------------------------------------------
def makeRequest(url, reqParams, urlParams):
    #print("Header to send to server: " + str(reqParams))
    # Build the url
    for param in urlParams:
        url += '/' + param

    # Set up the request headers
    if reqParams is not None:
        data = urllib.parse.urlencode(reqParams).encode()
        response = urllib.request.urlopen(url, data)
    else:
        response = urllib.request.urlopen(url)

    # Get and return the response
    resp = response.read().decode()
    if resp is not None:
        return resp
