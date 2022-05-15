from csv import reader
import requests

with open("data.csv", "r") as my_file:
    
    file_reader = reader(my_file)
    
    ans = []
    for i in file_reader:
        ans.append(i)
    
    print("procressing...")
    
    
    ##  THE THING THAT THE PLAYERS WILL MOST LIKEY CODE  ##
    for i in ans[1:10]:
        url = 'http://127.0.0.1:8000/get/'
        data = {
            'email': i[0], #6 for posting data
            'password' : i[1],
            #'first_name' : i[1],
            #'last_name' : i[2],
            #'phone' : i[3],
            #'bio' : i[5],
            #'verification_question' : i[8],
            #'date_of_birth' : i[4]
        }
        x = requests.get(url, params = data)
        print(x.text)
    print("Complete!")
