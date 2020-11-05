# Fetch rewards assignment



To run : 

1) Install Python 3.7.5 (https://www.python.org/downloads/release/python-375/)
2) Install the requirements by opening the terminal and navigating to the folder where the files are:
   Type this in the terminal ->    pip install -r requirements.txt
3) Execute in the terminal -> python main.py (to start the server)

Use postman to make the request body in the following manner with the content type as json and make a POST request to localhost:80/getUnique:

<pre>
{
  "emails" : ["test.email@gmail.com",".test.email+spam@gmail.com","testemail@gmail.com"]
}
</pre>

The output will be in the following manner : 

<pre>
{
    "data": 1,
    "message": "Server OK."
}
</pre>


<img src = "https://github.com/ehteshamshareef/fetchrewards_assignment/blob/master/screenshot.png?raw=true">
