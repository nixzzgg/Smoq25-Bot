import requests
import json
import random
import string
import time
import arrow
import sys
from english_words import get_english_words_set

prefijoUid = 'a_'
sufijoUid = ''.join(random.choices(string.digits, k=18))
uidBot = prefijoUid + sufijoUid
endpoint1 = ''.join(random.choices(string.digits, k=20))
endpoint2 = ''.join(random.choices(string.digits, k=20))
endpoint3 = ''.join(random.choices(string.digits, k=20))
endpoint4 = ''.join(random.choices(string.digits, k=20))

refreshToken = "AMf-vBxCfw3skb-cNVtd2gomnLmBJDu3oaxr6eixgAAA3SeqOlX6wRF9CsF78xV4UoCYfkNa9HyUbLKhdLto_w79hHhUY3QP8R_PKh10-PyfpVAyufh6bHT64008xhf2E6fiBD1QTI6IFpUZ7b1IYAu0iTAMaPyIZ7tnLLzCvOMFPst8VjfoSeNC0MT3jRF_-ZkL0Ln4KEY-rgfZ5FF5UUYX0FFEmUEfIids89kWRQpZ3NAb7L8W6AiXHlh7VMvYDYtZFl3SD-5qrme_z66yVE3nf7Z2fuR3dQoz1h786Z-hnqQq8e-ee64hzuTiKsnMDj65XxeRTR1JO-Loze-Uj6K1BvCclVfXDVAYa-V9bwCCpL2x0kyXM6o4bw1t0FisZnejJzARCNBvXtMsKZu7dWtDqg-DamIvf2TsOsQeNDh7bi59muO7Wjyb_np8v-nqjZfVCNVsL85Z"

def verCambios(url):
    maxReintentos = 30
    retrasoReintento = 1
    
    for _ in range(maxReintentos):
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            idTrade = datos.get('fields', {}).get('matchId', {}).get('stringValue', None)
            uid = datos.get('fields', {}).get('uid', {}).get('stringValue', None)
            if idTrade and uid:
                return idTrade, uid
        elif respuesta.status_code == 404:
            time.sleep(retrasoReintento)
        else:
            return None, None
    return None, None

def obtPalabras():
  palabras = get_english_words_set(['web2'], lower=True)
  
  palabrasFiltradas = [p for p in palabras if 3 <= len(p) <= 10]
  
  if len(palabrasFiltradas) >= 2:
      return random.sample(palabrasFiltradas, 2)

  palabrasRespaldo = [
      "Cyber", "Quantum", "Neo", "Astro", "Tech", "Data", "Echo",
      "Flux", "Hydro", "Meta", "Nova", "Pixel", "Solar", "Ultra",
      "Vector", "Wave", "Cosmic", "Digital", "Neural", "Spark"
  ]
  return random.sample(palabrasRespaldo, 2)


def genNombre():
    palabras = [palabra.capitalize() for palabra in obtPalabras()]

    if random.choice([True, False]):
        palabras.reverse()
    
    agregarNumeros = random.choice([True, False])
    
    if agregarNumeros:
        numeros = ''.join(random.choices(string.digits, k=random.choice([2, 3])))
        nombreAleatorio = palabras[0] + palabras[1] + numeros
    else:
        nombreAleatorio = palabras[0] + palabras[1]

    return nombreAleatorio

nombreBot1 = genNombre()
nombreBot2 = genNombre()

def obtenerWishlist(uiddd, idTrade):
  maxReintentos = 3
  retrasoReintento = 0.5

  for intento in range(maxReintentos):
      url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uiddd}"
      headers = {
          'User-Agent': "okhttp/3.12.13",
          'Connection': "Keep-Alive",
          'Accept-Encoding': "gzip",
          'Authorization': f"Bearer {tokenDeAcceso}",
          'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
          'Content-Type': "application/json; charset=utf-8"
      }
      
      try:
          respuesta = requests.get(url, headers=headers)
          if respuesta.status_code == 200:
              datos = respuesta.json()
              
              if 'documents' in datos:
                  for documento in datos['documents']:
                      if 'fields' in documento and 'wishlist' in documento['fields']:
                          wishlist = documento['fields']['wishlist'].get('arrayValue', {}).get('values', [])
                          if wishlist:
                              idswishlist = [str(item.get("integerValue")) for item in wishlist if "integerValue" in item]
                              if idswishlist:
                                  return idswishlist[:5]
              
              if 'fields' in datos and 'wishlist' in datos['fields']:
                  wishlist = datos['fields']['wishlist'].get('arrayValue', {}).get('values', [])
                  if wishlist:
                      idswishlist = [str(item.get("integerValue")) for item in wishlist if "integerValue" in item]
                      if idswishlist:
                          return idswishlist[:5]
          
          time.sleep(retrasoReintento)
          
      except Exception as e:
          time.sleep(retrasoReintento)
          continue

  wishlistDefecto = ["300157", "300154", "300156", "300153", "300155"]
  return wishlistDefecto

def obtenerTimestamp():
    tiempoActual = arrow.utcnow()
    timestampString = tiempoActual.format("YYYY-MM-DDTHH:mm:ss") + "Z"
    return timestampString

timestampString = obtenerTimestamp()

url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyDbs8XDzjZKSuMew3odWbfP0OoGLQwfhSM"

