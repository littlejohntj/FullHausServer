from haus import *
from flask import Flask, jsonify
import json

app = Flask(__name__)
connection = Controller()
connection.delete_tables()
connection.create_tables()
connection.add_user(assoc_name="Berkly testing Lakes", address="6933 West Street, Coral Springs, FL 32304", phone="954-496-0433", email="tjl13c@my.fsu.edu")
connection.add_user(assoc_name="Merpy testing Stones", address="1234 East Drive, West Palm, MA 42134", phone="784-432-0123", email="here_we_go@google.com")

@app.route('/search', methods=['GET','POST'])
def search():
	global connection
	json_list = []
	#input_string = str(json.loads(request.data)['input'])
	input_string = "testing"
	users = connection.get_users_by_substring_of_assoc_name(assoc_name=input_string)
	for user in users:
		json_list.append(user.user_to_dictionary())
	return json.dumps(json_list)

def reset():
	connection = Controller()
	connection.delete_tables()

def set_up():
	global connection
	connection = Controller()
	connection.create_tables()
	connection.add_user(assoc_name="Berkly testing Lakes", address="6933 West Street, Coral Springs, FL 32304", phone="954-496-0433", email="tjl13c@my.fsu.edu")
	connection.add_user(assoc_name="Merpy testing Stones", address="1234 East Drive, West Palm, MA 42134", phone="784-432-0123", email="here_we_go@google.com")


if "__main__" == __name__:
	app.run(debug=True, port=5000, threaded=False)
	