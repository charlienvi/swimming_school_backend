class Address:
    def __init__(self, id, street, housenumber, zipcode, city, person_id=None):
        self.id             = id
        self.person_id      = person_id
        self.street         = street
        self.housenumber    = housenumber
        self.zipcode        = zipcode
        self.city           = city

    def set_person_id(self, person_id):
        self.person_id = person_id
    
    def get_data(self):
        return {
            'id'            : self.id,
            'person_id'     : self.person_id,
            'street'        : self.street,
            'housenumber'   : self.housenumber,
            'zipcode'       : self.zipcode,
            'city'          : self.city
        }

    