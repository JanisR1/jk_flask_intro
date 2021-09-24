FILE_NAME = "dati.txt"

def pievienotVardu(vards):
    f = open(FILE_NAME, "a", encoding="utf-8")
    f.write(vards + "\n")
    f.close()

def pievienotUzvardu(uzvards):
    f = open(FILE_NAME, "a", encoding="utf-8")
    f.write(uzvards + "\n")
    f.close()

def pievienotEpastu(epasts):
    f = open(FILE_NAME, "a", encoding="utf-8")
    f.write(epasts + "\n")
    f.close()

def pievienotZinojumu(zinojums):
    f = open(FILE_NAME, "a", encoding="utf-8")
    f.write(zinojums + "\n")
    f.close()

def lasitDatus():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        ieraksti = f.readlines()

    return ieraksti