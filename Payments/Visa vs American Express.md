# Visa vs. American Express
## What are the differences between VISA and American Express’s (AMEX) processing when you swipe credit cards?
* __VISA__ uses a __4-party model__ where the issuer and acquirer are different entities
* __AMEX__ uses a __3-party model__ where the issuer and acquirer are the same entity.


🔹4-Party Model (Authorization Flow)
* __Step 0__: The card-issuing bank issues a credit card to its customer. 
* __Step 1__: The cardholder buys a product by swiping their credit card at the Point of Sale (POS) terminal in a merchant’s shop.
* __Step 2__: The POS terminal sends the transaction to the acquiring bank, which provides the POS terminal.
* __Steps 3 and 4__: The acquiring bank sends the transaction to the card network, also called the Card Scheme. 
               This card network sends the transaction to the issuing bank for approval.
* __Steps 4.1, 4.2, and 4.3__: The issuing bank freezes the money if the transaction is approved. 
                         The approval or rejection is sent back to the acquirer, and to the POS terminal. 

![image](https://user-images.githubusercontent.com/22426280/230948391-0fee11c5-7754-4b1b-8501-befd5a5f96f2.png)

🔹3-Party Model (Authorization Flow)

* __Steps 0,1 and 2__: are the same as in the 4-party model.
* __Step 3__: 
  1) Since one company performs issuing, acquiring, and card network functions, the transactions are processed internally within 
     the franchisor. This is also called the closed loop card model. 
  2) Closed loop networks are more efficient because all functions are processed in one franchisor. 
  3) However, it doesn’t allow other entities to issue or acquire on its behalf, so it scales more slowly.
  4) In recent years, the closed loop networks have partnered with other issuers and acquirers to scale their circulation.
* __Step 4__: The approval or rejection is sent back to the acquirer, then to the POS terminal. 
