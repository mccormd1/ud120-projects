#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""


##{'salary': 1111258, 'to_messages': 3627, 'deferral_payments': 'NaN', 'total_payments': 8682716, 
##'loan_advances': 'NaN', 'bonus': 5600000, 'email_address': 'jeff.skilling@enron.com', 
##'restricted_stock_deferred': 'NaN', 'deferred_income': 'NaN', 'total_stock_value': 26093672, 
##'expenses': 29336, 'from_poi_to_this_person': 88, 'exercised_stock_options': 19250000, 
##'from_messages': 108, 'other': 22122, 'from_this_person_to_poi': 30, 'poi': True, 
##'long_term_incentive': 1920000, 'shared_receipt_with_poi': 2042, 'restricted_stock': 6843672, 
##'director_fees': 'NaN'}

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl",'rb'))

## number of names in database
print("Number of names in database:",len(enron_data))

## find number of features per person
print("Number of features per person:",len(enron_data['SKILLING JEFFREY K']))

## number of POIs in database
poicount=0
for person in enron_data:
 if enron_data[person]['poi']==True:
  poicount=poicount+1
print("Number of persons of interest in database:", poicount)

## how much total stock value does James Prentice have?
print("Prentice has $",enron_data['PRENTICE JAMES']['total_stock_value'],"in total stock values")

##how many emails did Wesley Colwell send to POIs?
print("Colwell has",enron_data['COLWELL WESLEY']['from_this_person_to_poi'],"emails to POIs")

##values of stock options exercised by Skilling?
print("Skilling exercised $",enron_data['SKILLING JEFFREY K']['exercised_stock_options'], "in stock options")

##of lay, skilling, and fastow, who took home the most money?
print("Skilling:",enron_data['SKILLING JEFFREY K']['total_payments'],"Lay:",enron_data['LAY KENNETH L']['total_payments'],
"Fastow:",enron_data['FASTOW ANDREW S']['total_payments'])

##how many people have salaries, and how many have a known email address in the list
csalary=0
cemail=0
for person in enron_data:
 if enron_data[person]['salary'] != 'NaN':
  csalary=csalary+1
 if enron_data[person]['email_address'] != 'NaN':
  cemail=cemail+1
print("salaried people:",csalary," people with email:",cemail)



##what percentage of people in the dataset have NaN for total payments?
nopayment=0
for person in enron_data:
 if enron_data[person]['total_payments'] == 'NaN':
  nopayment=nopayment+1
print(nopayment,"or",100*nopayment/len(enron_data),"percent of people do not have a total payments")

#poidict=dict()
poinopay=0
for person in enron_data:
 if enron_data[person]['poi'] ==True:
  #poidict.update(enron_data[person]) makes a dict of just pois if wanted
  if enron_data[person]['total_payments'] == 'NaN':
   poinopay=poinopay+1
   
print(poinopay,"or",100*poinopay/poicount,"percent of POIs have no total payments")   
  
  
## note that if no POIs have missing total payment information, the model may incorrectly latch 
##on to this and classify ANYONE without total payment information as a POI.

