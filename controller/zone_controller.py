import uuid
import os
import json
from flask import request, jsonify
from csv import writer, reader, DictReader, DictWriter
from config import filename, tempfilename, fields

def create_zone():
    zone_id = uuid.uuid1()
    with open(filename, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([zone_id, request.json[fields[1]], request.json[fields[2]]])
        f_object.close()
    return {"id": str(zone_id)}

def transform_zone(zone):
    return {fields[0]: zone[0], fields[1]: zone[1], fields[2]: json.loads(zone[2])}

def get_zones():
    with open(filename, newline='') as csvfile:
        zones = list(reader(csvfile))
        if len(zones) == 0:
            return []

    return [transform_zone(item) for item in zones]

def delete_zone(zone):
    is_zone_found = False
    print(zone)
    with open(filename, 'r') as csvfile, open(tempfilename, 'a', newline='') as tempfile:
        reader = DictReader(csvfile, fieldnames=fields)
        writer = DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row[fields[0]] == zone:
                print('deleting zone:', zone)
                is_zone_found = True
                continue
            writer.writerow(row)
    csvfile.close()
    os.remove(filename)
    os.rename(tempfilename, filename)

    return {"deleted": zone} if is_zone_found else {"deleted": None}
