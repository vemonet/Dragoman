import re
import csv
import sys
import os
import pandas as pd

global global_dic
global_dic = {}
global functions_pool

#####################################################################################################
########### ADD THE IMPLEMENTATION OF YOUR FUNCTIONS HERE FOLLOWING THE EXAMPLES ####################
#####################################################################################################

## For each new function that you define, add an entry as "function_name":"" to the dictionary below 
functions_pool = {"tolower":"","chomp":"","process_string":""}


## Define your functions here following examples below, the column "names" from the csv files 
## that you aim to use as the input parameters of functions are only required to be provided 
## as the keys of "global_dic"
def tolower(): 
    return global_dic["value"].lower()

def chomp():
    return global_dic["value"].replace(global_dic["toremove"], '')


def split_string():
    return global_dic["value"].split(global_dic["split"])

def process_string():
    s = None
    if "input" in global_dic.keys():
        s = global_dic["input"]
    split = None
    if "split_on" in global_dic.keys():
        split = global_dic["split_on"]
    prefix = None
    if "add_prefix" in global_dic.keys():
        prefix = global_dic["add_prefix"]
    find = None
    if "find" in global_dic.keys():
        find = global_dic["find"]
    replace = None
    if "replace" in global_dic.keys():
        replace = global_dic["replace"]
    format = None
    if "format_for" in global_dic.keys():
        format = global_dic["format_for"]

    if not s:
        return None
    
    resultList = []
    if split:
        resultList = s.split(split)
    else:
        resultList.append(s)
    
    if prefix or replace or format:
        for i in resultList:
            if format and format.lower() == "uri":
                resultList[i] = resultList[i].replace(" ", "-").replace(",", "-").replace(".", "-").lower();
            if format and format.lower() == "lowercase":
                resultList[i] = resultList[i].toLowerCase()

            if format and format.lower() == "uppercase":
                resultList[i] = resultList[i].upper()

            if prefix:
                resultList[i] = prefix + resultList[i];
            
            if find and replace:
                # resultList[i] = resultList[i].replaceAll(find, replace);
                regex = re.compile(find)
                resultList[i] = re.sub(regex, replace, resultList[i])

    return resultList


    # return global_dic["value"].replace(global_dic["toremove"], '')


################################################################################################
############################ Static (Do NOT change this code) ##################################
################################################################################################

def execute_function(row,header,dic):
    func = dic["function"].split("/")[len(dic["function"].split("/"))-1]
    if func in functions_pool:
        global global_dic
        global_dic = execution_dic(row,header,dic)
        return eval(func + "()")             
    else:
        print("Invalid function")
        print("Aborting...")
        sys.exit(1)

def execution_dic(row,header,dic):
    output = {}
    for inputs in dic["inputs"]:
        if "constant" not in inputs: 
            if isinstance(row,dict):
                output[inputs[2]] = row[inputs[0]]
            elif isinstance(global_row,list):
                output[inputs[2]] = row[header.index(global_dic["func_par"][inputs[2]])]
        else:
            output[inputs[2]] = inputs[0]
    return output
