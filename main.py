import phonenumbers
from phonenumbers import geocoder
myPhoneNo = phonenumbers.parse("+1")

from phonenumbers import carrier

print(geocoder.description_for_number(myPhoneNo, 'en'))

print(carrier.name_of_number(myPhoneNo, 'en'))
