from flask import Flask, render_template, jsonify, make_response
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Add CORS headers manually
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Path to dataset (same folder as app.py)
DATA_FILE = os.path.join(os.path.dirname(__file__), "Phone Pay -1.csv")

def load_data():
    df = pd.read_csv(DATA_FILE)
    # Convert date columns if they exist
    date_columns = ['Transaction_Date', 'Signup_Date']
    for col in date_columns:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass
    return df

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/popular-banks")
def popular_banks():
    df = load_data()
    bank_counts = df["Bank"].fillna("Unknown").value_counts().head(10).to_dict()
    return jsonify(bank_counts)

@app.route("/api/popular-states")
def popular_states():
    df = load_data()
    state_counts = df["State"].fillna("Unknown").value_counts().head(10).to_dict()
    return jsonify(state_counts)

@app.route("/api/email-domains")
def email_domains():
    df = load_data()
    df["Domain"] = df["Person_EmailId"].str.split("@").str[-1]
    domain_counts = df["Domain"].value_counts().head(10).to_dict()
    return jsonify(domain_counts)

@app.route("/api/summary")
def summary():
    df = load_data()
    total_users = len(df)
    popular_bank = df["Bank"].fillna("Unknown").value_counts().idxmax()
    popular_state = df["State"].fillna("Unknown").value_counts().idxmax()
    
    # Calculate transaction metrics if available
    transaction_volume = None
    avg_transaction = None
    
    if 'Transaction_Amount' in df.columns:
        transaction_volume = df['Transaction_Amount'].sum()
        avg_transaction = df['Transaction_Amount'].mean()
    
    return jsonify({
        "total_users": total_users,
        "popular_bank": popular_bank,
        "popular_state": popular_state,
        "transaction_volume": transaction_volume,
        "avg_transaction": avg_transaction
    })

@app.route("/api/state-wise-data")
def state_wise_data():
    df = load_data()
    state_data = df.groupby('State').agg({
        'Person_ID': 'count',
        'Transaction_Amount': 'sum' if 'Transaction_Amount' in df.columns else None
    }).rename(columns={'Person_ID': 'user_count'}).to_dict('index')
    
    return jsonify(state_data)

@app.route("/api/transaction-trends")
def transaction_trends():
    df = load_data()
    
    # Check if we have transaction date and amount data
    if 'Transaction_Date' in df.columns and 'Transaction_Amount' in df.columns:
        df['Transaction_Month'] = df['Transaction_Date'].dt.to_period('M')
        monthly_data = df.groupby('Transaction_Month').agg({
            'Transaction_Amount': ['sum', 'count']
        }).reset_index()
        
        monthly_data.columns = ['Month', 'Total_Amount', 'Transaction_Count']
        monthly_data['Month'] = monthly_data['Month'].astype(str)
        
        return jsonify(monthly_data.to_dict('records'))
    
    return jsonify([])

@app.route("/api/user-demographics")
def user_demographics():
    df = load_data()
    
    # Age demographics if available
    age_data = {}
    if 'Age' in df.columns:
        bins = [0, 18, 25, 35, 45, 55, 100]
        labels = ['Under 18', '18-24', '25-34', '35-44', '45-54', '55+']
        df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
        age_data = df['Age_Group'].value_counts().to_dict()
    
    # Gender demographics if available
    gender_data = {}
    if 'Gender' in df.columns:
        gender_data = df['Gender'].value_counts().to_dict()
    
    return jsonify({
        "age_groups": age_data,
        "genders": gender_data
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)