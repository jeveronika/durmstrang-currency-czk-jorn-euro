# jeden jorn má 33 vikýřů
# jeden jorn je 15 norských korun
# jeden jorn je 1.5 centů
# jeden jorn je 38.5 korun

################# ZÁKLADNÍ KÓD BEZ ZJEDNODUŠENÍ:

# j = 0
# czk = 0
# eur = 0

# currency_input = input("Napište, kterou měnu chcete převést. Pro jorny napište 'j', pro české koruny napište 'czk' pro eura napište 'eur': ").lower()
# currency_output = input(f"Napište, na kterou měnu chcete převést. Pro jorny napište 'j', pro české koruny napište 'czk' pro eura napište 'eur': ").lower()
# currency_amount = float(input("Kolik chcete převést: "))

# if currency_amount < 0.0:
#     print(f"Pokud nemáte žádné peníze, tak co chcete převádět?")

# elif currency_input == "j" and currency_output == "czk":
#     j += currency_amount
#     czk = "{:.2f}".format(j * 38.5)
#     print(f"Právě máte v kapse {j} jornů, což je {czk} českých korun.")

# elif currency_input == "j" and currency_output == "eur":
#     j += currency_amount
#     eur = "{:.2f}".format(j * 1.5)
#     print(f"Právě máte v kapse {j} jornů, což je {eur} euro.")

# elif currency_input == "czk" and currency_output == "j":
#     czk += currency_amount
#     j = "{:.2f}".format(currency_amount / 38.5)
#     print(f"Právě máte v kapse {czk} českých korun, což je {j} jornů.")

# elif currency_input == "eur" and currency_output == "j":
#     eur += currency_amount
#     j = "{:.2f}".format(currency_amount / 1.5)
#     print(f"Právě máte v kapse {eur} eur, což je {j} jornů.")



################# KÓD SE ZJEDNODUŠENÍM POMOCÍ SLOVNÍKU:

exchange_rates = {
    'j': {'czk': 38.5, 'eur': 1.5},
    'czk': {'j': 1 / 38.5},
    'eur': {'j': 1 / 1.5}
}
currency_input = input("Napište, kterou měnu chcete převést. Pro jorny napište 'j', pro české koruny napište 'czk' pro eura napište 'eur': ").lower()
currency_output = input(f"Napište, na kterou měnu chcete převést. Pro jorny napište 'j', pro české koruny napište 'czk' pro eura napište 'eur': ").lower()
currency_amount = float(input("Kolik chcete převést: "))

if currency_amount < 0.0:
    print(f"Pokud nemáte žádné peníze, tak co chcete převádět?")
else:
    converted_amount = "{:.2f}".format(currency_amount * exchange_rates[currency_input][currency_output])
    print(f"Právě máte {currency_amount} {currency_input}, což je {converted_amount} {currency_output}.")
