import sys
import argparse
import configparser
import csv
import logging
import logging_config
import time
import schedule
import json
import requests
from datetime import datetime
from pathlib import Path

from utils.utils import is_supported_os, get_active_app_name
from counter.key_counter import key_counter
from counter.mouse_counter import mouse_counter
from monitor.key_monitor import create_key_monitor
from monitor.mouse_moitor import create_mouse_monitor
from exceptions import UnsupportedException

log = logging.getLogger(__name__)


def write_head(out_file_path):
    header = ['date', 'user_name', 'alphanumeric_key_count', 'special_key_count', 'keyboard_activity',
              'mouse_movement', 'mouse_click_count', 'mouse_scroll_count', 'mouse_activity', 'active_app_name']
    with open(out_file_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(header)


def post_data(end_point, username, password, app_name):
    data = {'username': username,
            'password': password,
            'alphanumeric_key_count': key_counter.alphanumeric,
            'special_key_count': key_counter.special,
            'keyboard_activity': (key_counter.alphanumeric + key_counter.special),
            'mouse_movement': mouse_counter.movement,
            'mouse_click_count': mouse_counter.click,
            'mouse_scroll_count': mouse_counter.scroll,
            'mouse_activity': (mouse_counter.movement + mouse_counter.click + mouse_counter.scroll),
            'app_name': app_name
            }
    response = requests.post(end_point, json.dumps(data), headers={'Content-Type': 'application/json'})
    if not response.status_code == 200:
        c = response.status_code
        r = response.json()
        log.error("The request failed. code = {}, message = {}, errors = {}".format(c, r['message'], r['error']))


def write_data(out_file_path, now, username, app_name):
    data = [now, username, key_counter.alphanumeric, key_counter.special,
            (key_counter.alphanumeric + key_counter.special), mouse_counter.movement, mouse_counter.click,
            mouse_counter.scroll, (mouse_counter.movement + mouse_counter.click + mouse_counter.scroll), app_name]
    with open(out_file_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def job(end_point, out_file_path, username, password):
    now = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.now())
    app_name = get_active_app_name()
    # post and write data
    post_data(end_point, username, password, app_name)
    write_data(out_file_path, now, username, app_name)
    # reset counter
    key_counter.reset()
    mouse_counter.reset()


def main():
    # check OS
    is_supported_os()

    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', default='gameinn.conf', type=str)
    parser.add_argument('--out', default='data.csv', type=str)
    args = parser.parse_args()
    log.info("parse argument. --conf = {0}, --out = {1}".format(args.conf, args.out))

    # parse config
    conf_file_path = args.conf
    config = configparser.ConfigParser()
    config.read(conf_file_path, 'UTF-8')
    conf = config['CONF']
    end_point = conf['END_POINT']
    username = conf['USER']
    password = conf['PASS']

    # output path
    out_file_path = args.out
    out_file = Path(out_file_path)
    if out_file.is_file():
        pass
    else:
        out_file.touch()
        write_head(out_file_path)

    # start monitoring keyboard or mouse event in other thread
    key_monitor = create_key_monitor()
    mouse_monitor = create_mouse_monitor()
    key_monitor.start()
    mouse_monitor.start()

    # setting job
    schedule.every(10).minutes.do(job, end_point, out_file_path, username, password)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    try:
        main()
    except UnsupportedException as ue:
        log.error(ue)
        sys.exit(1)
