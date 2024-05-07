from faker import Faker
fake = Faker()


class Person:
    def __init__(self, first_name, last_name,phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail= mail


    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")    


    @property
    def contact_phone(self):
        return self.phone
    

    def contact(self):
        return (f"Wybieram numer {self.contact_phone} i dzwonię do "
        f"{self.first_name} {self.last_name} {self.label_length}") 


    def __repr__(self):
        print( f"{self.first_name} {self.last_name}")


class BaseContact(Person):
    pass


class BusinessContact(Person):
    def __init__(self, first_name, last_name,phone, mail,company, work_phone):
        super().__init__(first_name, last_name,phone, mail)
        self.company=company
        self.work_phone=work_phone


    @property
    def contact_phone(self):
        return self.work_phone


def create_contacts(type, amount):
    contact_list=[]
    for i in range(amount):
        first_name = fake.first_name()

        last_name=fake.last_name()

        phone=f"0048{fake.msisdn()}"

        work_phone=fake.msisdn()

        mail=f"{first_name}.{last_name}@{fake.domain_name()}" 

        company=fake.company()

        work_phone=fake.msisdn()

        if type == "base":

            contact = BaseContact(

            first_name=first_name,

            last_name=last_name,

            phone=phone,

            mail=mail,
            ).contact()

        elif type == "business":

            contact = BusinessContact(

            first_name=first_name,

            last_name=last_name,

            phone=phone,

            mail=mail,

            company=company,

            work_phone=work_phone

            ).contact()

        contact_list.append(contact)


    return contact_list


if __name__ == "__main__":
    type=input("Please provide the type of contact: ")
    amount=input("Please provide the desired amount: ")

    
    print(create_contacts(type, int(amount)))