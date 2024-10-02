import json # dictionaryJson - We can use json module to convert dictionary to json and json to 
# Files are typically plain text, so Python objects like dictionaries need to be converted into a string format that can be stored. JSON is a lightweight data format that is easy to write and read back from files.

user_choice = input("Do you want to login or register ").lower()

def register():
    print("Registration")
    user_username= input("Username: ")
    user_password= input("Password: ")
    
    user_dict = {user_username: user_password}
    
    try:
        # opeing in a reading mode for just adding comma later if there is no content then we don't need to add comma
       with open("login.txt", "r") as f:
            existing_data = f.read()
            # data cha vane split into list
            if existing_data:
                existing_data_list = existing_data.split("|")
            #empty cha vane list initialize gairakhne so that append part ma comma wala handle garxa as 0>0 false so no comma will be added
            else:
                existing_data_list = []
    #file vetena vane error ma janxa ani initialize garera ani tala append part ma new file create garxa ani initailization compare garxa           
    except FileNotFoundError:
        # print("File not found. Creating new file ")
        existing_data_list = []

    with open("login.txt", "a") as f:
        user_data_json = json.dumps(user_dict) #transform a dictionary into a string format that can be easily written to a file.
        if len(existing_data_list) > 0:
            f.write("|")  # Append comma only if the file has data
        f.write(user_data_json)
    
    print("Registration successful!")
    ask = input("Do you want to login?(y/n) ").lower()
    if ask =='y':
        login()
    

def login():        

    user_username = input("Username: ")
    user_password = input("Password: ")
    try:
        with open("login.txt","r") as f:
            user_data = f.read()
            if not user_data:
                print("No registered users found!")
                
                ask = input("Do you want to register?(y/n) ").lower()
                if ask =='y':
                    register()
                else:
                    return
                
    except FileNotFoundError:
        print("Error! File not found")   
        return
    
    user_data_list= user_data.split("|")
    
    for i in user_data_list:
        if i: #value cha ki nai checking to avoid empty i
            try:
                user_dict_data = json.loads(i) # Converts a JSON string back into a Python object (like a dictionary or list).
                if user_username in user_dict_data and user_password == user_dict_data[user_username]:
                    print('Login Successfull')
                    return
            except json.JSONDecodeError:
                continue
    print("Login failed! Invalid username or password. Try again")
    login()
        
if user_choice == "register":  
    register()
    
elif user_choice =="login":
    login()
else:
    print("You can only login or register here. ")