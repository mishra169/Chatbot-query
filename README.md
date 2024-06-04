# Chatbot-query
A chatbot for making SQL queries developed utilizing the GPT-3 open-source language model and the ability to get trained on a particular dataset.

**Backend**
Programmed using Python
Used Flask as a backend framework to retrieve user input and display chatbot output
Integrated MySQL to create a database to store user's messages and the chatbot's responses
Integrated OpenAI's GPT-3 open-source language model API using python to generate contextual responses

**Frontend**
Programmed using HTML and CSS
Used Flask to return HTML and CSS as the web application

***HOW TO RUN LOCALLY***
Clone this repo
Download MySQL Workbench
Run the following in MySQL Workbench to create a database

CREATE DATABASE messages
CREATE TABLE convo (ID int primary key, question VARCHAR(3000), response VARCHAR(3000));

Within MySQL Workbench, connect to the messages database
Edit the convo table to set ID to auto-increment and click apply
Generate your own API key from OpenAI and replace it in the code within the getvalue() function
Run python.py
Use the browser to connect to http://127.0.0.1:5000/ to interact with the chatbot


DISCLAIMER: I haven't hosted it online due to the unavailability of free cloud databases in which I have worked. I'll soon try to find an opensource database and implement the backend deployment.


![image](https://github.com/mishra169/Chatbot-query/assets/104723673/e3b25976-a8b9-4a12-be9c-f071d9e8a968)

