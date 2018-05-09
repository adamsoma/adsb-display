from flask import Flask, request
from geographiclib.geodesic import Geodesic
import math

geod = Geodesic.WGS84

app = Flask(__name__)

@app.route('/selected-plane', methods=['POST'])
def selected_plane():
    p_alt = request.form.get('alt')
    p_lat = request.form.get('lat')
    p_lon = request.form.get('lon')

    s_alt = 262
    s_lat = 44.56696
    s_lon = -123.27578333

    g = geod.Inverse(s_lat, s_lon, p_lat, p_lon)

    return ''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)
