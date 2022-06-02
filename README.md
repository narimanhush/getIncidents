# getIncidents
<h1>getIncident</h1>
<p>An API written in Python using Flask which queries other APIs, normalizes the data, and creates an endpoint on localhost:9000/incidets. By sending a GET request to /incidents, you will receive and "incident" object which conatins, for each employeee, a list of incidents organized by severity </p>

<h2>requirements</h2>
<p>First, install Python 3 using https://www.python.org/downloads/
using your command prompt, enter the following commands to install the required libraries: 
</p>
 
```python
pip install flask
pip install flask-restful
pip install requests
```
<h2>How to run</h2>
open incidents.py and update the username and password variables with API credentials 

Run requests.py using `py incidents.py`. Once the server has initialized, you will see "Running on http://127.0.0.1:9000/" as the last line on your command prompt. 

To query the API, run `py request.py` in a separate command prompt window. 

<h2>Overall approach<h2>
<p>
 1. Queried each API endpoint and studied the various key/value pairs
 2. created the incident_types list to store the response from each API along with the the name of the API queried. This is presented in the getData() function as we are essentially collecting raw data from each endpoint
 3. Created the "incidents" dictionary which represents the final JSON response returned once /incidents is queried 
 4. For each incident type, i looped through each entry. If the employee ID is present in the "incidents" object then I add the entry to that employee ID with respect to the entry's severity (low, medium, high, critical).
 5. Some normaization occurs depending on the avaialble identification in each API endpoint. For example, for the "other" endpoint. I check to see if the idnetity field contains an IP address or an employee ID. If it contains an IP adress, I check the identities object for the associated employee ID.
 6. I created a simple API using flask an created a resource which returns the incident object when /incidents is queried using a GET request 
</p>
 
<h2>Other approaches considered</h2>

I considered using an approach where the data is normalized in a Pandas Dataframe(by adding corresponding employee ID & incident type to each entry), sorted based on employee ID and severity and then create the final JSON object from the sorted Datafram. I didn't follow this route because i though casting from JSON to datafram and back to JSON would intoruce more room for errors. 
 
 <h2>Considerations for deployment in production</h2>
 1. Error handling for when getData() received a status code other than 200 for either of the API endpoints.



