import sys


def linhaSimples(a):
    for b in range(a):
        sys.stdout.write("-")
    sys.stdout.write("\n")


def linhaDupla(c):
    for d in range(c):
        sys.stdout.write("=")
    sys.stdout.write("\n")


def linha(e, f):
    for g in range(f):
        sys.stdout.write(e)
    sys.stdout.write("\n")