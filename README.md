Welcome to Wit MTN MOMO API Python SDK, here is the full tutorial on how to use it:
Production url https://proxy.momoapi.mtn.com
Sandbox URL https://sandbox.momodeveloper.mtn.com

## Calling request to pay 
```
from pay import PayClass

callPay = PayClass.momopay(1,"ZMW", "The reference", "260968793843", "Payer message")
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
 
 
