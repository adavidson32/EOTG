# web/eotg_ws.py

import sys
from gmacser import getserial, getMAC
import httpRequest
import json
import sqlite3
import wsConstants

ws = wsConstants
class eotg_ws:
    # CTOR
    def __init__(self):
        self.deviceId = -1

    # Get the Brew Settings from the web server
    def getBrewSettings(self, conn):
        try:
            # Get device id (As a string)
            deviceId = self.getDeviceId(conn)
            resp = httpRequest.makeRequest(ws.getWs('getBrewSettings'), None, [deviceId])
            devSettings = json.loads(resp)
            brewSettings = devSettings['brewSettings']
            updateItems = ('', )
            for setting in brewSettings:
                if self.getSettingTypeName(setting['brew_setting_type_id']) != '-1':
                    updateItems = (setting['brew_setting_type_id'], setting['brew_setting_value'])
            c = conn.cursor()
            if len(updateItems) == 2:
                c.execute("INSERT INTO profile_list values (-1, 'manual', ?, ?, '')", updateItems)
            conn.commit()
        except Exception as err:
            print('Exception trying to get brew settings: ')
            print(err)

    # Send the device's status to the web server
    def putDeviceStatus(self):
        try:
            # Get connection to database
            conn = sqlite3.connect('../main/eotg.db')
            conn.row_factory = self.dict_factory
            # Get device id (As a string)
            deviceId = self.getDeviceId(conn)
            # Get status items from the database
            c = conn.cursor()
            c.execute('select * from device_info')
            status = c.fetchone()
            statusStr = '''[{"statusType": "battery_level", "statusValue": ''' + str(status['battery_level']) + '''}, {"statusType": "water_level", "statusValue": ''' + str(status['water_level']) + '''}, {"statusType": "current_state", "statusValue": ''' + str(status['current_state']) + '''}, {"statusType": "ac_power_state", "statusValue": ''' + str(status['ac_state']) + '}]'
            requestParam = {'newStatusItems': statusStr}
            # Update the status items on the web server
            resp = httpRequest.makeRequest(ws.getWs('setDeviceStatus'), requestParam, [deviceId])
            conn.commit()
            conn.close()
        except Exception as err:
            print('Exception trying to set brew settings: ')
            print(err)

    # Check if the device should be in a brewing state
    def shouldBrew(self):
        try:
            # Get the the brew status from the web server
            resp = httpRequest.makeRequest(ws.getWs('shouldBrew'), None, [])
            devSettings = json.loads(resp)
            shouldBrew = devSettings['shouldBrew']
            # Update the brew status in the local db
            conn = sqlite3.connect('../main/eotg.db')
            t = (shouldBrew, )
            cursor = conn.cursor()
            cursor.execute('update device_info set remote_brew_start = ?', t)
            conn.commit()
            conn.close()
            return shouldBrew
        except Exception as err:
            print('Exception trying to check brew state: ')
            print(err)

    # Set the brew state to low after we start a brew
    def brewStarted(self):
        try:
            # Tell the server we have started brewing and don't need to have brew state high anymore.
            resp = httpRequest.makeRequest(ws.getWs('setBrewEnable'), {'nate': 'Muller'}, ['0'])
            responseErr = json.loads(resp)['error']
            responseMsg = json.loads(resp)['message']
            if responseErr:
                print(responseMsg)

        except Exception as err:
            print('Exception trying to tell server a brew started: ')
            print(err)

    # Register our device.
    # Params: The device's serial number and mac address.
    # RETURNS: the device's ID from the web server
    def registerDevice(self, deviceIdentifier, macAddr):
        try:
            # Get connection to database
            conn = sqlite3.connect('../main/eotg.db')
            # Build request param
            requestParam = {'deviceIdentifier': deviceIdentifier, 'macAddress': macAddr}
            data = []
            # Get the device's ID back from the web server
            resp = httpRequest.makeRequest(ws.getWs('registerDevice'), requestParam, [])
            # Put the device id in the database
            devId = json.loads(resp)
            deviceId = (devId['deviceId'], )
            cursor = conn.cursor()
            cursor.execute('update device_info set given_id_num = ?', deviceId)
            conn.commit()
            conn.close()
            return deviceId[0]
        except Exception as err:
            print('Exception trying to register the device: ')
            print(err)
            return -1

    # Get the currently configured preset mode.  -1 => manual mode.
    def getCurrentPreset(self):
        try:
            # Get connection to database
            conn = sqlite3.connect('../main/eotg.db')
            # Get the device Id from the db
            deviceId = self.getDeviceId(conn)
            # Get the device's status
            resp = httpRequest.makeRequest(ws.getWs('getDeviceStatus'), None, [deviceId])
            # Get the preset mode id from the web server results
            statusJson = json.loads(resp)
            statusId = statusJson['brew_preset_id']
            cursor = conn.cursor()
            cursor.execute('update device_info set preset_state = ?', (statusId, ))
            conn.commit()
            conn.close()
        except Exception as err:
            print('Exception trying to get the current device state: ')
            print(err)

    # Get all device presets
    def getAllPresets(self):
        try:
            # Get connection to database
            conn = sqlite3.connect('../main/eotg.db')
            conn.row_factory = self.dict_factory
            # Get the device Id from the db
            devId = self.getDeviceId(conn)
            # Get the device's presets
            resp = httpRequest.makeRequest(ws.getWs('getDevicePresets'), None, [devId])
            # Put the preset in the database
            presets = json.loads(resp)['brewPresets']
            cursor = conn.cursor()
            cursor.execute('delete from profile_list')
            newPresets = {}
            oldPresetName = ''
            newSettings = {}
            for preset in presets:
                presetName = preset['preset_name']
                colName = self.getSettingTypeName(preset['setting_type_id'])
                if colName != '-1':
                    newSettings[self.getSettingTypeName(preset['setting_type_id'])] = preset['setting_value']
                else:
                    continue
                if presetName != oldPresetName and oldPresetName != '':
                    newPresets[oldPresetName] = newSettings
                    newSettings = {}
                oldPresetName = presetName

            self.getBrewSettings(conn)
            self.insertPresets(newPresets, conn)
            conn.commit()
            conn.close()
        except Exception as err:
            print('Exception trying to get all device presets: ')
            print(err)

    #--------------------------------------------------------------------------------------------
    #
    # HELPER METHODS --------------------------------------------------------
    #
    #--------------------------------------------------------------------------------------------

    # Get the device id from the database
    def getDeviceId(self, conn):
        if self.deviceId < 0:
            try:
                c = conn.cursor()
                # Get device id from db
                c.execute('select given_id_num from device_info')
                self.setDeviceId(c.fetchone()[0])
                if self.deviceId is None or self.deviceId <= 0:
                    self.setDeviceId(registerDevice(getserial(), getMAC('wlan0')))
                c.close()
            except Exception as err:
                print('Exception trying to get device id: ')
                print(str(err))

        return str(self.deviceId)

    # Turn db selct results into dictionaries
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d

    # Get the name of the setting based on the preset type id.  Hardcoded because fuck coding any more shit.
    def getSettingTypeName(self, presetTypeId):
        colSettings = '-1'
        if int(presetTypeId) == 1:
            colSettings = 'temp'
        elif int(presetTypeId) == 2:
             colSettings =  'volume'
        elif int(presetTypeId) == 6:
             colSettings = 'color_pattern'

        return colSettings

    def insertPresets(self, newPresets, conn):
        # TODO : check col names to make sure they're right
        #Columns:      | prof_num |  prof_name  | temp | volume |   color_pattern   |
        queryStr = 'insert into profile_list (prof_num, prof_name, '
        i = 1
        for key in newPresets:
            newPreset = newPresets[key]
            for subkey in newPreset:
                queryStr += subkey + ','
            queryStr = queryStr[:-1]
            queryStr += ') values (' + str(i) + ",'" + key + "',"
            for subkey in newPreset:
                queryStr += newPreset[subkey] + ','
            queryStr = queryStr[:-1]
            queryStr += ');'
            print(queryStr)
            c = conn.cursor()
            c.execute(queryStr)
            c.close()

            i+=1

    def setDeviceId(self, dId):
        self.deviceId = dId
