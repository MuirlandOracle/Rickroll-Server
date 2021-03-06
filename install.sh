#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "[-] Script needs to be run with root privileges"
    exit;
fi


get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
}
get_script_dir;


echo "[+] Creating the service unit file"
cat << EOF > /etc/systemd/system/rickroll.service
[Unit]
Description=Telnet Rickroll Server
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=$DIR
ExecStart=$DIR/main.py
[Install]
WantedBy=multi-user.target
EOF

systemctl enable  --now rickroll
