#!/bin/sh

#systemctl restart bluetooth

sleep 10

bluetoothctl << EOF

power on
devices
connect 00:18:09:1E:BD:B8
exit

EOF

sleep 1
