import json
import requests

ab_url = "http://localhost:8001/api/v1"
headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Basic YWlyYnl0ZTpwYXNzd29yZA=="}
workspace_id = requests.post(f"{ab_url}/workspaces/list", headers=headers).json().get("workspaces")[0].get("workspaceId")
print(f"{workspace_id=}")

payload = json.dumps({"workspaceId": workspace_id})
print(f"{payload=}")

connections = requests.post(f"{ab_url}/connections/list", headers=headers, data=payload).json().get("connections")
connection_id = ""

for c in connections:
    if c.get("name") == "demo_connection":
        connection_id = c.get("connectionId")
        break

print(f"{connection_id=}")
