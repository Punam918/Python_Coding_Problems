def dataTypeSize(data_type: str) -> int:
    sizes = {
        "Character": 1,  # In C/C++ it's 1 byte, in Java it's 2 bytes (UTF-16), but assuming general case
        "Integer": 4,
        "Long": 8,
        "Float": 4,
        "Double": 8
    }
    
    return sizes.get(data_type, -1)      #If input datatype is invalid then -1
print(dataTypeSize("Character"))  
print(dataTypeSize("Integer"))    
print(dataTypeSize("Long"))       
print(dataTypeSize("Float"))      
print(dataTypeSize("Double"))     
print(dataTypeSize("Boolean"))    