data = json.dumps({
    "grantType":
    "refresh_token",
    "refreshToken":
    "refresh_token","refreshToken": refreshToken,
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

respuestaInicio = requests.post(url, data=data, headers=headers)

tokenDeAcceso = respuestaInicio.json()["access_token"]

codigo = "" #pongan su codigo de smoq acá

url = "https://europe-west2-smoqgames25-simulation.cloudfunctions.net/addTradeInvitation"

data = json.dumps({
  "data": {
    "code": codigo,
    "uid2": uidBot,
    "badgeId": 240,
    "name": nombreBot1,
    "version": 281
  }
})

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {tokenDeAcceso}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}

respuesta = requests.post(url, data=data, headers=headers)
datosRespuesta = json.loads(respuesta.text)

responseKey = datosRespuesta['result']['responseKey']

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {tokenDeAcceso}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}

urlVerificar = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Invitations/{codigo}/Trades"
respuestaVerificacion = requests.get(urlVerificar, headers=headers)
datosVerificacion = respuestaVerificacion.json()

responseKeyEncontrada = False
if 'documents' in datosVerificacion:
    for doc in datosVerificacion['documents']:
        if 'fields' in doc and 'responseKey' in doc['fields']:
            if doc['fields']['responseKey']['stringValue'] == responseKey:
                responseKeyEncontrada = True
                break
    
if not responseKeyEncontrada:
    print("noEncontrada", file=sys.stderr)
    sys.exit(1)  

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
  'authorization': f"Bearer {tokenDeAcceso}",
  'x-firebase-appcheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
}

respuesta = requests.get(url, headers=headers)

print(respuesta.text)

idTrade, uidUsuario = verCambios(urlRK)

print(idTrade, uidUsuario)

url = "https://europe-west2-smoqgames25-simulation.cloudfunctions.net/sendHelloMessage"

data = json.dumps({
  "data": {
    "badgeId": 240,
    "wishlist": [],
    "name": nombreBot2,
    "opponentUid": uidUsuario,
    "tradeKey": idTrade
  }
})

headers = {
  'User-Agent': "okhttp/3.12.13",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {tokenDeAcceso}",
  'Firebase-Instance-ID-Token': "cN6BK1e-R3W_HFgx51-xk5:APA91bGbxvCN4Q8CAnDVgMfA2VIl_dDVYMsPt_t-n8KRTOHlceHL-Pfmg7WgLKz0yZwceWsy-9XLn3jw5MU16aqMJm2LCmhHLZmJjBGXgkrf-v1A6BNYpRXiD2t4qf2dBmb_FcqzqwUd",
  'Content-Type': "application/json; charset=utf-8"
}

respuesta = requests.post(url, data=data, headers=headers)

print(respuesta.text)

urlVerificar = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidUsuario}"

respuestaVerif = requests.get(urlVerificar, headers=headers)
jsonRespuesta = respuestaVerif.json()

print(jsonRespuesta)

uidPlayer = jsonRespuesta['documents'][0]['fields']['uid']['stringValue']

print(uidPlayer)

wishlist = obtenerWishlist(uidPlayer, idTrade)

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
  'authorization': f"Bearer {tokenDeAcceso}",
  'x-firebase-appcheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
}

url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidUsuario}/{endpoint1}"

data = {
    "fields": {
        "timestamp": {
            "timestampValue": timestampString
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

respuesta = requests.patch(url, json=data, headers=headers)

print(respuesta.text)

url = f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidUsuario}/{endpoint2}"

data = {
    "fields": {
        "timestamp": {
            "timestampValue": timestampString
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

respuesta = requests.patch(url, json=data, headers=headers)

print(respuesta.text)

def actualizarTrade(idTrade, uidUsuario, timestampString, headers):
    respuesta1 = requests.patch(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidUsuario}/{endpoint3}",
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
                    "timestampValue": timestampString
                },
            }
        },
        headers=headers
    )

    respuesta2 = requests.patch(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidUsuario}/{endpoint4}",
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
                    "timestampValue": timestampString
                },
            }
        },
        headers=headers
    )

    return respuesta1.json(), respuesta2.json()

def verCambios2(jsonRespuesta, idTrade, uidUsuario, timestampString, headers):
    for doc in jsonRespuesta.get('documents', []):
        valoresM = doc.get("fields", {}).get("m", {}).get("arrayValue", {}).get("values", [])
        for valor in valoresM:
            if valor.get("integerValue", "") == "76":
                raise ValueError("salir")
            elif valor.get("integerValue", "") == "65":
                return actualizarTrade(idTrade, uidUsuario, timestampString, headers)
    return None

tiempoInicio = time.time() 

while True:
    respuesta = requests.get(
        f"https://firestore.googleapis.com/v1/projects/smoqgames25-simulation/databases/(default)/documents/Trade3/{idTrade}/{uidPlayer}",
        headers=headers,
        stream=True,
    )
    if respuesta.status_code == 200:
        jsonRespuesta = respuesta.json()
        print(jsonRespuesta) 
        resultadoActualizacion = verCambios2(jsonRespuesta, idTrade, uidUsuario, timestampString, headers)

        if resultadoActualizacion:
            break 
    else:
        print("error: ", respuesta.status_code)

    if time.time() - tiempoInicio > 30:
        raise TimeoutError("lentoo")
