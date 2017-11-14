#!/bin/sh


sleep 5

bluetoothctl << EOF
info 00:18:09:1E:BD:B8
EOF

sleep 5
