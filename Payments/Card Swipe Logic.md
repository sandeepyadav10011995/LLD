# How does VISA work when we swipe a credit card at a merchant’s shop?
* __VISA, Mastercard, and American Express__ act as card networks for clearing and settling funds. 
* The card acquiring bank and the card issuing bank can be – and often are – different. 
* If banks were to settle transactions one by one without an intermediary, each bank would have to settle the transactions 
  with all the other banks ==> __This is quite inefficient__
  
#### There are two flows involved. 
##### In the process, the card network takes on the burden of talking to each bank and receives service fees in return.
* __Authorization flow__ happens when the customer swipes the credit card.
  * __Step 0__: The card issuing bank issues credit cards to its customers. 
  * __Step 1__: The cardholder wants to buy a product and swipes the credit card at the Point of Sale (POS) terminal in the merchant’s shop.
  * __Step 2__: The POS terminal sends the transaction to the acquiring bank, which has provided the POS terminal.
  * __Steps 3 and 4__: The acquiring bank sends the transaction to the card network, also called the card scheme. 
                       The card network sends the transaction to the issuing bank for approval.
  * __Steps 4.1, 4.2, and 4.3__: The issuing bank freezes the money if the transaction is approved. 
                                 The approval or rejection is sent back to the acquirer, as well as the POS terminal. 

![image](https://user-images.githubusercontent.com/22426280/230952170-fbd2c5c3-59ca-4826-b109-232dfb5a3335.png)

* __Capture and settlement flow__ occurs when the merchant wants to get the money at the end of the day.
  * __Steps 1 and 2__: The merchant wants to collect the money at the end of the day, so they hit ”capture” on the POS terminal. 
                       The transactions are sent to the acquirer in batches. 
                       The acquirer sends the batch file with transactions to the card network.
  * __Step 3__: The card network performs clearing for the transactions collected from different acquirers, and sends the clearing 
                files to different issuing banks.
  * __Step 4__: The issuing banks confirm the correctness of the clearing files, and transfer money to the relevant acquiring banks.
  * __Step 5__: The acquiring bank then transfers money to the merchant’s bank. 
  * __Step 6__: The card network clears the transactions from different acquiring banks. 
                Clearing is a process in which mutual offset transactions are netted, so the number of total transactions is reduced.
