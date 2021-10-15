# Example for using ImJoy Engine


## Start the server

```
python -m imjoy.server --host=0.0.0.0 --port=8000
```


## Start a worker plugin

```
python -m imjoy.runner --server-url=http://127.0.0.1:8000 --quit-on-ready example_plugin.py
```