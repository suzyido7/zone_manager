from flask import Flask
from flask_cors import CORS
import controller.zone_controller as zone_controller

app = Flask(__name__)
CORS(app)

@app.route('/zone', methods=['POST'])
def create_zone():
    return zone_controller.create_zone()

@app.route('/zones', methods=['GET'])
def get_zones():
    return zone_controller.get_zones()

@app.route('/zone/<zone>', methods=['DELETE'])
def delete_zone(zone):
    return zone_controller.delete_zone(zone)

if __name__ == '__main__':
    app.run()
