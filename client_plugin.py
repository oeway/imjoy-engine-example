"""Provide an example plugin."""
from imjoy_rpc import api, connect_to_server
# pylint: disable=no-self-use


class ImJoyPlugin:
    """Represent an ImJoy plugin."""

    async def setup(self):
        """Set up the plugin."""
        await api.log("initialized")
        ws = await connect_to_server({
            "name": "test-client",
            "server_url": "http://127.0.0.1:8000",
            "workspace": "TdYpVvhKhrfzY5LCTEFMbw", # change me!!!
            "token": "P8xJsThvnVDLqzjZUqJ9u3@imjoy@eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2ltam95LmlvLyIsInN1YiI6IlRkWXBWdmhLaHJmelk1TENURUZNYncvUDh4SnNUaHZuVkRMcXpqWlVxSjl1MyIsImF1ZCI6Imh0dHBzOi8vaW1qb3kuZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjEwODAwLCJleHAiOjE2MzQzMjE5MjUuODk0NDkyOSwic2NvcGUiOiJUZFlwVnZoS2hyZnpZNUxDVEVGTWJ3IiwicGFyZW50IjoiVGRZcFZ2aEtocmZ6WTVMQ1RFRk1idyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImh0dHBzOi8vYXBpLmltam95LmlvL3JvbGVzIjpbXSwiaHR0cHM6Ly9hcGkuaW1qb3kuaW8vZW1haWwiOm51bGx9.vAbBc0s_QIQdxO-Lt6W9E2YCV0IKf7Sx7uPycVH0bQI"
        })
        await ws.log("connected!!!!")
        plugin = await ws.getPlugin("example_plugin")
        result = await plugin.echo(123)
        print("Echo result: ", result)

api.export(ImJoyPlugin(), config={"name": "client-plugin"})