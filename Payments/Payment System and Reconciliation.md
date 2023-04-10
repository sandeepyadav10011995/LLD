# Payment System
#### Here is how money moves when you click the Buy button on Amazon or any of your favorite shopping websites. 
### Steps-:
1. When a user clicks the “Buy” button, a payment event is generated and sent to the payment service.
2. The payment service stores the payment event in the database.
3. Sometimes a single payment event may contain several payment orders. For example, you may select products from multiple sellers 
   in a single checkout process. The payment service will call the payment executor for each payment order.
4. The payment executor stores the payment order in the database.
5. The payment executor calls an external PSP to finish the credit card payment.
6. After the payment executor has successfully executed the payment, the payment service will update the wallet to record how much 
   money a given seller has.

![image](https://user-images.githubusercontent.com/22426280/230942017-6a11eee7-25de-49f9-8362-aba28f72aee4.png)

7. The wallet server stores the updated balance information in the database.
8. After the wallet service has successfully updated the seller’s balance information, the payment service will call the ledger to 
   update it.
9. The ledger service appends the new ledger information to the database.
10. Every night the PSP or banks send settlement files to their clients. The settlement file contains the balance of the bank 
    account, together with all the transactions that took place on this bank account during the day.

# Payment Reconciliation
#### Reconciliation might be the most painful process in a payment system. It is the process of comparing records in different systems to make sure the amounts match each other.

### For example, if you pay $200 to buy a watch with Paypal: 
- The eCommerce website should have a record of the $200 purchase order.
- There should be a transaction record of $200 in Paypal (marked with 2 in the diagram).
- The Ledger should record a debit of $200 dollars for the buyer, and a credit of $200 for the seller. 
  This is called double-entry bookkeeping (see the table below).

![image](https://user-images.githubusercontent.com/22426280/230944670-840e1259-9ea8-42ef-a4b2-934bbc59b151.png)

### Let’s take a look at some pain points and how we can address them: 

__Problem 1__: Data normalization. When comparing records in different systems, they come in different formats. For example, the timestamp can be “2022/01/01” in one system and “Jan 1, 2022” in another.

__Possible solution__: we can add a layer to transform different formats into the same format.

__Problem 2__: Massive data volume

__Possible solution__: we can use big data processing techniques to speed up data comparisons. If we need near real-time reconciliation, a streaming platform such as Flink is used; otherwise, end-of-day batch processing such as Hadoop is enough.

__Problem 3__: Cut-off time issue. For example, if we choose 00:00:00 as the daily cut-off time, one record is stamped with 23:59:55 in the internal system, but might be stamped 00:00:30 in the external system (Paypal), which is the next day. In this case, we couldn’t find this record in today’s Paypal records. It causes a discrepancy.

__Possible solution__:  we need to categorize this break as a “temporary break” and run it later against the next day’s Paypal records. If we find a match in the next day’s Paypal records, the break is cleared, and no more action is needed.

You may argue that if we have exactly-once semantics in the system, there shouldn’t be any discrepancies. But the truth is, there are so many places that can go wrong. Having a reconciliation system is always necessary. It is like having a safety net to keep you sleeping well at night. 
