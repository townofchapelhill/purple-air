import requests
import json
import csv
import re
import os
import datetime
import traceback

# Open log file
log = open("purpleairlog.txt", "a")
now = datetime.datetime.now()


def get_purple_air():
    url = "https://www.purpleair.com/json?show=10586"
    response = requests.get(url)

    try:
        data = json.loads(response.content.decode('utf-8'))
    except RuntimeError:
        log.write(now.strftime("%Y-%m-%d %H:%M") + ": Could not load data from url. \n")
        log.write(traceback.format_exc())

    log.write(now.strftime("%Y-%m-%d %H:%M") + ": Data loaded from url successfully. \n")
    return data


def get_data(info_sheet):
    # stores response info as a variable
    purple_air_info = get_purple_air()

    # creates ordered list of float/integers from stats
    p = re.compile(r"[-+]?\d*\.\d+|\d+")
    stats_0 = p.findall(purple_air_info["results"][0]["Stats"])
    stats_1 = p.findall(purple_air_info["results"][1]["Stats"])

    # deletes unwanted indexes in lists
    for i in sorted([1, 3, 5, 7, 9, 11], reverse=True):
        del stats_0[i]
        del stats_1[i]

    print("Here's your info: ")
    print(purple_air_info)
    # writes weather data to CSV
    writer = csv.writer(info_sheet)
    writer.writerow([purple_air_info["mapVersion"], purple_air_info["baseVersion"], purple_air_info["mapVersionString"],
                     purple_air_info["results"][0]["ID"], purple_air_info["results"][0]["ParentID"],
                     purple_air_info["results"][0]["Label"], purple_air_info["results"][0]["DEVICE_LOCATIONTYPE"],
                     purple_air_info["results"][0]["THINGSPEAK_PRIMARY_ID"],
                     purple_air_info["results"][0]["THINGSPEAK_PRIMARY_ID_READ_KEY"],
                     purple_air_info["results"][0]["THINGSPEAK_SECONDARY_ID"],
                     purple_air_info["results"][0]["THINGSPEAK_SECONDARY_ID_READ_KEY"],
                     purple_air_info["results"][0]["Lat"], purple_air_info["results"][0]["Lon"],
                     purple_air_info["results"][0]["PM2_5Value"],
                     datetime.datetime.utcfromtimestamp(purple_air_info["results"][0]["LastSeen"]).replace
                     (tzinfo=datetime.timezone.utc),
                     purple_air_info["results"][0]["State"], purple_air_info["results"][0]["Type"],
                     purple_air_info["results"][0]["Hidden"], purple_air_info["results"][0]["Flag"],
                     purple_air_info["results"][0]["DEVICE_BRIGHTNESS"],
                     purple_air_info["results"][0]["DEVICE_HARDWAREDISCOVERED"],
                     purple_air_info["results"][0]["DEVICE_FIRMWAREVERSION"], purple_air_info["results"][0]["Version"],
                     datetime.datetime.utcfromtimestamp(purple_air_info["results"][0]["LastUpdateCheck"]).replace
                     (tzinfo=datetime.timezone.utc),
                     purple_air_info["results"][0]["Uptime"],
                     purple_air_info["results"][0]["RSSI"], purple_air_info["results"][0]["isOwner"],
                     purple_air_info["results"][0]["A_H"], purple_air_info["results"][0]["temp_f"],
                     purple_air_info["results"][0]["humidity"], purple_air_info["results"][0]["pressure"],
                     purple_air_info["results"][0]["AGE"], stats_0[0], stats_0[1], stats_0[2], stats_0[3], stats_0[4],
                     stats_0[5], stats_0[6], stats_0[7], stats_0[8], stats_0[9],
                     purple_air_info["results"][1]["ID"], purple_air_info["results"][1]["ParentID"],
                     purple_air_info["results"][1]["Label"], purple_air_info["results"][1]["DEVICE_LOCATIONTYPE"],
                     purple_air_info["results"][1]["THINGSPEAK_PRIMARY_ID"],
                     purple_air_info["results"][1]["THINGSPEAK_PRIMARY_ID_READ_KEY"],
                     purple_air_info["results"][1]["THINGSPEAK_SECONDARY_ID"],
                     purple_air_info["results"][1]["THINGSPEAK_SECONDARY_ID_READ_KEY"],
                     purple_air_info["results"][1]["Lat"], purple_air_info["results"][1]["Lon"],
                     purple_air_info["results"][1]["PM2_5Value"],
                     datetime.datetime.utcfromtimestamp(purple_air_info["results"][1]["LastSeen"]).replace
                     (tzinfo=datetime.timezone.utc),
                     purple_air_info["results"][1]["State"], purple_air_info["results"][1]["Type"],
                     purple_air_info["results"][1]["Hidden"], purple_air_info["results"][1]["Flag"],
                     purple_air_info["results"][1]["DEVICE_BRIGHTNESS"],
                     purple_air_info["results"][1]["DEVICE_HARDWAREDISCOVERED"],
                     purple_air_info["results"][1]["DEVICE_FIRMWAREVERSION"], purple_air_info["results"][1]["Version"],
                     purple_air_info["results"][1]["LastUpdateCheck"], purple_air_info["results"][1]["Uptime"],
                     purple_air_info["results"][1]["RSSI"], purple_air_info["results"][1]["isOwner"],
                     purple_air_info["results"][1]["A_H"], purple_air_info["results"][1]["temp_f"],
                     purple_air_info["results"][1]["humidity"], purple_air_info["results"][1]["pressure"],
                     purple_air_info["results"][1]["AGE"], stats_1[0], stats_1[1], stats_1[2], stats_1[3], stats_1[4],
                     stats_1[5], stats_1[6], stats_1[7], stats_1[8], stats_1[9]])


