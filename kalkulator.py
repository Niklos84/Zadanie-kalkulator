import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

choice = int(input("Wybierz działanie wprowadzając odpowiednią liczbę:\n 1 Dodawanie\n 2 Odejmowanie\n 3 Mnożenie\n 4 Dzielenie\n"))
if choice < 1 or choice >4:
    logging.warning("Nie ma takiego działania!")
    exit(1)
first_number = float(input("Wprowadź pierwszą liczbę: "))
second_number = float(input("Wprowadź drugą liczbę: "))
result = 0

if choice == 1:
    add_number = input("Czy chcesz wprowadzić kolejną liczbę? T/N\n")
    additional_numbers = []
    while add_number == 'T':
        new_number = float(input("Wprowadź kolejną liczbę:\n"))
        additional_numbers.append(new_number)
        add_number = input("Czy chcesz wprowadzić kolejną liczbę? T/N\n")

    result = first_number + second_number + sum(additional_numbers)
    logging.info("Dodaję %g, %g, %s" % (first_number, second_number, additional_numbers))
elif choice == 2:
    result = first_number - second_number
    logging.info("Odejmuję %g i %g" % (first_number, second_number))
elif choice == 3:
    result = first_number * second_number
    logging.info("Mnożę %g i %g" % (first_number, second_number))
elif choice == 4:
    result = first_number / second_number
    logging.info("Dzielę %g i %g" % (first_number, second_number))

print(f'Wynik to: {result}')