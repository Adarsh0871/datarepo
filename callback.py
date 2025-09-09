import requests, json, sys

callback_url = sys.argv[1] if len(sys.argv) > 1 else ""
status = sys.argv[2] if len(sys.argv) > 2 else "success"

payload = {
    "request_id": sys.argv[3] if len(sys.argv) > 3 else "REQ0012345",
    "status": status
}

if callback_url:
    print("Posting to:", callback_url)
    try:
        resp = requests.post(
            callback_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            auth=("Admin", "U%B7QwtuQz1-")   # Replace with Azure DevOps secrets
        )
        print("Response:", resp.status_code, resp.text)
    except Exception as e:
        print("Callback failed:", str(e))
else:
    print("No callback URL provided.")
