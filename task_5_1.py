from faker import Faker
fake = Faker()


information=[("Christopher", "Johnson", "0048874242820", "Accommodation manager", 
              "Christopher.Johnson@reed.com","YHA","004875823"),
   ("Jessica", "Owens", "0048346627631", "Garment/textile technologist", 
    "Jessica.Owens@miller-torres.com","NTT","004824659"),
   ("Martin", "Moran", "0048470878121", "Ship broker", 
    "Martin.Moran@hart.info","SSY","004827594"),
   ("Stacey", "Brooks", "0048527429145", "Actuary", 
    "Stacey.Brooks@jensen.com","Aon","004869502"),
   ("Ryan","Bryant", "0048336715828", "surveyor",
     "Ryan.Bryant@scott.com","Insightica","004857531")]


type=input("Please provide type: ") 
additional=input("Do do want random information?: ")
if additional=="Yes":
    amount=int(input("Please provide amount: ")) 
elif additional=="No":
    amount=0

class personal_data:
   def __init__(self, first_name, last_name,phone, mail,*args,**kwargs):
           
           self.first_name = first_name
           self.last_name = last_name
           self.phone = phone
           self.mail= mail

   def contact(self):
       return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"
   @property
   def label_length(self):
       return f"Długość {self.first_name} {self.last_name}= {len(self.first_name)+len(self.last_name)}"
   

class BaseContact(personal_data):
   def __init__(self, *args,**kwargs):
       super().__init__(*args,**kwargs)


class BusinessContact(personal_data):
    def __init__(self,company,work_phone,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.company=company
       self.work_phone=work_phone

    def business_contact(self):
       return f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}"





def get_length_from_list(func):
   def wrapper(self):
       func(type)
       for x in range (0,len(information)):
           length=BaseContact(*information[x])
           length=length.label_length
           print(length)
   return wrapper
@get_length_from_list
def get_information_from_list(type):

    for x in range (0,len(information)):  
        if type=="Business_contact":
            business_contact=BusinessContact(first_name=information[x][0],last_name=information[x][1],
                                             phone=information[x][2],position=information[x][3],
                                             mail=information[x][4],company=information[x][5],
                                             work_phone=information[x][6]).business_contact()
            print(business_contact)
        elif type=="Base_contact":
             base_contact=BaseContact(first_name=information[x][0],last_name=information[x][1],
                                      phone=information[x][2],mail=information[x][4]).contact()
             print(base_contact)


get_information_from_list(type)


def create_contacts(type,amount):
    contact_list=[]
    if type=="Base_contact":
        for x in range (0,amount):
            first_name=fake.first_name()
            last_name=fake.last_name()
            phone=fake.msisdn()
            mail=f"{first_name}.{last_name}@{fake.domain_name()}" 
            contact_list.append((first_name,last_name,phone, mail))
        return contact_list
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
        return contact_list


generated_list=create_contacts(type,amount)
  

def get_additional_length(func):
   def wrapper(self):
       func(type)
       for x in range (0,len(generated_list)):
           if type=="Business_contact":
               length=BusinessContact(*generated_list[x])
               length=length.label_length
           elif type=="Base_contact":
               length=BaseContact(*generated_list[x])
               length=length.label_length
           print(length)
   return wrapper


@get_additional_length
def get_contact(type):
    print("\nGenerated output: ")
    for x in range (0,len(generated_list)):
        if type=="Business_contact":
            contact=BusinessContact(*generated_list[x]).business_contact()
        elif type=="Base_contact":
            contact=BaseContact(*generated_list[x]).contact()
        print(contact)


get_contact(type)



