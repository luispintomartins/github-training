import os
import json

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from github import IssueComment, NamedUser, GithubIntegration, Auth
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/webhook', methods=['POST'])

def webhook():

    key = os.path.dirname(__file__) + "/../key/test-github-app-asdasds.2023-10-13.private-key.pem"
    app_id = 407736
    # repository = "luispintomartins/github-training"

    # generate the code and print webhook
    with open(key, "r") as private_key:
        auth = Auth.AppAuth(app_id, private_key.read())
        gi = GithubIntegration(auth=auth)
        installation = gi.get_installations()[0]
        g = installation.get_github_for_installation()

        if request.method == 'POST':
            data = request.json
            print("Data received from Webhook is: ", request.json)
            
            installation_id = data["installation"]["id"]
            pull_request_number = data["number"]
            pull_request_user_login = data["pull_request"]["user"]["login"]
            pull_request_user_id = data["pull_request"]["user"]["id"]
            pull_request_repository_name = data["pull_request"]["head"]["repo"]["full_name"]

            repo = g.get_repo(pull_request_repository_name)
            issue = repo.get_issue(number=pull_request_number)
            issue.create_comment("I see you !")
            IssueComment(user=NamedUser(login=pull_request_user_login), id=pull_request_user_id)

            return "OK!"

# main driver function
if __name__ == '__main__':

        # run() method of Flask class runs the application 
        # on the local development server.
        app.run(host="localhost", port=3000, debug=True)
