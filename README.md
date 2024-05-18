# TerraKubeSphere II: Power Conversational AI ChatBot in AWS.

_At the end of this README, you can find the VideoTutorial._

## Introduction.
<div align="justify"> 
Chatbots represent one of the latest trends in contemporary technology, exerting a significant influence on our daily routines. From managing appointments and offering medical guidance to facilitating flight reservations and delivering real-time updates, they streamline our lives, rendering tasks more manageable and efficient. Thanks to their ability to deliver immediate responses and tailor interactions, chatbots simplify our interactions, making them more personalized. 
</div> <br>
This tutorial will cover the following aspects of building a chatbot: 

* Firstly, we will use the Amazon Lex service to create our ChatBot and configure it.  

* We will integrate a lambda function and see how we could add an extra layer to our code with the functionalities of Bedrock Claude LLM. 

* We will conduct testing to verify and observe the functioning of our ChatBot. 

* We will integrate our Bot into our website using Kommunicate. We will explore other options for integrating it with CloudFormation. 

* We add response cards to enhance the user experience and make interactions more intuitive. 

* Finally, we use DynamoDB to collect data from our ChatBot. 

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/AWS%20CHATBOT.png)

## Part 1: Amazon Services. 
<div align="justify"> 
AWS offers a comprehensive suite of AI services and tools designed to simplify the integration and deployment of artificial intelligence technologies. From pre-built AI services like image recognition and natural language processing to machine learning services such as Amazon SageMaker for building and training custom models, AWS provides scalable infrastructure and managed services to support various AI workloads. With seamless integration between services and flexible deployment options, AWS empowers businesses to harness the power of AI effectively, accelerating innovation and driving intelligent decision-making. Here are the main Amazon tools that we need to use for this tutorial. </div>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/services.jpg)

### Bedrock Claude LLM 
<div align="justify"> 
Bedrock Claude LLM is a state-of-the-art language model designed to understand and generate human-like text. It’s based on advanced machine learning techniques and is particularly adept at handling nuanced language tasks. Bedrock Claude LLM augments the natural language understanding capabilities of Amazon Lex by providing a more sophisticated language model. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/Bedrock.png)

 ### Amazon Lex
 <div align="justify"> 
AWS Lex is a cloud-based service provided by Amazon Web Services that enables developers to build conversational interfaces using voice and text. It uses natural language understanding (NLU) technology to understand and interpret user input, allowing developers to create chatbots, voice bots, and virtual assistants that can interact with users in a human-like way. AWS Lex is like a brain that can understand what people say or type, and then respond back like a human. </div>
<br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/Lex.png)

#### Key Fundamental Components of the Lex service: 
* Intents as the name suggests, are a fundamental concept used to represent the purpose or goal of a user's input. Intents can be viewed as a verb, detecting what a user's intention is. For example, if you go to a pizza shop and order a pizza, your main intention is to order pizza, your purpose for going to the store is to get pizza. This works the same way for lex-powered chatbots. We must define intents so the bot can easily track or identify our goals during a conversation. 

* Utterances are examples of phrases or sentences that we might use to convey a specific meaning or request. For example, when we walk into the pizza store to order a box of pizza, a possible request we could make is "I want to order a box of pizza." These utterances are used to teach the chatbot how to understand and respond to what we are saying. The more utterance we give, the better the chatbot will be at understanding what we’re trying to say. 

* Slots are a collection of information that your prompt chatbot users to provide during a conversation with your bot. The bot will prompt the user to provide information for each slot, and once all of the required slots have been filled, the bot will be able to process the order and respond appropriately. Amazon Lex includes a variety of built-in slot types, including numbers, dates, countries, and many more. We can also define what sets of values are acceptable by creating our own custom slot types. 
<p align="center">
  <img src= "https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/Lex%20Key%20points.png"/>
</p>

### Amazon Lambda 
 <div align="justify"> 
AWS Lambda is a way to write and run code without worrying about setting up and maintaining the underlying server or computing resources. We can focus on writing our code, and Lambda takes care of executing it and scaling it as needed based on demand. It’s a popular choice for building serverless applications. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/Lambda.png)

### Amazon CloudFormation 
 <div align="justify"> 
Amazon CloudFormation is a service provided by Amazon Web Services (AWS) that enables you to define and provision the infrastructure resources for your cloud-based applications using a declarative template. Instead of manually configuring and managing individual resources such as EC2 instances, databases, and networking components, CloudFormation allows you to describe your desired infrastructure in a template file using a JSON or YAML syntax. 
 </div>  <br>

<p align="center">
  <img src= "https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/CloudFormation.png" width=100%/>
</p>

### Kommunicate  
 <div align="justify"> 
