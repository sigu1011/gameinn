#!/bin/bash

echo "stop client application, exec kill <pid>."
echo "check th pid of gameinn_client.py with pgrep, please make sure you can stop it."

user=`whoami`
pid=`pgrep -u ${user} -f gameinn_client.py`

if [ -z ${pid} ]; then
  echo "gameinn_client.py is not running."
  exit 0
fi

read -p "${pid} - kill this pid? (y/n): " yn
case "$yn" in
  [yY]*)
    kill ${pid}
    ;;
  *)
    echo "abort this script."
    exit 0
    ;;
esac
