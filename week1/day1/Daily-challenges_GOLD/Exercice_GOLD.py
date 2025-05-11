birthdate = input("Enter your birthdate (DD/MM/YYYY): ")


year = int(birthdate[-4:])


current_year = 2025


age = current_year - year


candles = age % 10


print()
print("    ___" + "i" * candles + "___")
print("     |:H:a:p:p:y:|")
print("   __|___________|__")
print("  |^^^^^^^^^^^^^^^^^|")
print("  |:B:i:r:t:h:d:a:y:|")
print("  |                 |")
print("  ~~~~~~~~~~~~~~~~~~~")

