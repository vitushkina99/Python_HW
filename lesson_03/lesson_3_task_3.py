from lesson_03.Pochta import Address
from lesson_03.Adres import Mailing

to_address = Address('357348', 'Острогорка', 'пер.Школьный', 'д 71', '3')
from_address = Address('303823', 'Норовка', 'улица Кирова', 'д. 92', '6')
cost = "1200"
track = "1234567890"

my_mail = Mailing(to_address, from_address, cost, track)


print(
   f"Отправление {my_mail.track} из {my_mail.from_address.index},"
   f"{my_mail.from_address.city}, {my_mail.from_address.street},"
   f"{my_mail.from_address.home}-{my_mail.from_address.apart}",
   f" в {my_mail.to_address.index}"
   f"  {my_mail.to_address.city}, {my_mail.to_address.street},"
   f"{my_mail.to_address.home}-{my_mail.to_address.apart}",
   f".Стоимость {my_mail.cost} рублей"
     )
