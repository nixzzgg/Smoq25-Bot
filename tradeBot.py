import requests
import json
import random
import string
import time
import arrow
import sys
from english_words import get_english_words_set

prefix = 'a_'
random_suffix = ''.join(random.choices(string.digits, k=18))
uidBot = prefix + random_suffix
lol1 = ''.join(random.choices(string.digits, k=20))
lol2 = ''.join(random.choices(string.digits, k=20))
lol3 = ''.join(random.choices(string.digits, k=20))
lol4 = ''.join(random.choices(string.digits, k=20))
lol5 = ''.join(random.choices(string.digits, k=20))
lol6 = ''.join(random.choices(string.digits, k=20))

refresh_token = "AMf-vBxCfw3skb-cNVtd2gomnLmBJDu3oaxr6eixgAAA3SeqOlX6wRF9CsF78xV4UoCYfkNa9HyUbLKhdLto_w79hHhUY3QP8R_PKh10-PyfpVAyufh6bHT64008xhf2E6fiBD1QTI6IFpUZ7b1IYAu0iTAMaPyIZ7tnLLzCvOMFPst8VjfoSeNC0MT3jRF_-ZkL0Ln4KEY-rgfZ5FF5UUYX0FFEmUEfIids89kWRQpZ3NAb7L8W6AiXHlh7VMvYDYtZFl3SD-5qrme_z66yVE3nf7Z2fuR3dQoz1h786Z-hnqQq8e-ee64hzuTiKsnMDj65XxeRTR1JO-Loze-Uj6K1BvCclVfXDVAYa-V9bwCCpL2x0kyXM6o4bw1t0FisZnejJzARCNBvXtMsKZu7dWtDqg-DamIvf2TsOsQeNDh7bi59muO7Wjyb_np8v-nqjZfVCNVsL85Z"

def verCambios(url):
    max_retries = 30
    retry_delay = 1
    
    for _ in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            match_id = data.get('fields', {}).get('matchId', {}).get('stringValue', None)
            uid = data.get('fields', {}).get('uid', {}).get('stringValue', None)
            if match_id and uid:
                return match_id, uid
        elif response.status_code == 404:
            time.sleep(retry_delay)
        else:
            return None, None
    return None, None


def ObtPalabras():
  palabras = get_english_words_set(['web2'], lower=True)
  
  palabras_filtradas = [p for p in palabras if 3 <= len(p) <= 10]
  
  if len(palabras_filtradas) >= 2:
      return random.sample(palabras_filtradas, 2)

  palabras_respaldo = [
      "Cyber", "Quantum", "Neo", "Astro", "Tech", "Data", "Echo",
      "Flux", "Hydro", "Meta", "Nova", "Pixel", "Solar", "Ultra",
      "Vector", "Wave", "Cosmic", "Digital", "Neural", "Spark"
  ]
  return random.sample(palabras_respaldo, 2)


def genNombre():
    palabras = [palabra.capitalize() for palabra in ObtPalabras()]

    if random.choice([True, False]):
        palabras.reverse()
    
    agregar_numeros = random.choice([True, False])
    
    if agregar_numeros:
        numeros = ''.join(random.choices(string.digits, k=random.choice([2, 3])))
        nombre_aleatorio = palabras[0] + palabras[1] + numeros
    else:
        nombre_aleatorio = palabras[0] + palabras[1]

    return nombre_aleatorio

nameBot1 = genNombre()
nameBot2 = genNombre()

def obtenerWishlist(uiddd, match_id):
  max_retries = 3
  retry_delay = 0.5

  for attempt in range(max_retries):
      url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{uiddd}"
      headers = {
          'User-Agent': "okhttp/3.12.13",
          'Connection': "Keep-Alive",
          'Accept-Encoding': "gzip",
          'Authorization': f"Bearer {accessToken}",
          'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
          'Content-Type': "application/json; charset=utf-8"
      }
      
      try:
          response = requests.get(url, headers=headers)
          if response.status_code == 200:
              data = response.json()
              
              if 'documents' in data:
                  for document in data['documents']:
                      if 'fields' in document and 'wishlist' in document['fields']:
                          wishlist = document['fields']['wishlist'].get('arrayValue', {}).get('values', [])
                          if wishlist:
                              wishlist_ids = [str(item.get("integerValue")) for item in wishlist if "integerValue" in item]
                              if wishlist_ids:
                                  return wishlist_ids[:5]
              
              if 'fields' in data and 'wishlist' in data['fields']:
                  wishlist = data['fields']['wishlist'].get('arrayValue', {}).get('values', [])
                  if wishlist:
                      wishlist_ids = [str(item.get("integerValue")) for item in wishlist if "integerValue" in item]
                      if wishlist_ids:
                          return wishlist_ids[:5]
          
          time.sleep(retry_delay)
          
      except Exception as e:
          time.sleep(retry_delay)
          continue

  default_wishlist = ["300157", "300154", "300156", "300153", "300155"]
  return default_wishlist


