
class Person():
    def __init__(self, id, name, first_name, email, phone, address_id=None):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.address_id = address_id

    def set_addres_id(self, address_id):
        self.address_id = address_id

    def get_data(self):
        return {
            'id'            : self.id,
            'name'          : self.name,
            'first_name'    : self.first_name,
            'email'         : self.email,
            'phone'         : self.phone,
            'address_id'    : self.address_id
        }