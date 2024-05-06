from faker import Faker
fake = Faker()


class Person:
    def __init__(self, first_name, last_name,phone, mail,*args,**kwargs):
           
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail= mail
    
    @property
    def label_length(self):
        self.length=len(self.first_name)+len(self.last_name)    
        return self.length 
        
    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}" 


class BaseContact(Person):
    pass


class BusinessContact(Person):
    def __init__(self,company,work_phone,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.company=company
        self.work_phone=work_phone

    def business_contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}"


if __name__ == "__main__":
    type=input("Please provide type: ") 
    additional=input("Do do want random information?: ")
    if additional=="Yes":
        amount=int(input("Please provide amount: ")) 
    elif additional=="No":
        amount=0


    def create_contacts(type,amount):
        contact_list=[]
        print("\nGenerated output: ")
        if type=="Base_contact":
            for x in range (0,amount):
                first_name=fake.first_name()
                last_name=fake.last_name()
                phone=f"0048{fake.msisdn()}"
                mail=f"{first_name}.{last_name}@{fake.domain_name()}" 

                contact_list.append((first_name,last_name,phone, mail))
            for x in range (0,amount): 
                contact=BaseContact(*contact_list[x]).contact()
                contact_length=BaseContact(*contact_list[x]).label_length
                print(contact,contact_length)
        elif type=="Business_contact":
            for x in range (0,amount):
                company=fake.company()
                work_phone=fake.msisdn()
                first_name=fake.first_name()
                last_name=fake.last_name()
                phone=fake.msisdn()
                position=fake.job()
                mail=f"{first_name}.{last_name}@{fake.domain_name()}" 
            
                contact_list.append((company,work_phone,first_name,last_name,phone, position,mail))
            for x in range (0,amount):    
                contact=BusinessContact(*contact_list[x]).business_contact()
                contact_length=BusinessContact(*contact_list[x]).label_length    
                print(contact,contact_length)


    create_contacts(type,amount)