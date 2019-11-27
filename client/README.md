# gameinn client

## About

* This application uses [pynput](https://github.com/moses-palmer/pynput).
* Collect keyboard and mouse activity, and POST data to gameinn server.

## Enviroment

* ubuntu 18.04
  * apt install xdotool
* python 3.6
  * pip install -r requirements.txt

## How to use

### Start

```
python gameinn_client.py
```

* When the app starts, ``data.csv`` is generated, and the keyboard and mouse activity are recorded.
* POST data to server every 10 minutes.

```
# data.csv
date,user_name,alphanumeric_key_count,special_key_count,keyboard_activity,mouse_movement,mouse_click_count,mouse_scroll_count,mouse_activity,active_app_name
2019-11-26 17:00:00,admin,62,2,64,0,0,0,0,jetbrains-pycharm-ce
2019-11-26 17:10:00,admin,0,0,0,239,2,7,248,Firefox
2019-11-26 17:20:00,admin,2,2,4,120,4,0,124,Gnome-terminal
...
```

### Stop

```
# Stop by kill
./stop.sh
```

## Data format

* Data format of ``data.csv``.

column | detail
--- | ---
date | Date of data collection.
user_name | User name. (Can be set ``gameinn.conf``)
alphanumeric_key_count | Number of alphanumeric key presses. (ex. ``a``, ``b``, ...)
special_key_count | Number of special key presses. (ex. ``Shift``, ``Alt``, ...)
keyboard_activity | Sum keyboard activity. (alphanumeric_key_count + keyboard_activity)
mouse_movement | mouse movement.
mouse_click_count | Number of mouse click.
mouse_scroll_count | Number of mouse scroll.
mouse_activity | Sum mouse actibity. (mouse_click_count + mouse_scroll_count + mouse_activity)
active_app_name | The app that was active when the data was collected.
