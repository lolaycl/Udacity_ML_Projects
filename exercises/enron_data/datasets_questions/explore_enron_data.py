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
from __future__ import division  #for 15-29
import pickle


enron_data = pickle.load(open("/Users/Lola/Udacity_ML_Projects/exercises/enron_data/final_project/final_project_dataset.pkl", "r"))

## 15-13        
#print len(enron_data)

## 15-15
#poi_count = []
#for key in enron_data:
#    if enron_data[key]["poi"] is True:
#        poi_count.append(1)
#print len(poi_count)
#print len([ key for key in enron_data if enron_data[key]["poi"] is True])  #in one word

## 15-16
#poi_names = open("/Users/Lola/Udacity_ML_Projects/exercises/enron_data/final_project/poi_names.txt", "r")
#name_count = []
#for name in poi_names:
#    if name[0] is '(':
#        name_count.append(1)
#print len(name_count)

## 15-18 James Prentice
#print enron_data["PRENTICE JAMES"]["total_stock_value"] 

## 15-19 Wesley Colwell
#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] 

## 15-20 Jeffrey K Skilling
#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] 

## 15-25
#data_lay = []
#data_skilling = []
#data_fastow = []
#for name in enron_data:
#    name_split = name.split(" ")
#    if name_split[0] == "LAY":
#        data_lay = enron_data[name]
#    elif name_split[0] == "SKILLING":
#        data_skilling = enron_data[name]
#    elif name_split[0] == "FASTOW":
#        data_fastow = enron_data[name]       
#print "Lay:", data_lay["total_payments"]
#print "Skilling:",data_skilling["total_payments"]
#print "Fastow:", data_fastow["total_payments"]

## 15-27
#folks_salary_count = []
#folks_email_count = []
#for folk in enron_data:
#    if enron_data[folk]["salary"] != 'NaN':
#        folks_salary_count.append(1)
#    if enron_data[folk]["email_address"] != 'NaN':
#        folks_email_count.append(1)
#print len(folks_salary_count)
#print len(folks_email_count)    

## 15-29
#name_nan_count = []
#for name in enron_data:
#    if enron_data[name]["total_payments"] == 'NaN':
#        name_nan_count.append(1)
#    else:
#        name_nan_count.append(0)
#ratio = name_nan_count.count(1)/len(name_nan_count)
#print ratio

## 15-30
#name_poi_count = []
#for name in enron_data:
#    if enron_data[name]["poi"] == True and enron_data[name]["total_payments"] == 'NaN':
#        name_poi_count.append(1)
#    else:
#        name_poi_count.append(0)
#ratio = name_poi_count.count(1)/len(name_poi_count)
#print ratio





    



