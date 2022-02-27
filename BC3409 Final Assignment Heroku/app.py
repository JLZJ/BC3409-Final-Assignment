#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, session
from flask_session import Session 
import os
import joblib

# In[2]:


app = Flask(__name__)
app.secret_key = os.urandom(12).hex()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# In[3]:


from flask import request, render_template

@app.route("/", methods = ["GET", "POST"])
def index(): 
    if 'past_vals' not in session:
        session['past_vals'] = []
    if request.method == "POST":
        if 'lr' in request.form:
            print('Logistic regression chosen')
            age = request.form.get("agelr")
            loan = request.form.get("loanlr")
            if age=='' or loan=='':
                return(render_template("index.html", resultlr = 'Please key in all fields with proper values', resultcart='', resultrf='', resultxgb='', resultnn='', past_vals=session['past_vals']))
            model = joblib.load("lr.gz")
            pred = model.predict([[float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
                session['past_vals'] = [f'Logistic Regression: Age - {age}, Loan - {loan}: Unlikely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            else:
                s = "This user is likely to default"
                session['past_vals'] = [f'Logistic Regression: Age - {age}, Loan - {loan}: Likely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            return(render_template("index.html", resultlr = s, resultcart='', resultrf='', resultxgb='', resultnn='', past_vals=session['past_vals']))
        elif 'cart' in request.form:
            print('CART chosen')
            income = request.form.get("incomecart")
            age = request.form.get("agecart")
            loan = request.form.get("loancart")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='Please key in all fields with proper values', resultrf='', resultxgb='', resultnn='', carttab=True, past_vals=session['past_vals']))
            model = joblib.load("cart.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
                session['past_vals'] = [f'CART: Income - {income}, Age - {age}, Loan - {loan}: Unlikely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            else:
                s = "This user is likely to default"
                session['past_vals'] = [f'CART: Income - {income}, Age - {age}, Loan - {loan}: Likely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            return(render_template("index.html", resultlr = '', resultcart=s, resultrf='', resultxgb='', resultnn='', carttab=True, past_vals=session['past_vals']))
        elif 'rf' in request.form:
            print('Random forest chosen')
            income = request.form.get("incomerf")
            age = request.form.get("agerf")
            loan = request.form.get("loanrf")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='Please key in all fields with proper values', resultxgb='', resultnn='', rftab=True, past_vals=session['past_vals']))
            model = joblib.load("rf.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
                session['past_vals'] = [f'Random Forest: Income - {income}, Age - {age}, Loan - {loan}: Unlikely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            else:
                s = "This user is likely to default"
                session['past_vals'] = [f'Random Forest: Income - {income}, Age - {age}, Loan - {loan}: Likely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            return(render_template("index.html", resultlr = '', resultcart='', resultrf=s, resultxgb='', resultnn='', rftab=True, past_vals=session['past_vals']))
        elif 'xgb' in request.form:
            print('XGBoost chosen')
            income = request.form.get("incomexgb")
            age = request.form.get("agexgb")
            loan = request.form.get("loanxgb")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='Please key in all fields with proper values', resultnn='', xgbtab=True, past_vals=session['past_vals']))
            model = joblib.load("xgb.gz")
            pred = model.predict([[float(income), float(age), float(loan)]])
            if pred==0:
                s = "This user is unlikely to default"
                session['past_vals'] = [f'XGBoost: Income - {income}, Age - {age}, Loan - {loan}: Unlikely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            else:
                s = "This user is likely to default"
                session['past_vals'] = [f'XGBoost: Income - {income}, Age - {age}, Loan - {loan}: Likely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb=s, resultnn='', xgbtab=True, past_vals=session['past_vals']))
        elif 'nn' in request.form:
            print('Neural network chosen')
            income = request.form.get("incomenn")
            age = request.form.get("agenn")
            loan = request.form.get("loannn")
            if income=='' or age=='' or loan=='':
                return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn='Please key in all fields with proper values', nntab=True, past_vals=session['past_vals']))
            model = joblib.load("nn.gz")
            scaler = joblib.load("scaler.bin")
            pred = model.predict(scaler.transform([[float(income), float(age), float(loan)]]))
            if pred==0:
                s = "This user is unlikely to default"
                session['past_vals'] = [f'Neural Network: Income - {income}, Age - {age}, Loan - {loan}: Unlikely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            else:
                s = "This user is likely to default"
                session['past_vals'] = [f'Neural Network: Income - {income}, Age - {age}, Loan - {loan}: Likely to default'] + session['past_vals']
                if len(session['past_vals'])==11:
                    session['past_vals'].pop()
            return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn=s, nntab=True, past_vals=session['past_vals']))
        
    else:
        return(render_template("index.html", resultlr = '', resultcart='', resultrf='', resultxgb='', resultnn=''))


# In[4]:


if __name__ == '__main__':
    app.run()

