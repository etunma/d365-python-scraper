from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def get_contacts():
    first_names = ['John', 'Jane', 'Alice', 'Bob']
    last_names = ['Doe', 'Smith', 'Johnson', 'Brown']
    emails = ['john@example.com', 'jane@example.com', 'alice@example.com', 'bob@example.com']

    contacts = []
    for i in range(4):
        contacts.append({
            'firstname': first_names[i],
            'lastname': last_names[i],
            'emailaddress1': emails[i],
            'mobilephone': f'+23480{random.randint(10000000, 99999999)}'
        })

    return jsonify(contacts)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

