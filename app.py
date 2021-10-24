from os import error
from flask import Flask, flash, request
from flask import render_template
from flask.wrappers import Request

import ipaddress
app = Flask(__name__)
app.debug = True



@app.route("/", methods=['GET','POST'])

def check():
    if request.method == 'GET':
        ipv4 =  request.args.get('ipaddress')
        try:
            ip = ipaddress.ip_address(ipv4)
            rightIPmsg = "Valid"

            if isinstance(ip, ipaddress.IPv4Address):
                iplist = ipv4.split('.')
                firstOctet = int(iplist[0])
                if firstOctet >=0 and firstOctet<=127:
                    class_IP = "Class A"
                elif firstOctet >=128 and firstOctet<=191:
                    class_IP = "Class B"
                elif firstOctet >=192 and firstOctet<=223:
                    class_IP = "Class C"
                elif firstOctet >=224 and firstOctet<=239:
                    class_IP = "Class D"
                elif firstOctet >=240 and firstOctet<=255:
                    class_IP = "Class E"
                else:
                    class_IP = "Invalid"

                type_IP_version = "IPv4 Address"
            elif isinstance(ip,  ipaddress.IPv6Address):
                type_IP_version = "IPv6 Address"

            return render_template('index.html', msg = rightIPmsg, type_IP_version=type_IP_version, class_IP = class_IP)
            #  mycss = "border: 4px solid rgb(127, 0, 212);"
        except ValueError:
            wrongIPmsg = "Invalid IP address"
            return render_template('index.html', msg = wrongIPmsg, type_IP_version = "Invalid")
            #  mycss = "border: 4px solid red;"
    

def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()