for credencial in (False, True):
    for reserva in (False, True):
        permitido = credencial and reserva
        print(int(credencial), int(reserva), int(permitido))
