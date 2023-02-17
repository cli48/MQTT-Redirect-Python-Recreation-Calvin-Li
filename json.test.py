import json

json_data = '{"hardware_serial": "ESP_32", "payload_fields": {"temperature": 24.81999969, "pressure": 99.51672363, "altitude": 151.6508484}}'

data = json.loads(json_data)

temp = data['payload_fields']['temperature']
pressure = data['payload_fields']['pressure']
altitude = data['payload_fields']['altitude']

sensor_data = {'temperature': temp, 'pressure': pressure, 'altitude': altitude}

print(sensor_data)


    # data = json.loads(payload_string)

    # temp = data['payload_fields']['temperature']
    # pressure = data['payload_fields']['pressure']
    # altitude = data['payload_fields']['altitude']

    # temp = (temp*1.8) + 32 #convert C to F
    # pressure = pressure/6.895 #convert kpa to psi
    # altitude = altitude*3.281 #Meters to feet

    # edited_sensor_data = {'temperature': temp, 'pressure': pressure, 'altitude': altitude}
    # print(payload_string)
    # print(edited_sensor_data)