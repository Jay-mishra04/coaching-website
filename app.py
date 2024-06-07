import streamlit as st
import datetime
import json

def log_update(data):
    with open("logs.json", "a") as file:
        json.dump(data, file, indent = 4)
        file.write('\n')

def suggestion_logs(datas):
    with open("suggestions.json", "a") as file:
        json.dump(datas, file, indent = 4)
        file.write('\n')

def info():
    st.header("user information page")

    name = st.text_input("Enter your name:")
    phone= st.text_input("Enter your number:")


    if st.button("Submit"):
        if name and phone:
            user_data = {
                'name' : name,
                'phone_number' : phone,
                'date_time' : datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
            }

            log_update(user_data)
            st.success("Information submitted successfully")
        else:
            st.error("something is wrong")


    st.header("this is a suggestion box")
    name = st.text_input("Enter your name")
    class_ = st.text_input("enter your class")
    suggestion = st.text_input("enter your suggestion in full detail:")

    if st.button("submit suggestion"):
        if name and class_ and suggestion:
            suggestion_data = {
                "name" : name,
                "class" : class_,
                "suggestion" : suggestion,
                "datetime"  : datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")     
            }

            suggestion_logs(suggestion_data)
            st.success("Suggestion submitted successfully")
        else:
            print("there is some error")
        
if __name__ == '__main__':
    info()