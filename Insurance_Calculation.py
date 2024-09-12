def calculate_insurance(vehicle_value, vehicle_age, owner_age, owner_experience, base_rate=0.02):
    
    if vehicle_age < 3:
        vehicle_factor = 1.0  
    elif 3 <= vehicle_age <= 10:
        vehicle_factor = 0.9  
    else:
        vehicle_factor = 0.8  

    if owner_age < 25:
        age_factor = 1.5  
    elif 25 <= owner_age < 60:
        age_factor = 1.0  
    else:
        age_factor = 1.2  

    if owner_experience < 2:
        experience_factor = 1.4  
    elif 2 <= owner_experience < 10:
        experience_factor = 1.1  
    else:
        experience_factor = 0.9  


    premium = base_rate * vehicle_value * vehicle_factor * age_factor * experience_factor

    return round(premium, 2)
