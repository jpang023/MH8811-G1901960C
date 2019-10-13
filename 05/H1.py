import json
    
def serialize(my_input):
    out_str = ""
    if isinstance(my_input,list):
        out_str = "["
        if not my_input:
            return "[]"
        else:
            for i in my_input:
                if type(i) != str:
                    out_str = out_str + str(i)
                else:
                    out_str = out_str + "'" + str(i) + "'"
                out_str = out_str + ','
            return out_str[:-1]+"]"
    if isinstance(my_input,dict):
        out_str = "{"
        if not my_input:
            return "{}"
        else:
            try:
                for key in my_input:
                    if type(my_input[key]) != str:
                        out_str = out_str + str(key) + ":" + str(my_input[key])
                    else:
                        out_str = out_str + str(key) + ":" + "'"+str(my_input[key])+"'"
                    out_str = out_str + ','
                return out_str[:-1]+"}"
            except:
                return {}

def transdatatype(obj):
    if "'" in obj:
        obj = obj.strip("'")
    else:
        try: 
            obj = int(obj)
        except ValueError: 
            try:
                obj = float(obj)
            except ValueError:
                print("Value Error")
    return obj
                
def data_compare(d1,d2):
    if type(d1) == type(d1):
        if isinstance(d1,list):
            if d1 == d2:
                print("Success!")
            else:
                print("Fail!")
        elif isinstance(d1,dict):
            if d1.keys() == d2.keys():
                allsame = True
                for key in d1:
                    if d1[key] != d2[key]:
                        allsame = False
                if allsame:
                    print("Success!")
                else:
                    print("Fail!")
            else:
                print("Fail!")   
                    
        else:
            print("Wrong data type!")
            
    else:
        print("Fail!")
        
#d1= dict()
#d1['a'] = 1
#d1['b'] = 2
#d2= dict()
#d2['b'] = 2
#d2['a'] = 1
#print(d1)
#print(d2)
#data_compare(d1,d2)
        
def deserialize(input_str):
    
    if "{" in input_str:
        #dict
        input_str=input_str.lstrip('{')
        input_str=input_str.rstrip('}')
        res = dict()
        if not input_str:
            return res
        else:
            if "," in input_str:
                dict_of_str = input_str.split(',')
                for s in dict_of_str:
                    item = s.split(':')
                    item[1] = transdatatype(item[1])
                    res[item[0]] = item[1]
            else:
                print(input_str)
                input_str = input_str.split(':')
                print(input_str)   
                input_str[1] = transdatatype(input_str[1])
                res[input_str[0]] = input_str[1]
            return res
    else:
        #list
        input_str = input_str.lstrip('[')
        input_str = input_str.rstrip(']')
        res = list()
        if not input_str:
            return res
        else:
            if "," in input_str:
                list_str = input_str.split(',')
                for s in list_str:
                    s = transdatatype(s)
                    res.append(s)
            else:
                input_str = transdatatype(input_str)
                res.append(input_str)
            return res
                

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return same
#Ask user for a path to the json file
json_path=input("Please type in file name to load:")

#Use the code from the slide to load the data structure from the json file
try:
    json_file = open(json_path)
    json_data = json.load(json_file) 
    json_file.close()
except:
    print("Wrong file path")
#type(json_data)
#print(json_data)

#Use your serializer to convert the original data structure into a string
try:
    str_data= serialize(json_data)
except:
      print("Wrong JSON data format.")
#print(str_data)

#Write the string to a file (ask user for a file name for that too). Don't forget to close the file.
myfile_path=input("Please type in file name to save:")
#myfile_path="output.txt"
try:
    my_file = open(myfile_path , 'w')  
    my_file.write(str_data)
    my_file.close()
except:
      print("Wrong file path")
#Read the string back from the file. Close the file afterwards.
same_file = open(myfile_path)
my_str= same_file.read()
#print(my_str)

#Pass it to your deserialization function, which would return a restored data structure
new_data = deserialize(my_str)
#print(new_data)

#Compare the two data structures
data_compare(json_data,new_data)
        