Kommunicate is a customer support and engagement platform that integrates seamlessly with websites and mobile apps to provide live chat support, chatbots, and other communication tools. It's designed to help businesses interact with their customers in real-time, automate responses, and manage conversations efficiently. Kommunicate offers features such as chat routing, canned responses, analytics, and integrations with popular customer relationship management (CRM) systems and helpdesk software. It's used by companies across various industries to enhance their customer support and engagement capabilities.  </div> <br>

<p align="center">
  <img src= "https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/Kommunicate%20.png" width=100%/>
</p>

### DynamoDB
 <div align="justify"> 
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data. For more information, see DynamoDB encryption at rest.  </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/dynamodb.png)

## Part 2: Chatbot Technology. 
 <div align="justify"> 
From time to time, humans have been trying to find more and more ways to make lives easier using technology. With all sorts of applications & software taking care of day-to-day life, chatbots are soon becoming an integral part of daily life. It’s the latest buzzword.   </div> <br>
 <div align="justify"> 
In simple terms, chatbot is a service or tool that you can communicate with via a chat interface. Chatbot understands what you are trying to imply and replies with a relevant message or directly completes the desired task for you. 
 </div> <br>
 <div align="justify"> 
Chatbot technology enables the development of conversational agents that interact with users in natural language, typically through text or speech interfaces. These AI-powered bots can be deployed across various platforms like websites, messaging apps, and voice assistants. Chatbots use natural language processing (NLP) and machine learning algorithms to understand user inputs, interpret intents, and generate relevant responses. They can handle a wide range of tasks, from answering FAQs and providing customer support to assisting with product recommendations and automating business processes. Chatbots offer businesses a scalable and efficient way to engage with customers, streamline operations, and deliver personalized experiences round the clock. </div> <br>

<p align="center">
  <img src= "https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/How-an-AI-Chatbot-Works.png" width=100%/>
</p>

### AWS ChatBot Features 

Important features of the AWS Chatbot service include the following: 
 <div align="justify"> 
   
* Customize notifications: You can define and receive customized AWS service and application notifications directly in your chat channels. Custom notifications can be as succinct or comprehensive as you desire and use the same Amazon SNS-based mechanisms as default notifications. 

* Create custom actions: Custom actions transform your notifications into actionable items. A custom action appears as a button on your notifications. This button represents a Lambda function or CLI command that you define. You can use custom actions to retrieve telemetry information, run Lambda functions, run an automation runbook, and notify team members. When an issue arises, you can easily act directly from your notifications. 

* Search and discover AWS information: You can search and discover information about AWS services and your AWS resources by asking AWS Chatbot natural language questions. The answers provided in your chat channels are pulled directly from your AWS environments, AWS product documentation, and support articles. This makes it easier to locate your resources, find product information, and troubleshoot issues.
</div>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/AWS%20ChatBot%20Features.png)

### How AWS Chatbot Works 
 <div align="justify"> 
AWS Chatbot uses Amazon Simple Notification Service (Amazon SNS) topics to send event and alarm notifications from AWS services to your chat channels. Once an SNS topic is associated with a configured chat client, events and alarms from various services are processed and notifications are delivered to the specified chat channels and webhooks. For Microsoft Teams and Slack, after an administrator approves AWS Chatbot support for the workspace or tenant, anyone in the workspace or team can add AWS Chatbot to their chat channels. For Amazon Chime, users with AWS Identity and Access Management (IAM) permissions to use Amazon Chime can add AWS Chatbot to their webhooks. You use the AWS Chatbot console to configure chat clients to receive notifications from SNS topics. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/How%20AWS%20Chatbot%20Works.jpg)

## Part 3: Conclusion. 
 <div align="justify"> 
To summarize (summarize), building chatbots powered by Bedrock Claude LLM with AWS Lex, Lambda, and CloudFormation or Kommunicate and integrating them with a web app is a powerful and efficient way to increase user engagement and customer satisfaction. In addition to being able to have a summary of our chatbot data stored in DynamoDB. </div>
<br>
 <div align="justify"> 
You can easily create chatbots with natural language understanding, integrate them with your web apps, and automate various workflows using these AWS Services. You can easily build and deploy chatbots by following the steps outlined in this video without having to worry about the underlying infrastructure.  </div>
<br>
 <div align="justify"> 
   You can provide an end-to-end solution for building sophisticated chatbots that can improve user experience and streamline business operations
 </div>

 # VideoTutorial in YT:

 [<img src="https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/AWS%20CHATBOT.png" width="100%">](https://youtu.be/tuWLN_4r9tw?si=3h-Mj4hyif6VE_PJ "Now in Android: 55")

Autor/a: Javier Ramírez Moral   

Curso: Administración de Sistemas MultiCloud con Azure, AWS y GCP.   

Centro: Tajamar   

Año académico: 2023-2024  

LinkedIn: https://www.linkedin.com/in/javier-ramirez-moral/ 
 
