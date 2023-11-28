class Doctor():
    
    def __init__(self):
        print("This is class Doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is "+str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart rate is normal")
        else:
            print("Your heart rate does not seem normal, please visit the clinc")
            
    
class Paitent(Doctor):
    
    def __init__(self, name, weight, height, heart_rates):
        self.paitent_name = name
        self.paitent_weight = weight
        self.paitent_height = height
        self.paitent_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Paitent Name: ", self.paitent_name)
        Doctor.BMI(self.paitent_weight, self.paitent_height)
        Doctor.heart_rate(self.paitent_heart_rates)
        
        
paitent1 = Paitent("Michael", 30, 0.9144, 80)
paitent1.healthCheck()

paitent2 = Paitent("Jessica", 40, 1, 120)
paitent2.healthCheck()