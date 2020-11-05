# Fetch rewards assignment

Python Version : 3.7.5

To run : 

1) pip install -r requirements.txt
2) python main.py (to start the server)

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
