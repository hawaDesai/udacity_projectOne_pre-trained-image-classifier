#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hawa Desai
# DATE CREATED:    4 March 2023                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
# Imports only listdir function from OS module 
from os import listdir  



# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
        
    """
    # Retrieve the filenames from folder pet_images/
    results_dic = {} #creates a dictionary of files and their labels
    
    file_list = listdir(image_dir) #creates a list of filename
    
    label_list = []
    
    #for loop that runs through each file name in the file list and
    #creates a label for each name
    for filename in file_list:
        low_split_label = filename.lower().split('_') #local variable that lowers and splits filename by "-"
  
        label = " " #create local variable to hold finalized label data
        
        #creates a for loop that runs throught the low_split_label list created by splitting the variables
        for final_split in low_split_label:
             #sets up if statement that checks each value of final_split and adds all
             #alphabetic characters into the final label, adding spaces in between word
           if final_split.isalpha():
            #creates label with name of animal in filename with a space in between
            label += final_split + " "
                
         
        label_list.append(label.strip())#strips extra characters from finalized label and appends to label list
        
        if filename not in results_dic:
            results_dic[filename] = label_list #adds filename as key and label_list as value
        else:
            print("File already exists in list!")
        
        label_list = []#reassigns label_list to empty list
        
    '''
    filename_list = listdir("pet_images/")
    results_dic = dict()
    final_name = ""
    pre_check = {}
    list_make = []
    y = 0
    
    
    for i in filename_list:
        name_breakdown  = i.lower()
        final_name_breakdown = name_breakdown.split("_")
        for name in final_name_breakdown:
            if name.isalpha():
                final_name += name + " "
        
        final_name = final_name.strip()
        
        if final_name not in list_make:
            list_make.append(final_name)
            results_dic[i] = final_name
            final_name = ""
        else:
            final_name = ""
    
    # Replace None with the results_dic dictionary that you created with this
    # function'''
    return results_dic
