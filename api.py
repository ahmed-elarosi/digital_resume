import requests

reqUrl = "https://apply.caplena.com/api-guru"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "text/plain"
}

payload = "The Internet? We are not interested in it."

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)