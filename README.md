Welcome to Wit MTN MOMO API Python SDK, here is the full tutorial on how to use it:
Production url https://proxy.momoapi.mtn.com
Sandbox URL https://sandbox.momodeveloper.mtn.com

#Requirements for production users 
  - MTN MOMO DEVELOPER ACCOUNT(https://momodeveloper.mtn.com/signin?ReturnUrl=%2F)
  - MTN MOMO COLLECTIONS SUBSCRIPTION KEY
  - MTN MOMO DEVELOPER DISBURSEMENT SUBSCRIPTION KEY
# Requirements For Sandbox/Testing users
  - Basic authorizatio, which is generated with API user and API key
  


## Calling request to pay 
```
from pay import PayClass

callPay = PayClass.momopay(amount, currency, txt_ref, phone_number, payermessage)
print(callPay["response"])
```
To return the reference(UUID), print out this: 
```
print(callPay["ref"]) 
```
And to return the status code print out this:
```
print(callPay["response"])
```
Note: If it returns 202 or 200 then it means the request was successful

## Verify and check the transaction status
 Checking the transaction status is used to verify if the customer has confirmed the payment or not. Here is the calling for transaction status and verification check.
 ```
 from pay import PayClass

#Verify the transaction
verify = PayClass.verifymomo("Reference returned by momopay function")
 ```
Status 200 or 202 means okay
When the transaction is successful it returns:
 ```
{
  "amount": 100,
  "currency": "UGX",
  "financialTransactionId": 23503452,
  "externalId": 947354,
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": 4656473839.0
  },
  "status": "SUCCESSFUL"
}
 ```
 For the complete reference of payment verification read on the bottom page from this link"
 https://momodeveloper.mtn.com/docs/services/collection/operations/requesttopay-referenceId-GET?
 
 ## Checking the account balance from the collections account
 This function is used to check the account balance for the money inside the collections wallet account. Here is how the API call is done:
  ```
from pay import PayClass
#Checking the collections balance
checkcollectionsbalance = PayClass.momobalance()
  ```
  If the status is 200 or 202 it means the call was successful. After the call above it returns the account balance
  
## Checking the account balance from the disbursement account
  This function is used to check the account balance for the money inside the Disbursement wallet account. Here is how the API call is done:
  ```
  #Checking the disbursment balance
  disbursementBalanceCheck = PayClass.momobalancedisbursement()
  ```
   If the status is 200 or 202 it means the call was successful. After the call above it returns the account balance
   
## Transfer money from MTN Disbursement wallet to an MTN mobile money account
This function is used to transfer money from MTN disbursement account to an MTN mobile money account. Here is how it is done:

 ```
from pay import PayClass
#Transfer money from disbursement account
withdrawmoney = PayClass.withdrawmtnmomo(amount, currency, txt_ref, phone_number, payermessage)

  ```
  After a successful transfer it either returns 202 or 200
  Note: To check the status print this 
   ```
  print(withdrawmoney["response"])
  ```
  To Check the transaction UUID(Reference)
  Print this:
  ```
  print(withdrawmoney["ref"])
  ```
  
    Note: The call withdrawmoney["ref"] returns a unique UUID(reference) which we will use in the next part

## Checking withdraw status
 This function is used to check the withdraw status after calling a withdraw function. Here is the code:
 ```
 from pay import PayClass
 CheckWithdrawStatus = PayClass.checkwithdrawstatus("UUID reference returned from the transfer")
 ```
  
  
# REFERENCES
MTN DEVELOPER, (2019). /Token - Post. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/collection/operations/token-POST?, [ACCESSED: 7 july, 2022]

MTN DEVELOPER, (2019). Request to pay. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/collection/operations/requesttopay-POST?, [ACCESSED: 7 july, 2022] 

MTN DEVELOPER, (2019). /requesttopay/{referenceId} - GET. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/collection/operations/requesttopay-referenceId-GET?, [ACCESSED: 7 july, 2022] 

MTN DEVELOPER, (2019). /v1_0/account/balance - GET. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/collection/operations/get-v1_0-account-balance?, [ACCESSED: 7 july, 2022] 

MTN DEVELOPER, (2019). Disbursement token. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/disbursement/operations/token-POST?, [ACCESSED: 7 july, 2022]

MTN DEVELOPER, (2019). /transfer - POST. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/disbursement/operations/transfer-POST?, [ACCESSED: 7 july, 2022]

MTN DEVELOPER, (2019). /transfer/{referenceId} - GET. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/disbursement/operations/transfer-referenceId-GET?, [ACCESSED: 7 july, 2022]

MTN DEVELOPER, (2019). /v1_0/account/balance - GET. MOMO DEVELOPER PORTAL, Available: https://momodeveloper.mtn.com/docs/services/disbursement/operations/get-v1_0-account-balance?, [ACCESSED: 7 july, 2022]










 
