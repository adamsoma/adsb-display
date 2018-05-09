from flask import Flask, request
from geographiclib.geodesic import Geodesic
import math

geod = Geodesic.WGS84

app = Flask(__name__)

@app.route('/selected-plane', methods=['POST'])
def selected_plane():
    p_alt = float(request.form.get('alt'))
    p_lat = float(request.form.get('lat'))
    p_lon = float(request.form.get('lon'))

    s_alt = float(89)
    s_lat = float(44.56696)
    s_lon = float(-123.27578333)

    g = geod.Inverse(s_lat, s_lon, p_lat, p_lon)

    hz_dist = g['s12']
    vt_diff = (p_alt * 0.3048) - s_alt 

    arm_azi = g['azi1']
    arm_rad = math.atan(vt_diff / hz_dist)
    arm_deg = math.degrees(arm_rad)

    print(arm_azi, arm_deg)

    return ''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)
