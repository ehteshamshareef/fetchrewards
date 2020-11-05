import json
from flask import Flask,request,jsonify

app = Flask(__name__)

def getEmailCount(emails):
    unique = set()
    for i in range(len(emails)):
        # Splitting on @ to get the userid and domain name.
        _firstSplit = emails[i].split("@")
        userid = _firstSplit[0]
        domain = _firstSplit[1]

        # Splitting "userid" on "+" to discard the string after "+".
        _secondSplit = userid.split("+")
        beforePlus = _secondSplit[0]


        # Splitting the string before "+" on "." because placement of "." has to be ignored.
        _thirdSplit = beforePlus.split(".")

        # Getting the parsed email from _thirdSplit and domain
        parsedEmail = "".join(_thirdSplit) + "@" + "".join(domain)

        # Adding the parsed email to an unordered set.
        unique.add(parsedEmail)
    return len(unique)

@app.route('/getUnique',methods = ["POST"])
def get_unique():
    #Get the list of emails from the query parameter "emails" since we are using a GET request.

    #Light error handling
    try:
        #Get the email list from the request body
        emailList = request.json["emails"]

        #Calling the function defined above to get number of unique email addresses.
        uniqueEmails = getEmailCount(emailList)
    except Exception as e:
        return jsonify({"data": None, "message": "An unexpected error has occurred."}), 500

    return jsonify({"data": uniqueEmails,"message": "Server OK."})


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 80)




# print (getEmailCount(["test.email@gmail.com","test.email+spam@gmail.com","testemail@gmail.com","test.email@fetchrewards.com"]))