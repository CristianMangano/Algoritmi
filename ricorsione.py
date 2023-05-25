def cronometro(tempo):
    if tempo > 0:
        print(tempo)
        return cronometro(tempo - 1)
    if tempo == 0:
        return 'via!'

conto_alla_rovescia = cronometro(10)
print(id(conto_alla_rovescia))

conto_alla_rovescia = conto_alla_rovescia.upper()
print(id(conto_alla_rovescia))

conto_alla_rovescia = conto_alla_rovescia[0] + 'ia!'
print(id(conto_alla_rovescia))

print(conto_alla_rovescia)
