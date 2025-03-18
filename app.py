from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Run the 'top' command and capture the output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the response
    response = f"""
    <pre>
    Name: Anurag Sharma
    User: {username}
    Server Time (IST): {current_time}

    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)