from .models import donors
from table import Table
from table.columns import Column

class donorsTable(Table):
    name = Column(field='name')
    email = Column(field='email')
    mob_no = Column(field='mob_no')
    age = Column(field='age')
    blood_group = Column(field='blood_group')
    city = Column(field='city')
    gender = Column(field='gender')
    
    class Meta:
        model = donors

