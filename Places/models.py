from django.db import models
from multiselectfield import MultiSelectField

POWER_TYPES = (
    (0, 'None'),
    (1, 'Limited'),
    (2, 'Good'),
    (3, 'Plenty'),
)
PLACE_TYPES = (
    (0, 'Commercial'),
    (1, 'Private'),
    (2, 'Public'),

)
NOISELEVEL_TYPES = (
    (0, 'Louder'),
    (1, 'Average'),
    (2, 'Quiet'),
)
Amenties_CHOICES = (
    ('1', 'LoungeSeating'),
    ('2', 'Desk'),
    ('3', 'CommunityTables'),
    ('4', 'GroupFriendly'),
    ('5', 'AirConditioner'),
    ('6', 'OutDoorSeating'),
    ('7', 'Pos'),
    ('8', 'NaturalLighting'),
    ('9', 'HasFood'),
    ('10', 'Coffee'),
    ('11', 'EspressoDrink'),
    ('12', 'Tea'),
    ('13', 'JuiceBar'),
    ('14', 'KidFriendly'),
    ('15', 'CarParking'),
    ('16', 'BikeParking'),
)


class Place(models.Model):
    placename = models.CharField(max_length=100, null=True)
    placetype = models.IntegerField(choices=PLACE_TYPES, default=0)
    WiFiSSID = models.CharField(max_length=32, null=True)
    WiFiPassword = models.CharField(max_length=32, null=True)
    power = models.IntegerField(choices=POWER_TYPES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Noiselevel = models.IntegerField(choices=NOISELEVEL_TYPES, null=True)
    Protips = models.CharField(max_length=1000, null=True)
    OpenHour = models.TimeField(null=True)
    CloseHour = models.TimeField(null=True)
    Amenties = MultiSelectField(choices=Amenties_CHOICES, max_choices=16, null=True)

    def __str__(self):
        return str(self.placename)
