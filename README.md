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
python -m imjoy.server --host=0.0.0.0 --port=8000 -enable-server-apps --allow-origin=* --allow-origin=https://lib.imjoy.io
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
 * Create a new window plugin
```html
<config lang="json">
{
  "name": "Test Client",
  "type": "window",
  "tags": [],
  "ui": "",
  "version": "0.1.0",
  "cover": "",
  "description": "[TODO: describe this plugin with one sentence.]",
  "icon": "extension",
  "inputs": null,
  "outputs": null,
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": [],
  "dependencies": [],
  "defaults": {"w": 20, "h": 10}
}
</config>

<script lang="javascript">


class ImJoyPlugin {
  async setup() {
    await api.log('initialized')
    window.connect = async function(){
        const ws = await api.connectToServer({
            name: "client-plugin",
            server_url: document.getElementById("server_url").value,
            workspace: document.getElementById("workspace").value,
            token: document.getElementById("token").value,
            server_token: document.getElementById("token").value,
        })
        const plugin = await ws.getPlugin("example_plugin")
        window.execute = function (){
            const result = await plugin.echo(123)
            alert(result)
        }
    }
  }

  async run(ctx) {
    
  }
}

api.export(new ImJoyPlugin())
</script>

<window lang="html">
  <div>
    Server URL: <input id="server_url" value="http://127.0.0.1:8000">
    Workspace: <input id="workspace">
    Token: <input id="token">
    <br>
    <button onclick="connect()">Connect</button>
    <button onclick="execute()">Execute Run</button>
  </div>
</window>

<style lang="css">

</style>

```
