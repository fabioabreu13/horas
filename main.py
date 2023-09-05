def horas (minutos):
    episodios = int(input("Quantos episódios são: "))
    minutos = int(input("Qtos minutos são: "))
    tempo_epi = (episodios * minutos)
    horas = tempo_epi / 60
    return "São " + str(horas) + " horas"