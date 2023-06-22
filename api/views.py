from django.shortcuts import render
from rest_framework import generics, status
from django.urls import path
import pandas as pd
import random
from django.shortcuts import render
from rest_framework import generics, status
from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import os, json

from .serializers import DataSerializer

# Read data from CSV file
# csv_file_path = 'MOCK_DATA.csv'

# csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'MOCK_DATA.csv')
# csv_file_path = os.path.join(settings.BASE_DIR, 'MOCK_DATA.csv')
# general_data= pd.read_csv(csv_file_path)

csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'MOCK_DATA.csv')
general_data= pd.read_csv(csv_file_path)


lines = 200 # Default number of lines to generate

def gender(value='g', lines=1000):
    '''
    Creates gender data
    
    >>> gender(5)
    >>> ['Male', 'Female', 'Male', 'Male', 'Female']
    '''
    genders = ['Male', 'Female']
    result = random.choices(genders, k=lines)
    return result

def generate_number_list(start, end, lines=1000):
    '''
    Generate numbers within a given range 
       
    >>> generate_number_list(2, 9, 4)
    >>> [2, 4, 7, 8]
    '''
    num_list = []
    for _ in range(lines):
        num = random.randint(start, end)
        num_list.append(num)
    return num_list

def number(value, lines=1000):
    '''
    Creates number data
    '''
    # Check if type is number
    try: 
        age_range = value.split('(')[1].split(')')[0]
        if len(age_range) > 0:
            age_start, age_end = map(int, age_range.split('-'))
    except:
        age_start, age_end = 12, 49
        
    result = generate_number_list(age_start, age_end, lines)
        
    return result

def data_generator(value, lines=1000):
    '''
    Helper function that generates data using the given value from the dict
    '''
    return random.choices(general_data[value].to_list(), k=lines)

modes = [
    "csv", # pd to csv from dict_data or pandas df
    "json",
    "sql",
    "delimiter"
]

def create_data_from_dict(data_dict, lines=1000):
    '''
    Container containing the functions that create the data from dict
    '''
    data_df = pd.DataFrame()
    
    models = {
        'id' : data_generator,
        'name' : data_generator,
        'gender' : gender,
        'number' : number,
        'ip' : data_generator,
        'city' : data_generator,
        'state' : data_generator,
        'country' : data_generator,
        'email' : data_generator,
    }
    
    for key, value in data_dict.items():
        value =  value.lower()
        
        if 'number' in value:
            # Get function from models dictionary or use default function (number)
            func = models.get(key, number)
            result = func(value, lines)
            data_df[key] = result
        elif 'country' in value:
            # Assign fixed value 'Nigeria' for 'country' key
            # data_df[key] = ['Nigeria']
            _=0
        else:
            # Get function from models dictionary or use default function (data_generator)
            func = models.get(key, models[value])
            result = func(value, lines)
            data_df[key] = result
            
    # Save the generated data to a dataframe
    # Return dataframe
    
    return data_df


class CreateDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data  # Get the data from the request payload
        headers = request.headers # Get the headers from the request payload
                
        try:
            # mode = request.headers.get('mode')
            lines = headers.get('line') or 10
            
            # mode = 'csv'
            # lines = 1000
                                    
            df = create_data_from_dict(data, lines = lines)
            result = json.loads(df.to_json(orient='records', indent=4))
                        
            # return Response(result, status=status.HTTP_200_OK)
            return Response(result, status=status.HTTP_200_OK)
        
        except Exception as e:
            
            return Response(f'Exception during data creation: {e}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
# def home(request):
#     return render(request, 'home.html')


def landing(request):
    return render(request, 'landing.html')
