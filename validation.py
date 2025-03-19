import re

class ValidationError(Exception):
    pass

def validate_data(data_dict):
    validated_data = {}  
    errors = [] 
    
    for k, v in data_dict.items():
        if k.endswith("fname"):
            pattern = r'^[A-Z]{1}[a-z]{2,}$'
            if not re.fullmatch(pattern, v):
                errors.append("First Name should start with a capital letter and have at least 3 characters")
            else:
                validated_data[k] = v
        elif k.endswith("lname"):
            pattern = r'^[A-Z]{1}[a-z]{2,}$'
            if not re.fullmatch(pattern, v):
                errors.append("Last Name should start with a capital letter and have at least 3 characters")
            else:
                validated_data[k] = v
        elif k.endswith("address"):
            pattern = r'^.{3,100}$'  # Allows all characters (min 3, max 100)
            if not re.fullmatch(pattern, v):
                errors.append("Address should be between 3 to 100 characters")
            else:
                validated_data[k] = v
        elif k.endswith("city"):
            pattern = r'^[A-Z]{1}[a-z]{2,}$'
            if not re.fullmatch(pattern, v):
                errors.append("City Name should start with a capital letter and have at least 3 characters")
            else:
                validated_data[k] = v
        elif k.endswith("state"):
            pattern = r'^[A-Z]{1}[a-z]{2,}$'
            if not re.fullmatch(pattern, v):
                errors.append("State Name should start with a capital letter and have at least 3 characters")
            else:
                validated_data[k] = v
        elif k.endswith("zip"):
            pattern = r'^[1-9]{1}[0-9]{5}$'
            if not re.fullmatch(pattern, v):
                errors.append("Zip should be a 6-digit number and should not start with 0")
            else:
                validated_data[k] = v
        elif k.endswith("phonenum"):
            pattern = r'^[1-9]{1}[0-9]{9}$'
            if not re.fullmatch(pattern, v):
                errors.append("Phone Number should be a 10-digit number and should not start with 0")
            else:
                validated_data[k] = v
        elif k.endswith("email"):
            pattern = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
            if not re.fullmatch(pattern, v):
                errors.append("Email is not in the correct format")
            else:
                validated_data[k] = v

    return validated_data, errors  

def validation_wrapper(func):
    def inner(data_dict):
        validated_data, errors = validate_data(data_dict)
        
        if errors:
            print("\nValidation Errors:")
            for error in errors:
                print(" -", error)
            return None 
        
        return func(validated_data)  
    return inner

@validation_wrapper
def validate_user_data(data_dict):
    print("Data is valid")
    return data_dict
