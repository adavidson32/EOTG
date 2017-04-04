import httplib
import urllib
import json

Post_Params = urllib.urlencode(     )
Post_Headers = (        )

conn = httplib.HTTPConnection("http://espressotg.com/eotg/api/")
conn.request("POST", "", Post_Params, Post_Headers)
response = conn.getresponse()
print response.status, response.reason
