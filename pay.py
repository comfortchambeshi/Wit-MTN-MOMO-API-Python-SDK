
import requests
import json
import uuid
from basicauth import encode





class PayClass():
    #Keys
    #Collections Subscription Key:
    collections_subkey = "{{Collections_subscription_key}}"
    #Disbursement subscription key
    disbursment_subkey = ""
    #Production collections basic authorisation key(Leave it blank if in sandbox mode)
    basic_authorisation_collections = ""
    #Production disbursement basic authorisation key(Leave it blank if in sandbox mode)
    basic_authorisation_disbursment = ""
    
    #API user and Key(Note: Only use this when in production mode)
    collections_apiuser = ""
    api_key_collections = ""

    #Application mode
    environment_mode = "sandbox"
    accurl = "https://proxy.momoapi.mtn.com"
    if environment_mode == "sandbox":
        accurl = "https://sandbox.momodeveloper.mtn.com"
    
    #Generate Basic authorization key when it test mode
    if environment_mode == "sandbox":
      collections_apiuser = str(uuid.uuid4())
      
    #Create API user
    url = ""+str(accurl)+"/v1_0/apiuser"

    payload = json.dumps({
      "providerCallbackHost": "URL of host ie google.com"
    })
    headers = {
      'X-Reference-Id': collections_apiuser,
      'Content-Type': 'application/json',
      'Ocp-Apim-Subscription-Key': collections_subkey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
      
    #Create API key
    url = ""+str(accurl)+"/v1_0/apiuser/"+str(collections_apiuser)+"/apikey"

    payload={}
    headers = {
      'Ocp-Apim-Subscription-Key': collections_subkey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #print("The response is: \n"+str(response))
    response = response.json()
    #Auto generate when in test mode
    if environment_mode == "sandbox":
      api_key_collections = str(response["apiKey"])

    #Create basic key for Collections
    username, password = collections_apiuser, api_key_collections
    basic_authorisation_collections = encoded_str = str(encode(username, password))
    #print(basic_authorisation_collections)

    #API User
    #print("Api user:"+collections_apiuser+"\n")
    #print("Api Key:"+api_key_collections)


    #Momo token generation
    def  momotoken():
          url = ""+str(PayClass.accurl)+"/collection/token/"

          payload={}
          headers = {
            'Ocp-Apim-Subscription-Key': PayClass.collections_subkey,
            'Authorization': str(PayClass.basic_authorisation_collections)
          }

          response = requests.request("POST", url, headers=headers, data=payload)

          authorization_token = response.json()
          return authorization_token

    #Momo disbursement token generation
    def  momotokendisbursement():
          url = ""+str(PayClass.accurl)+"/disbursement/token/"

          payload={}
          headers = {
            'Ocp-Apim-Subscription-Key': PayClass.disbursment_subkey,
            'Authorization': 'Basic '+str(PayClass.basic_authorisation_disbursment)+''
          }

          response = requests.request("POST", url, headers=headers, data=payload)

          authorization_token = response.json()
          return authorization_token      

    def momopay(amount, currency, txt_ref, phone_number, payermessage):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = ""+str(PayClass.accurl)+"/collection/v1_0/requesttopay"

        payload = json.dumps({
          "amount": amount,
          "currency": currency,
          "externalId": txt_ref,
          "payer": {
            "partyIdType": "MSISDN",
            "partyId": phone_number
          },
          "payerMessage": payermessage,
          "payeeNote": payermessage
        })
        headers = {
  'X-Reference-Id': uuidgen,
  'X-Target-Environment': PayClass.environment_mode,
  'Ocp-Apim-Subscription-Key': PayClass.collections_subkey,
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(PayClass.momotoken()["access_token"])
}

        response = requests.request("POST", url, headers=headers, data=payload)

        context = {"response":response.status_code, "ref":uuidgen}
       
        return context

    def verifymomo(txn):
       url = ""+str(PayClass.accurl)+"/collection/v1_0/requesttopay/"+str(txn)+""

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': PayClass.collections_subkey,
         'Authorization':  "Bearer "+str(PayClass.momotoken()["access_token"]),
           'X-Target-Environment': PayClass.environment_mode,
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon

    #Check momo collections balance
    def momobalance():
       url = ""+str(PayClass.accurl)+"/collection/v1_0/account/balance"

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': PayClass.collections_subkey,
         'Authorization':  "Bearer "+str(PayClass.momotoken()["access_token"]),
           'X-Target-Environment': PayClass.environment_mode,
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon 
    
    #Check Disubursement balance
    def momobalancedisbursement():
       url = ""+str(PayClass.accurl)+"/disbursement/v1_0/account/balance"

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': PayClass.momobalancedisbursement,
         'Authorization':  "Bearer "+str(PayClass.momotokendisbursement()["access_token"]),
           'X-Target-Environment': PayClass.environment_mode,
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon   


  #Withdraw money Disbursement
    def withdrawmtnmomo(amount, currency, txt_ref, phone_number, payermessage):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = ""+str(PayClass.accurl)+"/disbursement/v1_0/transfer"

        payload = json.dumps({
            "amount": amount,
            "currency": currency,
            "externalId": txt_ref,
            "payee": {
              "partyIdType": "MSISDN",
              "partyId": phone_number
            },
            "payerMessage": payermessage,
            "payeeNote": payermessage
        })

  
        headers = {
  'X-Reference-Id': uuidgen,
  'X-Target-Environment': PayClass.environment_mode,
  'Ocp-Apim-Subscription-Key': PayClass.disbursment_subkey,
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(PayClass.momotokendisbursement()["access_token"])
}

        response = requests.request("POST", url, headers=headers, data=payload)

        context = {"response":response.status_code, "ref":uuidgen}
     
        return context        

#Check transfer status disbursment
    def checkwithdrawstatus(txt_ref):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = ""+str(PayClass.accurl)+"/disbursement/v1_0/transfer/"+str(txt_ref)+""

        payload = json.dumps({
           
        })

  
        headers = {
  'X-Reference-Id': uuidgen,
  'X-Target-Environment': PayClass.environment_mode,
  'Ocp-Apim-Subscription-Key': PayClass.disbursment_subkey,
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(PayClass.momotokendisbursement()["access_token"])
}

        response = requests.request("GET", url, headers=headers, data=payload)
        returneddata = response.json()
        context = {"response":response.status_code, "ref":txt_ref, "data":returneddata}
     
        return context





