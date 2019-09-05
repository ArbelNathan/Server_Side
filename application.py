"""
here flask is handling the side server
"""
from datetime import datetime

from flask import Flask, request, jsonify

from server_side.handlers.sql.buildQueries import create_user, update_user, get_user, \
    get_user_by_email, delete_user


application = app = Flask(__name__)


@application.route('/', methods=['GET'])
def get_user_():
    user_id = request.args.get("id")
    user_email = request.args.get("email")
    if user_uni is not None:
        ans = get_user(user_id, user_uni)
        return jsonify(ans)
    elif user_email is not None:
        ans = get_user_by_email(user_email, user_uni)
        return jsonify(ans)

@application.route('/id', methods=['GET'])
def get_user_id():
    uni = request.args.get("uni")
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    idx = f'{uni}{str(timestamp.hex())}'
    return idx.replace('.', '').replace('+', '')

@application.route('/', methods=['POST'])
def create_user_():
    values = request.get_json()
    user_id = request.args.get("id")   
    ans = create_user(values, user_id, user_uni)
    return jsonify({"status": ans})


@application.route('/', methods=['PUT'])
def update_user_():
    values = request.get_json()
    user_id = request.args.get("id")
    ans = update_user(values, user_id, user_uni)
    return jsonify({"status": ans})


@application.route('/', methods=['DELETE'])
def delete_user_():
    user_id = request.args.get("id")
    ans = delete_user(user_id, user_uni)
    return jsonify(ans)


if __name__ == '__main__':
    application.run(debug=True)
