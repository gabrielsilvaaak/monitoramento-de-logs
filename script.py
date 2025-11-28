import os
import csv
import datetime

LOGFILE = "logs_monitoramento.csv"

def registrar_evento(evento, descricao):
    tempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOGFILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([tempo, evento, descricao])

def simular_logs():
    registrar_evento("LOGIN_INVALIDO", "Tentativa de login falhou para o usuário 'admin'.")
    registrar_evento("EXECUCAO_SUSPEITA", "Processo desconhecido tentou executar 'malware.exe'.")
    registrar_evento("MODIFICACAO_ARQUIVO", "Arquivo crítico '/etc/passwd' foi alterado.")

if __name__ == "__main__":
    simular_logs()
    print("Logs gerados com sucesso!")
