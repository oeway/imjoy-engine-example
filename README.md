# Example for using ImJoy Engine

## Installation

```
git clone https://github.com/oeway/imjoy-engine-example
cd imjoy-engine-example
pip install -r requirements.txt
```

## Start the server

In a terminal, you can start the server by running
```
python -m imjoy.server --host=0.0.0.0 --port=8000 --allow-origin=https://lib.imjoy.io
```
Note that you should keep this terminal running all the time, 
so maybe run the above command using virtual command tools such as `screen`.


## Start a worker plugin
In another terminal, start the worker plugin:
```
python -m imjoy.runner --server-url=http://127.0.0.1:8000 example_plugin.py
```

You an also run the worker in another computer, but please change the server url to the external ip (not localhost or 127.0.0.1) of the server computer.

## Start a plugin in ImJoy
 * Goto https://imjoy.io/lite (you can also use any imjoy enabled website)
 * Create a client plugin in Python (see [client_plugin.py](client_plugin.py)) or as ImJoy plugin (see [client_plugin.imjoy.html](./client_plugin.imjoy.html)). Note: To load the imjoy plugin, you need to use the ImJoy lite available at http://127.0.0.1:8000/static/lite.html