def obtenerTimestamp():
    current_time = arrow.utcnow()
    timestamp_string = current_time.format("YYYY-MM-DDTHH:mm:ss") + "Z"
    return timestamp_string

timestamp_string = obtenerTimestamp()

##########################################################


url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyDbs8XDzjZKSuMew3odWbfP0OoGLQwfhSM"

payload = json.dumps({
    "grantType":
    "refresh_token",
    "refreshToken":
    "refresh_token","refreshToken": refresh_token,
})

headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 14; SM-A536E Build/UP1A.231005.007)",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'X-Android-Package': "com.smoqgames.smoq25",
  'X-Android-Cert': "025C3A3B097F556CA63D5334D3D790B0F9F87FB2",
  'Accept-Language': "es-US, en-US",
  'X-Client-Version': "Android/Fallback/X23000000/FirebaseCore-Android",
  'X-Firebase-GMPID': "1:121033544792:android:9e5665e285d3f548a4a62d",
  'X-Firebase-Client': "H4sIAAAAAAAA_6tWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
  'X-Firebase-AppCheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
}

responseStart = requests.post(url, data=payload, headers=headers)

accessToken = responseStart.json()["access_token"]

code = "NXDH86"

url = "https://europe-west2-smoqgames25-simulation.cloudfunctions.net/addTradeInvitation"

payload = json.dumps({
  "data": {
    "code": code,
    "uid2": uidBot,
    "badgeId": 240,
    "name": nameBot1,
    "version": 281
  }
})

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {accessToken}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}


response = requests.post(url, data=payload, headers=headers)
response_data = json.loads(response.text)


responseKey = response_data['result']['responseKey']

##########################################################

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {accessToken}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}

urlCheck = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Invitations/{code}/Trades"
checkResponse = requests.get(urlCheck, headers=headers)
checkData = checkResponse.json()

responseKey_found = False
if 'documents' in checkData:
    for doc in checkData['documents']:
        if 'fields' in doc and 'responseKey' in doc['fields']:
            if doc['fields']['responseKey']['stringValue'] == responseKey:
                responseKey_found = True
                break
    
if not responseKey_found:
    print("notFound", file=sys.stderr)
    sys.exit(1)  

##########################################################

urlRK = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/TResp3/{responseKey}"

headers = {
  'User-Agent': "grpc-java-okhttp/1.57.2",
  'content-type': "application/grpc",
  'te': "trailers",
  'x-goog-api-client': "gl-java/ fire/25.0.0 grpc/",
  'google-cloud-resource-prefix': "projects/smoqgames25-simulation/databases/(default)",
  'x-goog-request-params': "projects/smoqgames25-simulation/databases/(default)",
  'x-firebase-client': "fire-cls/19.0.3 device-model/a53x fire-installations/18.0.0 kotlin/1.8.22 fire-gcs/21.0.0 fire-app-check/18.0.0 device-brand/samsung fire-core/21.0.0 fire-core-ktx/21.0.0 android-platform/ fire-sessions/2.0.3 fire-transport/19.0.0 android-target-sdk/34 fire-auth/23.0.0 android-min-sdk/23 fire-rtdb/21.0.0 fire-fn/21.0.0 fire-android/34 android-installer/com.android.vending fire-iid/21.1.0 fire-analytics/22.0.2 fire-fst/25.0.0 device-name/a53xnsxx fire-fcm/24.0.0",
  'x-firebase-gmpid': "1:121033544792:android:9e5665e285d3f548a4a62d",
  'grpc-accept-encoding': "gzip",
  'authorization': f"Bearer {accessToken}",
  'x-firebase-appcheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
}

response = requests.get(url, headers=headers)

print(response.text)

match_id, userUidd = verCambios(urlRK)

print(match_id, userUidd)

url = "https://europe-west2-smoqgames25-simulation.cloudfunctions.net/sendHelloMessage"

payload = json.dumps({
  "data": {
    "badgeId": 240,
    "wishlist": [],
    "name": nameBot2,
    "opponentUid": userUidd,
    "tradeKey": match_id
  }
})

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {accessToken}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)

url_verify = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{userUidd}"

responseee = requests.get(url_verify, headers=headers)
response_json = responseee.json()

print(response_json)

uiddd2 = response_json['documents'][0]['fields']['uid']['stringValue']

print(uiddd2)

wishlist = obtenerWishlist(uiddd2, match_id)

if wishlist:

    if len(wishlist) > 1:
        wishlist = wishlist[:5]

    if len(wishlist) > 2:
        wishlist = wishlist[:5]

    if len(wishlist) > 3:
        wishlist = wishlist[:5]         

    if len(wishlist) == 1:
        wishlist *= 5

    if len(wishlist) == 2:
        wishlist *= 3


    if len(wishlist) == 3:
        wishlist *= 2

    if len(wishlist) > 4:
        wishlist = wishlist[:5]

    if len(wishlist) == 4:
        wishlist *= 2

print(wishlist)

