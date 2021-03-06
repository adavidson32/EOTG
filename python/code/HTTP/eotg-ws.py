import httpRequest
import json
import sqlite3 
import wsConstants

ws = wsConstants
# Get the Brew Settings from the web server
def getBrewSettings():
    try:
        # Get connection to database
        conn = sqlite3.connect('eotg.db')
        conn.row_factory = dict_factory
        # Get device id (As a string)
        deviceId = getDeviceId(conn)
        resp = httpRequest.makeRequest(ws.getWs('getBrewSettings'), None, [deviceId])
        devSettings = json.loads(resp)
        brewSettings = devSettings['brewSettings']
        # Put settings in settings table
        updates = []
        for setting in brewSettings:
            updateItems = (setting['brew_setting_value'], setting['brew_setting_type_id'])
            updates.extend(updateItems)
        c.executemany('INSERT INTO brew_settings values (?,?,now())', updates)
        conn.commit()
        conn.close()
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)

# Send the device's status to the web server
def putDeviceStatus():
    try:
        # Get connection to database
        conn = sqlite3.connect('eotg.db')
        conn.row_factory = dict_factory
        # Get device id (As a string)
        deviceId = getDeviceId(conn)
        # Get status items from the database
        c = conn.cursor()
        c.execute('select * from device_info limit 1')
        status = c.fetchone()
        statusStr = '"newStatusItems":[{"statusType": "battery_level", "statusValue": ' + str(status['battery_level']) + 
            '}, {"statusType": "water_level", "statusValue": ' + str(status['water_level']) + 
            '}, {"statusType": "current_state", "statusValue": ' + str(status['current_state']) + 
            '}, {"statusType": "ac_power_state", "statusValue": ' + str(status['ac_state']) 
        requestParam = {'newStatusItems': statusStr}
        # Update the status items on the web server
        resp = httpRequest.makeRequest(ws.getWs('setDeviceStatus'), requestParam, [deviceId])
        conn.close()
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)

# Check if the device should be in a brewing state
def shouldBrew():
    try:
        # Get the the brew status from the web server
        resp = httpRequest.makeRequest(ws.getWs('shouldBrew'), None, [])
        devSettings = json.loads(resp)
        shouldBrew = devSettings['shouldBrew']
        # Update the brew status in the local db
        conn = sqlite3.connect('eotg.db')
        t = (shouldBrew, )
        cursor = conn.cursor()
        cursor.execute('update device_info set remote_brew_state = ?', t)
        conn.commit()
        conn.close()
        return shouldBrew
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)


# Register our device.  
# Params: The device's serial number and mac address.
# RETURNS: the device's ID from the web server
def registerDevice(deviceIdentifier, macAddr):
    try:
        # Get connection to database
        conn = sqlite3.connect('eotg.db')
        # Build request param
        requestParam = {'deviceIdentifier': deviceIdentifier, 'macAddress': macAddr}
        # Get the device's ID back from the web server
        resp = httpRequest.makeRequest(ws.getWs('setDeviceStatus'), requestParam, [])
        # Put the device id in the database
        devId = json.loads(resp)
        deviceId = (devId['deviceId'], )
        cursor = conn.cursor()
        cursor.execute('update device_info set given_id_num = ?', deviceId)
        conn.commit()
        conn.close()
        return deviceId[0]
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)
        return -1

# Get the currently configured preset mode.  -1 => manual mode.
def getCurrentPreset():
    try:
        # Get connection to database
        conn = sqlite3.connect('eotg.db')
        # Get the device Id from the db
        deviceId = getDeviceId(conn)
        # Get the device's status
        resp = httpRequest.makeRequest(ws.getWs('getDeviceStatus'), requestParam, [deviceId])
        # Get the preset mode id from the web server results
        statusJson = json.loads(resp)
        statusId = statusJson['brew_preset_id']
        cursor = conn.cursor()
        cursor.execute('update device_info set preset_state = ?', statusId)
        conn.commit()
        conn.close()
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)

# Get all device presets
def getAllPresets():
    try:
        # Get connection to database
        conn = sqlite3.connect('eotg.db')
        conn.row_factory = dict_factory
        # Get the device Id from the db
        deviceId = getDeviceId(conn)
        # Get the device's presets
        resp = httpRequest.makeRequest(ws.getWs('getDevicePresets'), requestParam, [deviceId])
        # Put the preset in the database
        presets = json.loads(resp)['brew_presets']
        cursor = conn.cursor()
        cursor.execute('delete from preset_list')
        newPresets = {}
        oldPresetName = ''
        newSettings = {}
        for preset in presets:
            presetName = preset['preset_name']
            colName = getSettingTypeName(preset['setting_type_id'])
            if colName != '-1':
                newSettings[getSettingTypeName(preset['setting_type_id'])] = preset['setting_value']
            else:
                continue

            if presetName != oldPresetName and oldPresetName != '':
                new_presets[oldPresetName] = newSettings
                newSettings = {}

            oldPresetName = presetName
        
        insertPresets(newPresets, conn)
        conn.commit()
        conn.close()
    except Exception as err:
        print('Exception trying to get brew settings: ')
        print(err)

#--------------------------------------------------------------------------------------------
#
# HELPER METHODS --------------------------------------------------------
#
#--------------------------------------------------------------------------------------------

# Get the device id from the database
def getDeviceId(conn):
    c = conn.cursor()
    # Get device id from db
    c.execute('select given_id_num from device_info')
    deviceIdRow = c.fetchone()['given_id_num']
    if deviceId is None or deviceId <= 0:
        deviceId = registerDevice()
    c.close()
    return str(deviceId)

# Turn db selct results into dictionaries
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d

# Get the name of the setting based on the preset type id.  Hardcoded because fuck coding any more shit.
def getSettingTypeName(presetTypeId):
    colName = '-1'
    if int(presetTypeId) == 1:
        colName = 'temp'
    elif int(presetTypeId) == 2:
         colName =  'volume'
    elif int(presetTypeId) == 6:
         colName = 'colors'

    return colName

def insertPresets(newPresets, conn):
    # TODO : check col names to make sure they're right
    queryStr = 'insert into preset_list (ID,name,'
    i = 1
    for key in newPresets:
        newPreset = newPresets[key]
        for subkey in newPreset:
            queryStr += subkey + ','
        queryStr = queryStr[:-1]
        queryStr += ') values (' + str(i) + ',' + key + ','
        for subkey in newPreset:
            queryStr += newPreset[subkey] + ','
        queryStr = queryStr[:-1]
        queryStr += ');'
        print(queryStr)
        c = conn.cursor
        c.execute(queryStr)
        c.close()
        
        i++
