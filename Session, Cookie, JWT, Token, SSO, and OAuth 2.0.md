## Authentication Journey !!
![image](https://user-images.githubusercontent.com/22426280/227697014-a57c416f-425f-45dd-be76-c7189e0a4d17.png)

### 𝗪𝗪𝗪-𝗔𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗲
    🔹 Oldest & most basic method
    🔹 Browser asks for username & password
    🔹 Lacks control over login life cycle
    🔹 Rarely used today 
 ![image](https://user-images.githubusercontent.com/22426280/230318279-97b16268-6183-436e-b615-e27e492deda4.png)


### 𝗦𝗲𝘀𝘀𝗶𝗼𝗻-𝗖𝗼𝗼𝗸𝗶𝗲
    🔹 Server maintains session storage
    🔹 Browser keeps session ID
    🔹 Works mainly with browsers, not mobile app friendly
  ![image](https://user-images.githubusercontent.com/22426280/230319158-e2220a29-1820-455c-9f11-98c75ecce0d2.png)


### 𝗧𝗼𝗸𝗲𝗻
    🔹 Compatible with mobile apps
    🔹 Client sends token to server for validation

### 𝗝𝗪𝗧 (𝗝𝗦𝗢𝗡 𝗪𝗲𝗯 𝗧𝗼𝗸𝗲𝗻)
    🔹 Standard representation of tokens
    🔹 Digitally signed & verifiable
    🔹 No need to save session info server-side
  <img width="300" alt="Screenshot 2023-04-06 at 2 32 23 PM" src="https://user-images.githubusercontent.com/22426280/230329002-8a909041-966c-4266-ab8a-521c952633b7.png">


### 𝗦𝗦𝗢 (𝗦𝗶𝗻𝗴𝗹𝗲 𝗦𝗶𝗴𝗻-𝗢𝗻) & 𝗢𝗔𝘂𝘁𝗵 𝟮.𝟬. 
    🔹 SSO: Log in once, access multiple sites
    🔹 Uses CAS (central authentication service)
    🔹 OAuth 2.0: Authorize one site to access info on another
   <img width="300" alt="Screenshot 2023-04-06 at 2 19 56 PM" src="https://user-images.githubusercontent.com/22426280/230326770-3a2b2569-d03f-4fe5-973b-7e7eaf066da5.png">
            Built on concept called Federated Identity: It enables the sharing of identity information across trusted but independent systems 
            <img width="300" alt="Screenshot 2023-04-06 at 2 21 39 PM" src="https://user-images.githubusercontent.com/22426280/230327471-329655b3-b441-447b-9449-5558dc82ce22.png">
           
#### Two kinds of Authetication Process for SSO -:
   <img width="300" alt="Screenshot 2023-04-06 at 2 41 52 PM" src="https://user-images.githubusercontent.com/22426280/230331296-212b4cb5-1395-4366-aaeb-c6055a88bafb.png">
   
##### SAML (Security Assertion Markup Language)
    It is an XML based open standard for exchanging identity information between services.
###### Step1:
<img width="400" alt="Screenshot 2023-04-06 at 2 35 00 PM" src="https://user-images.githubusercontent.com/22426280/230332799-cb750cbb-d32e-4b22-9941-1409973954e8.png">

###### Step2:
<img width="400" alt="Screenshot 2023-04-06 at 2 37 28 PM" src="https://user-images.githubusercontent.com/22426280/230332989-7c8b9b81-a795-4c00-99ca-dc3eb9842e6c.png">

###### Step: For Third Part App like Workday
<img width="500" alt="Screenshot 2023-04-06 at 2 39 29 PM" src="https://user-images.githubusercontent.com/22426280/230333677-314000bd-3fc0-4b56-8086-d882638f8b47.png">


##### OpenID Connect
    It uses JWT Token to share information between services.
    
    
    

