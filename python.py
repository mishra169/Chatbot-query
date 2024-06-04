import openai
from flask import Flask, render_template, request
import mysql.connector
from html import unescape
import joblib

#from api_secrets import API_KEY

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000", #Use your own MySQL password.
    database="messages" 
)

mycursor = db.cursor()


# Load the trained model
model = joblib.load('query_model.pkl')

#Create your own database and table in MySQL Workbench.
#mycursor.execute("CREATE DATABASE messages")
#mycursor.execute("CREATE TABLE convo (ID int primary key, question VARCHAR(3000), response VARCHAR(3000))")
#set ID to auto increment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    
    mycursor.execute("SELECT question FROM convo ORDER BY ID DESC LIMIT 1")
    qu = str(mycursor.fetchall())
    qu = qu.replace("[('", '')
    qu = qu.replace("',)]", '')

    mycursor.execute("SELECT response FROM convo ORDER BY ID DESC LIMIT 1")
    re = str(mycursor.fetchall())
    re = re.replace("[('", '')
    re = re.replace('[("', '')
    re = re.replace("',)]", '')
    re = re.replace('",)]', '')
    num_appear = re.count('\\n')
    re = re.replace("\\n", '', num_appear)

    message = request.form['message']
    askprompt = "You are an informative, happy, and helpful Query Chatbot, The conversation starts now. " + message
    openai.api_key = "sk-...." #put you api key here 
    response = openai.Completion.create(engine="text-davinci-001", prompt=askprompt, max_tokens=200)
    resp = response.choices[0].text
    resp2 = model.predict([message])[0]
    print(response)
    print(f"Model response: {resp}")
    mycursor.execute("INSERT INTO convo (question, response) VALUES (%s, %s)", (message, resp+resp2))
    db.commit()
    return render_template('index.html', m=message, r=resp, n=qu, s=re)


if __name__ == '__main__':
    app.run(debug=True)