# main function to create log and call get_data
def main():
    info_sheet = open("purple-air.csv", "a")

    # if there is data in the response, write CSV headers
    if os.stat("purple-air.csv").st_size == 0:
        writer = csv.writer(info_sheet)
        writer.writerow(["mapVersion", "baseVersion", "mapVersionString", "results.0.ID", "results.0.ParentID",
                         "results.0.Label", "results.0.DEVICE_LOCATIONTYPE", "results.0.THINGSPEAK_PRIMARY_ID",
                         "results.0.THINGSPEAK_PRIMARY_ID_READ_KEY", "results.0.THINGSPEAK_SECONDARY_ID",
                         "results.0.THINGSPEAK_SECONDARY_ID_READ_KEY", "results.0.Lat", "results.0.Lon",
                         "results.0.PM2_5Value", "results.0.LastSeen", "results.0.State", "results.0.Type",
                         "results.0.Hidden", "results.0.Flag", "results.0.DEVICE_BRIGHTNESS",
                         "results.0.DEVICE_HARDWAREDISCOVERED", "results.0.DEVICE_FIRMWAREVERSION", "results.0.Version",
                         "results.0.LastUpdateCheck", "results.0.Uptime", "results.0.RSSI", "results.0.isOwner",
                         "results.0.A_H", "results.0.temp_f", "results.0.humidity", "results.0.pressure",
                         "results.0.AGE", "results.0.Stats.v", "results.0.Stats.v1", "results.0.Stats.v2", "results.0.Stats.v3",
                         "results.0.Stats.v4", "results.0.Stats.v5", "results.0.Stats.v6", "results.0.Stats.pm",
                         "results.0.Stats.lastModified", "results.0.Stats.timeSinceModified",
                         "results.1.ID", "results.1.ParentID", "results.1.Label", "results.1.DEVICELOCATIONTYPE",
                         "results.1.THINGSPEAK_PRIMARY_ID", "results.1.THINGSPEAK_PRIMARY_ID_READ_KEY",
                         "results.1.THINGSPEAK_SECONDARY_ID", "results.1.THINGSPEAK_SECONDARY_ID_READ_KEY",
                         "results.1.Lat", "results.1.Lon", "results.1.PM2_5Value", "results.1.LastSeen", "results.1.State",
                         "results.1.Type", "results.1.Hidden", "results.1.Flag", "results.1.DEVICE_BRIGHTNESS",
                         "results.1.DEVICE_HARDWAREDISCOVERED", "results.1.DEVICE_FIRMWAREVERSION", "results.1.Version",
                         "results.1.LastUpdateCheck", "results.1.Uptime", "results.1.RSSI", "results.1.isOwner",
                         "results.1.A_H", "results.1.temp_f", "results.1.humidity", "results.1.pressure",
                         "results.1.AGE", "results.1.Stats.v", "results.1.Stats.v1", "results.1.Stats.v2", "results.1.Stats.v3",
                         "results.1.Stats.v4", "results.1.Stats.v5", "results.1.Stats.v6", "results.1.Stats.pm",
                         "results.1.Stats.lastModified", "results.1.Stats.timeSinceModified"])

    try:
        get_data(info_sheet)
    except RuntimeError:
        log.write(now.strftime("%Y-%m-%d %H:%M") + ": Could not gather data. \n")
        log.write(traceback.format_exc())
    log.write(now.strftime("%Y-%m-%d %H:%M") + ": Data gathered successfully. \n")

    info_sheet.close()
    log.close()


# main
main()
