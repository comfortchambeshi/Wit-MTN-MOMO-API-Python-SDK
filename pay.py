
import requests
import json
import uuid

#Momo token generation
def  momotoken():
   url = "https://sandbox.momodeveloper.mtn.com/collection/token/"

   payload={}
   headers = {
     'Ocp-Apim-Subscription-Key': 'Your MTN MOMO SUBSCRIPTION KEY',
     'Authorization': 'Basic _Your basic authorization_'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   authorization_token = response.json()
   return authorization_token

#Momo disbursement token generation
def  momotokendisbursement():
   url = "https://sandbox.momodeveloper.mtn.com/disbursement/token/"

   payload={}
   headers = {
     'Ocp-Apim-Subscription-Key': 'Your MTN MOMO DISBURSEMENT SUBSCRIPTION KEY',
     'Authorization': 'Basic _Disbursement_basic_key_'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   authorization_token = response.json()
   return authorization_token


class PayClass():


    def momopay(amount, currency, txt_ref, phone_number, payermessage):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"

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
  'X-Target-Environment': 'sandbox',
  'Ocp-Apim-Subscription-Key': 'Your MTN MOMO COLLECTIONS SUBSCRIPTION KEY',
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(momotoken()["access_token"])
}

        response = requests.request("POST", url, headers=headers, data=payload)

        context = {"response":response.status_code, "ref":uuidgen}
       
        return context

    def verifymomo(txn):
       url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/"+str(txn)+""

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': 'Your MTN MOMO COLLECTIONS SUBSCRIPTION KEY',
         'Authorization':  "Bearer "+str(momotoken()["access_token"]),
           'X-Target-Environment': 'sandbox',
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon

    #Check momo collections balance
    def momobalance():
       url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/account/balance"

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': 'Your MTN MOMO SUBSCRIPTION KEY',
         'Authorization':  "Bearer "+str(momotoken()["access_token"]),
           'X-Target-Environment': 'sandbox',
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon 
    
    #Check Disubursement balance
    def momobalancedisbursement():
       url = "https://sandbox.momodeveloper.mtn.com/disbursement/v1_0/account/balance"

       payload={}
       headers = {
         'Ocp-Apim-Subscription-Key': 'Your MTN MOMO DISBURSEMENT SUBSCRIPTION KEY',
         'Authorization':  "Bearer "+str(momotokendisbursement()["access_token"]),
           'X-Target-Environment': 'sandbox',
       }

       response = requests.request("GET", url, headers=headers, data=payload)

       json_respon = response.json()

       return json_respon   


  #Withdraw money Disbursement
    def withdrawmtnmomo(amount, currency, txt_ref, phone_number, payermessage):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = "https://sandbox.momodeveloper.mtn.com/disbursement/v1_0/transfer"

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
  'X-Target-Environment': 'sandbox',
  'Ocp-Apim-Subscription-Key': 'Your MTN MOMO DISBURSEMENT SUBSCRIPTION KEY',
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(momotokendisbursement()["access_token"])
}

        response = requests.request("POST", url, headers=headers, data=payload)

        context = {"response":response.status_code, "ref":uuidgen}
     
        return context        

#Check transfer status disbursment
    def checkwithdrawstatus(txt_ref):
        #UUID V4 generator
        uuidgen = str(uuid.uuid4())
        url = "https://sandbox.momodeveloper.mtn.com/disbursement/v1_0/transfer/"+str(txt_ref)+""

        payload = json.dumps({
           
        })

  
        headers = {
  'X-Reference-Id': uuidgen,
  'X-Target-Environment': 'sandbox',
  'Ocp-Apim-Subscription-Key': 'Your MTN MOMO DISBURSEMENT SUBSCRIPTION KEY',
  'Content-Type': 'application/json',
  'Authorization': "Bearer "+str(momotokendisbursement()["access_token"])
}

        response = requests.request("GET", url, headers=headers, data=payload)
        returneddata = response.json()
        context = {"response":response.status_code, "ref":txt_ref, "data":returneddata}
     
        return context





