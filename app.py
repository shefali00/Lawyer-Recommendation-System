from dotenv import load_dotenv
import os
import time
import spacy
import json
from geopy.geocoders import Nominatim
import google.generativeai as genai
import streamlit as st 
import pandas as pd
import random
from geopy.geocoders import Nominatim
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#dictionary of indian locations

#create dataframe from csv file
df = pd.read_excel('C:\\Users\\Shefali\\Downloads\\output_data.xlsx')

#function to greet the user 
def greet_user():
    print("Hello! I'm here to assist you. Please provide me with your case description.")

#get the nearest location
def find_nearest_location(user_location, locations):
 
    geolocator = Nominatim(user_agent="my_geocoding_app",timeout=10)
    user_coordinates = geolocator.geocode(user_location)
    if user_coordinates is None:
        return None
    user_lat, user_lon = user_coordinates.latitude, user_coordinates.longitude
    closest_location = None
    min_distance = float('inf')
    for location in locations:
        location_coordinates = geolocator.geocode(location)
        if location_coordinates is None:
            continue
        location_lat, location_lon = location_coordinates.latitude, location_coordinates.longitude
        distance = ((user_lat - location_lat) ** 2 + (user_lon - location_lon) ** 2) ** 0.5

        if distance < min_distance:
            min_distance = distance
            closest_location = location

    return closest_location 

#generate a list of unique values
def get_unique_values_from_dict(input_dict):
    unique_values = set(input_dict.values())
    return unique_values

#function to generate response
def generate_response(case_description):
    greet_user()
    print("Thank you for providing your case description. We will now proceed to assist you further.")
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt=f'''consider yourself a lawyer recommendation expert that returns just a list containing 3 values and nothing else and for the given case description {case_description} Suggest type of lawyer, type of court, and location for it in India.select type of lawyer from following list : Intellectual Property Lawyer, Public Interest Lawyer, Tax Lawyer, Corporate Lawyers, Immigration Lawyers, Criminal Defense, Civil Rights Lawyer, Family Lawyer, Environmental Lawyer, Entertainment Lawyer, Estate Planning Lawyer, Civil Litigation Lawyers, Constitutional Lawyers, Real Estate Lawyers, Estate Planning Lawyers, Bankruptcy Lawyers, Labor Lawyers, Malpractice Lawyers, Personal Injury Lawyers, Toxic Tort Lawyers, Family Lawyers, Contract Lawyer, Employment Lawyer.Select the location from the following list : Nagaland,Odisha,Maharashtra,Andhra Pradesh,Tamil Nadu,Rajasthan,Arunachal Pradesh,Mizoram,Uttarakhand,Chhattisgarh,Uttar Pradesh,Gujarat,Telangana,Haryana,Bihar,Gauhati,
    ,Manipur,Patna,Jammu and Kashmir,Andaman and Nicobar Islands,West Bengal,Tripura,Jharkhand,Punjab,Delhi,Uttaranchal,Assam,Puducherry,Allahabad,Calcutta,West BengalSouth 24 Parganas:West Bengal,Karnataka,Himachal Pradesh,Madras,Meghalaya,Sikkim,Ladakh,Dadra and Nagar Haveli and Daman and Diu,Goa,Kerala,Bombay,Orissa,Mumbai'''
    response = model.generate_content(prompt)
    response=response.text
    response = [item.strip() for item in response.split(',')]
    user_location = response[2]
    df['Location'] = df['location'].str.lower()
    df['Type_of_Court'] = df['Type_of_Court'].str.lower()
    df['Type_of_Lawyer'] = df['Type_of_Lawyer'].str.lower()
    response_1 = response[1].lower()
    response_0=response[0].lower()
    
    # Filter rows based on conditions
    filtered_df = df[(df['Location'] == user_location) & (df['Type_of_Court'] == response_1) & (df['Type_of_Lawyer'] == response_0)]

    # Print the filtered DataFrame
    sorted_df = filtered_df.sort_values(by='Stars', ascending=False)
    return filtered_df
    
    
    
   

print(generate_response("my friend shot my father.i live in UP.i will prefer district court"))
    