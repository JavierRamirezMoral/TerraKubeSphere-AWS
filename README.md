# TerraKubeSphere II: Power Conversational AI ChatBot in AWS.

_At the end of this README, you can find the VideoTutorial._

## Introduction.
<div align="justify"> 
Chatbots represent one of the latest trends in contemporary technology, exerting a significant influence on our daily routines. From managing appointments and offering medical guidance to facilitating flight reservations and delivering real-time updates, they streamline our lives, rendering tasks more manageable and efficient. Thanks to their ability to deliver immediate responses and tailor interactions, chatbots simplify our interactions, making them more personalized. 
Amazon Lex stands out as a leading platform for crafting rapid and scalable chatbots. In this article, I will guide you through the process of constructing a chatbot utilizing Amazon Lex and Lambda, illustrating how to seamlessly integrate it into your React.js project. 
</div> <br>
This tutorial will cover the following aspects of building a chatbot: 

* Utilizing Bedrock Claude LLM, an advanced language model to understand and generate human-like text. 

* Leveraging the Amazon Lex UI console for chatbot construction and testing.
  
* Employing AWS Lambda Function to augment the chatbot's capabilities, enabling it to furnish users with more precise information.
  
* Harnessing AWS CloudFormation to automate the deployment and administration of applications through straightforward procedures.
  
* Integration with ReactJS for building user interfaces (UIs) for single-page applications.

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/AWS%20CHATBOT.png)

## Part 1: Amazon Tools. 
<div align="justify"> 
AWS offers a comprehensive suite of AI services and tools designed to simplify the integration and deployment of artificial intelligence technologies. From pre-built AI services like image recognition and natural language processing to machine learning services such as Amazon SageMaker for building and training custom models, AWS provides scalable infrastructure and managed services to support various AI workloads. With seamless integration between services and flexible deployment options, AWS empowers businesses to harness the power of AI effectively, accelerating innovation and driving intelligent decision-making. Here are the main Amazon tools that we need to use for this tutorial. </div>

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

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/CloudFormation.png)

### ReactJS 
 <div align="justify"> 
ReactJS, often simply referred to as React, is an open-source JavaScript library developed by Facebook. It is primarily used for building user interfaces (UIs) for single-page applications. React allows developers to create interactive UI components that can efficiently update and render changes to the user interface when data changes. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/ReactJS.png)


## Part 2: Chatbot Technology. 
 <div align="justify"> 
From time to time, humans have been trying to find more and more ways to make lives easier using technology. With all sorts of applications & software taking care of day-to-day life, chatbots are soon becoming an integral part of daily life. It’s the latest buzzword.   </div> <br>
 <div align="justify"> 
In simple terms, chatbot is a service or tool that you can communicate with via a chat interface. Chatbot understands what you are trying to imply and replies with a relevant message or directly completes the desired task for you. 
 </div> <br>
 <div align="justify"> 
Chatbot technology enables the development of conversational agents that interact with users in natural language, typically through text or speech interfaces. These AI-powered bots can be deployed across various platforms like websites, messaging apps, and voice assistants. Chatbots use natural language processing (NLP) and machine learning algorithms to understand user inputs, interpret intents, and generate relevant responses. They can handle a wide range of tasks, from answering FAQs and providing customer support to assisting with product recommendations and automating business processes. Chatbots offer businesses a scalable and efficient way to engage with customers, streamline operations, and deliver personalized experiences round the clock. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/How-an-AI-Chatbot-Works.png)

### AWS ChatBot Features 

Important features of the AWS Chatbot service include the following: 

* Customize notifications: You can define and receive customized AWS service and application notifications directly in your chat channels. Custom notifications can be as succinct or comprehensive as you desire and use the same Amazon SNS-based mechanisms as default notifications. 

* Create custom actions: Custom actions transform your notifications into actionable items. A custom action appears as a button on your notifications. This button represents a Lambda function or CLI command that you define. You can use custom actions to retrieve telemetry information, run Lambda functions, run an automation runbook, and notify team members. When an issue arises, you can easily act directly from your notifications. 

* Search and discover AWS information: You can search and discover information about AWS services and your AWS resources by asking AWS Chatbot natural language questions. The answers provided in your chat channels are pulled directly from your AWS environments, AWS product documentation, and support articles. This makes it easier to locate your resources, find product information, and troubleshoot issues.

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/AWS%20ChatBot%20Features.png)

### How AWS Chatbot Works 
 <div align="justify"> 
AWS Chatbot uses Amazon Simple Notification Service (Amazon SNS) topics to send event and alarm notifications from AWS services to your chat channels. Once an SNS topic is associated with a configured chat client, events and alarms from various services are processed and notifications are delivered to the specified chat channels and webhooks. For Microsoft Teams and Slack, after an administrator approves AWS Chatbot support for the workspace or tenant, anyone in the workspace or team can add AWS Chatbot to their chat channels. For Amazon Chime, users with AWS Identity and Access Management (IAM) permissions to use Amazon Chime can add AWS Chatbot to their webhooks. You use the AWS Chatbot console to configure chat clients to receive notifications from SNS topics. </div> <br>

![Alt text](https://github.com/JavierRamirezMoral/TerraKubeSphere-AWS/blob/main/Images/How%20AWS%20Chatbot%20Works.jpg)

## Part 3: Conclusion. 
 <div align="justify"> 
In essence, developing chatbots fueled by Bedrock Claude LLM alongside AWS Lex, Lambda, and CloudFormation, and seamlessly integrating them with a ReactJS web application, presents a robust and effective strategy for enhancing user engagement and satisfaction. </div>
<br>
 <div align="justify"> 
By harnessing these AWS services, you can effortlessly create chatbots with natural language understanding, seamlessly incorporate them into your web applications, and automate diverse workflows. Following the steps outlined in this article, you can build and deploy chatbots with ease, sidestepping concerns about the underlying infrastructure.  </div>
<br>
 <div align="justify"> 
Leveraging the capabilities of AWS Lex, Lambda, CloudFormation, and ReactJS enables you to furnish a comprehensive solution for constructing sophisticated chatbots. Such chatbots have the potential to elevate user experiences and optimize business processes, delivering end-to-end solutions that drive efficiency and customer satisfaction.  </div>









