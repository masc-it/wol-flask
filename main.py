from wakeonlan import send_magic_packet
from flask import Flask

app = Flask(__name__)

@app.route('/wol/<mac>')
def wol(mac):
    send_magic_packet(mac, port=9)
    return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) #,ssl_context="adhoc"