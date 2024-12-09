from flask import Flask, render_template, request

app = Flask(__name__)

Auth_url = f"http://omada-controller-url/api/v2/auth"


@app.route("/", methods=["GET"])
def home():
    client_mac = request.args.get("clientMac")
    ap_mac = request.args.get("apMac")
    ssid_name = request.args.get("ssidName")
    return render_template("index.html", client=client_mac, ap=ap_mac, ssid=ssid_name)


@app.route("/authenticate", methods=["GET"])
def authenticate():
    client_mac = request.args.get("clientMac")
    ap_mac = request.args.get("apMac")
    ssid_name = request.args.get("ssidName")
    return render_template("display.html", infos=[client_mac, ap_mac, ssid_name])


if __name__ == "__main__":
    app.run(debug=True)
