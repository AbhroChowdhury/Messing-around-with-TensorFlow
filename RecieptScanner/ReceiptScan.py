import requests as rq    # pip3 install requests
import json
import pickle

url = "https://ocr.asprise.com/api/v1/receipt"
receipt = "figure1.jpg"

res = rq.post(url, 
                data = {'api_key': 'TEST', 'recognizer': 'auto', 'ref_no': 'oct_python_123'},
                files = {'file': open(receipt, 'rb')})

json.dumps(json.loads(res.text))