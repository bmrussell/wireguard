#!/usr/bin/env python3

# Print Wireguard logs to JSON
# USE:
#   docker exec -it wireguard wg show all dump | ./conv.py

import json
import fileinput
from datetime import datetime

entries = {}
for line in fileinput.input():
    try:
        interface, publickey, privatekey, endpoint, allowedips, lasthandshake, received, sent, keepalive = line.split()
        entries[publickey] = {"publickey": publickey, 
                              "endpoint": endpoint, 
                              "allowedips": allowedips, 
                              "lasthandshake": datetime.utcfromtimestamp(int(lasthandshake)).strftime('%Y-%m-%d %H:%M:%S'),
                              "sent": '{0:.2f}MiB'.format(float(sent)/1048576.0),
                              "received": '{0:.2f}MiB'.format(float(received)/1048576.0)}
    except ValueError as ve:
        continue


print(json.dumps(entries, indent=4, sort_keys=True))