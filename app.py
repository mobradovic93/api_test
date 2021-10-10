#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)


# In[2]:


class Users(Resource):
    def get(self):
        data = {'userId': {0: 'a1b', 1: 'a2c', 2: 'b1b', 3: 'b2c'},
                'name': {0: 'Joe', 1: 'Jenny', 2: 'Jack', 3: 'Jill'},
                'city': {0: 'Paris', 1: 'London', 2: 'London', 3: 'Berlin'},
                'locations': {0: "['0001', '0002', '0008']",
                 1: "['0003', '0004']",
                 2: "['0003', '0005']",
                 3: "['0006', '0007']"}}
        return {'data': data}, 200  # return data and 200 OK code
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations
if __name__ == '__main__':
    app.run()  # run our Flask app


# In[ ]:




