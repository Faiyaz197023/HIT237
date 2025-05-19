# pest_model.py

# This is our Pest class, which is like a blueprint for creating pest objects.
class Pest:
    def __init__(self, key, name, scientific_name, affects, image, description='', life_cycle=''):

        self.key = key
        self.name = name
        self.scientific_name = scientific_name
        self.affects = affects
        self.image = image
        self.description = description
        self.life_cycle = life_cycle

    @classmethod 
    #Why I used Classmethod ? because I wanted to combine both the pest_data and pest_description data. Classmethod helps me to change the attributes of a class itself not the object so that I don't create new instances
    
    def from_data(cls, data, description_data):
        pest_description = {}
        
       
        for description in description_data:
            if description['key'] == data['key']: 
                pest_description = description
                break  
        
        return cls(
            key=data['key'], 
            name=data['name'], 
            scientific_name=data['scientific_name'], 
            affects=data['affects'],  
            image=data['image'], 
            description=pest_description.get('description', ''),  
            life_cycle=pest_description.get('life_cycle', '') 
        )


class Protect_Against_Pest(Pest):
    def __init__(self, key, name, scientific_name, affects, image, description='', life_cycle='', 
                 controlling_strategies='', monitoring=''):
        super().__init__(key, name, scientific_name, affects, image, description, life_cycle)
        self.controlling_strategies = controlling_strategies
        self.monitoring = monitoring

    @classmethod
    def from_protect_data(cls, pest_data, description_data, protect_data):
        pest = cls.from_data(pest_data, description_data)
        
        protection_info = {}
        for protect in protect_data:
            if protect['key'] == pest_data['key']:
                protection_info = protect
                break
        
        return cls(
            key=pest.key,
            name=pest.name,
            scientific_name=pest.scientific_name,
            affects=pest.affects,
            image=pest.image,
            description=pest.description,
            life_cycle=pest.life_cycle,
            controlling_strategies=protection_info.get('controlling_strategies', ''),
            monitoring=protection_info.get('monitoring', '')
        )

        

class Organism:
    def __init__(self, key, name, scientific_name, affects, image):
        self._key = key
        self._name = name
        self._scientific_name = scientific_name
        self._affects = affects
        self._image = image

    def get_summary(self):
        return f"{self._name} affects {self._affects}."

class Disease(Organism):
    def __init__(self, key, name, scientific_name, affects, image, type, description, life_cycle, gallery=None):
        super().__init__(key, name, scientific_name, affects, image)
        self._type = type
        self._description = description
        self._life_cycle = life_cycle
        self._gallery = gallery or []

    def get_summary(self):
        return f"{self._name} ({self._type}) affects {self._affects} and is caused by {self._scientific_name}."

    def get_gallery(self):
        return self._gallery
<<<<<<< HEAD


class Protect_Against_Diseases:
    def __init__(self, key, name, measure, image):
        self._key = key
        self._name = name
        self._measure = measure
        self._image = image

    @classmethod
    def from_disease_prot_data(cls, data, disease_protection_description):
        protection_info = {}

        for description in disease_protection_description:
            if description['key'] == data['key']:
                protection_info = description
                break

        return cls(
            key=data['key'],
            name=data['name'],
            measure=protection_info.get('measure', ''),
            image=data['image']
        )



    

=======
    
class Diseases_Protection:
    def __init__(self, key, name, scientific_name, affects, description, controlling_strategies, monitoring):
        self.key = key
        self.name = name
        self.scientific_name = scientific_name
        self.affects = affects
        self.description = description
        self.controlling_strategies = controlling_strategies
        self.monitoring = monitoring

    @classmethod
    def from_data(cls, data, detail_data, protection_data):
        # Get the matching disease detail
        detail = next((d for d in detail_data if d['key'] == data['key']), {})
        # Get the matching protection data
        protection = next((p for p in protection_data if p['key'] == data['key']), {})

        return cls(
            key=data.get('key'),
            name=data.get('name'),
            scientific_name=data.get('scientific_name', ''),
            affects=data.get('affects', ''),
            description=detail.get('description', ''),
            controlling_strategies=protection.get('controlling_strategies', ''),
            monitoring=protection.get('monitoring', '')
        )


class Protect_Against_Diseases:
    def __init__(self, key, name, scientific_name, affects, description, controlling_strategies, monitoring):
        self.key = key
        self.name = name
        self.scientific_name = scientific_name
        self.affects = affects
        self.description = description
        self.controlling_strategies = controlling_strategies
        self.monitoring = monitoring

    @classmethod
    def from_disease_prot_data(cls, disease_data, disease_description, protection_detail):
        description_data = next((d for d in disease_description if d['key'] == disease_data['key']), {})
        protection_data = next((p for p in protection_detail if p['key'] == disease_data['key']), {})

        return cls(
            key=disease_data['key'],
            name=disease_data.get('name', ''),
            scientific_name=disease_data.get('scientific_name', ''),
            affects=disease_data.get('affects', ''),
            description=description_data.get('description', ''),
            controlling_strategies=protection_data.get('controlling_strategies', ''),
            monitoring=protection_data.get('monitoring', '')
        )
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
