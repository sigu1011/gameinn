#!/bin/bash

ps -aux | head -n 1 | awk '{ printf("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11);}' >> memory.log

while true
do
  ps -aux | grep -e gameinn_client.py | grep -v grep | awk '{ printf("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11);}' >> memory.log
  sleep 1
done
