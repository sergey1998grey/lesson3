from address import Address
from mailing import Mailing


to_address = Address("127543", "Москва", "Мелиховская", "7", "92")
from_address = Address("187015", "Санкт-Петербург", "Невский проспект", "6", "91")

mailing = Mailing(to_address, from_address, 500, "KON321")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
