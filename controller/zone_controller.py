import uuid
import os
import json
from flask import request
from csv import writer, reader, DictReader, DictWriter
from config import filename, tempfilename, fields
from pathlib import Path

def create_zones_file_if_not_exists():
    if not Path(filename).is_file():
        open(filename, "w").close()

def transform_zone(zone):
    return {fields[0]: zone[0], fields[1]: zone[1], fields[2]: json.loads(zone[2])}

def create_zone():
    create_zones_file_if_not_exists()
    zone_id = uuid.uuid1()
    with open(filename, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([zone_id, request.json[fields[1]], request.json[fields[2]]])
    return {"id": str(zone_id)}

def get_zones():
    create_zones_file_if_not_exists()
    with open(filename, newline='') as csvfile:
        zones = list(reader(csvfile))

    return [transform_zone(item) for item in zones]

def delete_zone(zone):
    create_zones_file_if_not_exists()
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
    os.remove(filename)
    os.rename(tempfilename, filename)

    return {"deleted": zone} if is_zone_found else {"deleted": None}
