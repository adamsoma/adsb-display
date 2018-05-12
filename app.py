from flask import Flask, request
from geographiclib.geodesic import Geodesic
import math
import time

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

    #send_data(arm_azi, arm_deg)

    return ''''''


def send_data(bearing, angle):
    #print(socket.gethostname())
    #TCP_IP = '10.42.0.240'
    #TCP_PORT = 5008
    #BUFFER_SIZE = 64

    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #s.bind((TCP_IP, TCP_PORT))
    #s.listen(1)

    #conn1, addr = s.accept()
#    s.listen(1)
#    bearing_temp = "b" + str(bearing)
#    angle_temp = "p" + str(angle)
#    data_b = str.encode(bearing_temp)
#    data_a = str.encode(angle_temp)
    msg = "b" + str(bearing) + "p" + str(angle) + "x"
    data_c = str.encode(msg)
    #print("received data:", data_b)
    #print("received data:", data_a)
    print("sent data:", data_c)
#    conn1.send(data_b)
#    time.sleep(.2)
#    conn1.send(data_a)
    conn1.send(data_c)
    print('Connection address:', addr)
    #print("connection address:", addr)
    #conn1.close()
    #s.close()

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5020)
