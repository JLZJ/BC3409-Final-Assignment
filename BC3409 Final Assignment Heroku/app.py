#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route("/", methods = ["GET", "POST"])
def index(): 
    if request.method == "POST":
        if 'lr' in request.form:
            print('Logistic regression chosen')
            age = request.form.get("agelr")
            loan = request.form.get("loanlr")
            if age=='' or loan=='':
                return(render_template("index.html", resultlr = 'Please key in all fields with proper values', resultcart='', resultrf='', resultxgb='', resultnn=''))
            model = joblib.load("lr.gz")
            pred = model.predict([[float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
            else:
                s = "This user is likely to default"
            return(render_template("index.html", resultlr = s, resultcart='', resultrf='', resultxgb='', resultnn=''))
        elif 'cart' in request.form:
            print('CART chosen')
            income = request.form.get("incomecart")
            age = request.form.get("agecart")
            loan = request.form.get("loancart")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='Please key in all fields with proper values', resultrf='', resultxgb='', resultnn='', carttab=True))
            model = joblib.load("cart.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
            else:
                s = "This user is likely to default"
            return(render_template("index.html", resultlr = '', resultcart=s, resultrf='', resultxgb='', resultnn='', carttab=True))
        elif 'rf' in request.form:
            print('Random forest chosen')
            income = request.form.get("incomerf")
            age = request.form.get("agerf")
            loan = request.form.get("loanrf")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='Please key in all fields with proper values', resultxgb='', resultnn='', rftab=True))
            model = joblib.load("rf.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
            else:
                s = "This user is likely to default"
            return(render_template("index.html", resultlr = '', resultcart='', resultrf=s, resultxgb='', resultnn='', rftab=True))
        elif 'xgb' in request.form:
            print('XGBoost chosen')
            income = request.form.get("incomexgb")
            age = request.form.get("agexgb")
            loan = request.form.get("loanxgb")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='Please key in all fields with proper values', resultnn='', xgbtab=True))
            model = joblib.load("xgb.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
            else:
                s = "This user is likely to default"
            return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb=s, resultnn='', xgbtab=True))
        elif 'nn' in request.form:
            print('Neural network chosen')
            income = request.form.get("incomenn")
            age = request.form.get("agenn")
            loan = request.form.get("loannn")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn='Please key in all fields with proper values', nntab=True))
            model = joblib.load("nn.gz")
            scaler = joblib.load("scaler.bin")
            pred = model.predict(scaler.transform([[float(income), float(age), float(loan)]]))
            if pred==0:
                s = "This user is unlikely to default"
            else:
                s = "This user is likely to default"
            return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn=s, nntab=True))
        
    else:
        return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn=''))


# In[4]:


if __name__ == '__main__':
    app.run()


# In[ ]:




