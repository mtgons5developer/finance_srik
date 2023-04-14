from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Store the API tokens in a dictionary
api_tokens = {}

@app.route('/api_token', methods=['POST'])
def create_api_token():
    # Generate a random API token value
    api_token = secrets.token_urlsafe(32)

    # Store the token value in the dictionary with associated metadata
    api_tokens[api_token] = {
        'user_id': request.json['user_id'],
        'expiration': request.json['expiration']
    }

    # Return the token value to the client
    return jsonify({'api_token': api_token}), 201

@app.route('/api_token/<api_token>', methods=['DELETE'])
def revoke_api_token(api_token):
    # Check if the API token exists
    if api_token in api_tokens:
        # Remove the API token from the dictionary
        del api_tokens[api_token]
        return '', 204
    else:
        return '', 404

if __name__ == '__main__':
    app.run(debug=True)
