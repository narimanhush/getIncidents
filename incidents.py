from textwrap import indent
import requests
import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


username = 'elevateinterviews'
password = 'ElevateSecurityInterviews2021'

def getIdentities(usrname,passowrd):
    identities = requests.get('https://incident-api.use1stag.elevatesecurity.io/identities/' ,auth=(username,password)).json()
    return identities

def getData(username, password):
    incident_types = [['denial'] ,['intrusion'], ['executable'],['misuse'],['unauthorized'], ['probing'],['other']]
    
    e_identifiers = ['employee_id','reported_by','internal_ip','machine_ip']

    for item in incident_types:
        item.append(requests.get('https://incident-api.use1stag.elevatesecurity.io/incidents/'+item[0]+'/' ,auth=(username,password)).json())
    return incident_types

def getIncidents(incident_types):
    incidents = {}
    for item in incident_types:
        inc_type = item[0]
        # print(inc_type)
        all_incidents = item[1]['results']
        # print(len(all_incidents))
        for inc in all_incidents:
            inc['type'] = inc_type
            if inc['type'] == 'denial':
                emp_id = str(inc['reported_by'])
            elif inc['type'] == 'intrusion':
                emp_id = identities[inc['internal_ip']]
            elif inc['type'] == 'executable':
                emp_id = identities[inc['machine_ip']]
            elif inc['type'] == 'misuse':
                emp_id= str(inc['employee_id'])
            elif inc['type'] == 'unauthorized':
                emp_id= str(inc['employee_id'])
            elif inc['type'] == 'probing':
                emp_id = identities[inc['ip']]
            elif inc['type'] == 'other':
                if type(inc['identifier']) == str:
                    emp_id =  identities[inc['identifier']]
                else:
                    emp_id = str(inc['identifier'])
            # print(inc)
            # print(emp_id)

            if emp_id not in incidents.keys():
                incidents[emp_id] = {
                    'low':{
                        'count': 0,
                        'incidents': []
                    },
                    'medium':{
                        'count':0,
                        'incidents':[]
                    },
                    'high':{
                        'count':0,
                        'incidents':[]
                    },
                    'critical':{
                        'count':0,
                        'incidents':[]
                    }
                }
                incidents[emp_id][inc['priority']]['incidents'].append(inc)
                incidents[emp_id][inc['priority']]['count'] += 1
            else:
                incidents[emp_id][inc['priority']]['incidents'].append(inc)
                incidents[emp_id][inc['priority']]['count'] += 1
    incidents = json.dumps(incidents, indent=4)
    return incidents

identities = getIdentities(username,password)
incident_types = getData(username,password)

class incident(Resource):
    def get(self):
        return getIncidents(incident_types)
api.add_resource(incident, "/incident")

if __name__ == "__main__":
    app.run(debug=True, port= 9000)




    

   




# f = open('out.txt','w')
# f.write(incidents)
# f.close()