headers = {
  'User-Agent': "grpc-java-okhttp/1.57.2",
  'content-type': "application/grpc",
  'te': "trailers",
  'x-goog-api-client': "gl-java/ fire/25.0.0 grpc/",
  'google-cloud-resource-prefix': "projects/smoqgames25-simulation/databases/(default)",
  'x-goog-request-params': "projects/smoqgames25-simulation/databases/(default)",
  'x-firebase-client': "fire-cls/19.0.3 device-model/a53x fire-installations/18.0.0 kotlin/1.8.22 fire-gcs/21.0.0 fire-app-check/18.0.0 device-brand/samsung fire-core/21.0.0 fire-core-ktx/21.0.0 android-platform/ fire-sessions/2.0.3 fire-transport/19.0.0 android-target-sdk/34 fire-auth/23.0.0 android-min-sdk/23 fire-rtdb/21.0.0 fire-fn/21.0.0 fire-android/34 android-installer/com.android.vending fire-iid/21.1.0 fire-analytics/22.0.2 fire-fst/25.0.0 device-name/a53xnsxx fire-fcm/24.0.0",
  'x-firebase-gmpid': "1:121033544792:android:9e5665e285d3f548a4a62d",
  'grpc-accept-encoding': "gzip",
  'authorization': f"Bearer {accessToken}",
  'x-firebase-appcheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
}

url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{userUidd}/{lol2}"

payload = {
    "fields": {
        "timestamp": {
            "timestampValue": timestamp_string
        },
        "m": {
            "arrayValue": {
                "values": [
                    {"integerValue": "88"},
                    {"integerValue": "0"},
                    {"integerValue": "100000"},
                    {"integerValue": "0"},
                    {"integerValue": wishlist[0] if wishlist else "319410"},
                    {"integerValue": "2"},
                    {"integerValue": wishlist[1] if wishlist else "320587"},
                    {"integerValue": "4"},
                    {"integerValue": wishlist[2] if wishlist else "319413"},
                    {"integerValue": "5"},
                    {"integerValue": wishlist[3] if wishlist else "319278"},
                    {"integerValue": "3"},
                    {"integerValue": wishlist[4] if wishlist else "319534"},
                    {"integerValue": "1"}
                ]
            }
        }
    }
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)

url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{userUidd}/{lol3}"

payload = {
    "fields": {
        "timestamp": {
            "timestampValue": timestamp_string
        },
        "m": {
            "arrayValue": {
                "values": [
                    {"integerValue": "80"},
                    {"integerValue": "0"},
                    {"integerValue": "100000"},
                    {"integerValue": "0"},
                    {"integerValue": wishlist[0] if wishlist else "300157"},
                    {"integerValue": "2"},
                    {"integerValue": wishlist[1] if wishlist else "300154"},
                    {"integerValue": "4"},
                    {"integerValue": wishlist[2] if wishlist else "300156"},
                    {"integerValue": "5"},
                    {"integerValue": wishlist[3] if wishlist else "300153"},
                    {"integerValue": "3"},
                    {"integerValue": wishlist[4] if wishlist else "300155"},
                    {"integerValue": "1"}
                ]
            }
        }
    }
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)

def updateTrade(match_id, userUidd, timestamp_string, headers):
    response1 = requests.patch(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{userUidd}/{lol4}",
        json={
            "fields": {
                "m": {
                    "arrayValue": {
                        "values": [
                            {
                                "integerValue": "65"
                            },
                            {
                                "integerValue": "0"
                            },
                            {
                                "integerValue": "0"
                            },
                            {
                                "integerValue": "0"
                            },
                        ]
                    }
                },
                "timestamp": {
                    "timestampValue": timestamp_string
                },
            }
        },
        headers=headers
    )

    response2 = requests.patch(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{userUidd}/{lol5}",
        json={
            "fields": {
                "m": {
                    "arrayValue": {
                        "values": [
                            {
                                "integerValue": "67"
                            },
                            {
                                "integerValue": "0"
                            },
                            {
                                "integerValue": "0"
                            },
                            {
                                "integerValue": "0"
                            },
                        ]
                    }
                },
                "timestamp": {
                    "timestampValue": timestamp_string
                },
            }
        },
        headers=headers
    )

    return response1.json(), response2.json()

def verCambios2(response_json, match_id, userUidd, timestamp_string, headers):
    for doc in response_json.get('documents', []):
        m_values = doc.get("fields", {}).get("m", {}).get("arrayValue", {}).get("values", [])
        for value in m_values:
            if value.get("integerValue", "") == "76":
                raise ValueError("exit")
            elif value.get("integerValue", "") == "65":
                return updateTrade(match_id, userUidd, timestamp_string, headers)
    return None

start_time = time.time() 

while True:
    response = requests.get(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{match_id}/{uiddd2}",
        headers=headers,
        stream=True,
    )
    if response.status_code == 200:
        response_json = response.json()
        print(response_json) 
        update_result = verCambios2(response_json, match_id, userUidd, timestamp_string, headers)

        if update_result:
            break 
    else:
        print("error: ", response.status_code)

    if time.time() - start_time > 30:
        raise TimeoutError("lentoo")
