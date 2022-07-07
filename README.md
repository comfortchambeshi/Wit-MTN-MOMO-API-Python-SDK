Welcome to Wit MTN MOMO API Python SDK, here is the full tutorial on how to use it:
Production url https://proxy.momoapi.mtn.com
Sandbox URL https://sandbox.momodeveloper.mtn.com

## Calling request to pay 
```
from pay import PayClass

callPay = PayClass.momopay(1,"ZMW", "The reference", "260968793843", "Payer message")
print(callPay["response"])
```
