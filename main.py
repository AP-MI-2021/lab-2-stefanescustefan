def is_prime(n):
    """
    Determina daca un numar este prim
    :param n: un numar natural
    :return: True daca n este prim, altfel False
    """
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def is_superprime(n):
    """
    Determina daca un numar este superprim

    :param n: un numar natural
    :return: True daca n este superprim, altfel False
    """
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(239) is True
    assert is_superprime(2337) is False
    assert is_superprime(2333) is True


def get_base_2(n):
    """
    Transforma un numar dat in baza 10 in baza 2

    :param n: Un numar natural
    :return: Reprezentarea in baza 2 a numarului n
    """
    x = int(n)
    s = ""
    while x > 0:
        s = str(x % 2) + s
        x = x // 2
    return s


def test_get_base_2():
    assert get_base_2("5") == "101"
    assert get_base_2("12") == "1100"
    assert get_base_2("33") == "100001"
    assert get_base_2("287") == "100011111"


def main():
    test_is_superprime()
    test_get_base_2()
    end = False
    while not end:
        print("1. Verificati daca un numar este superprim")
        print("2. Convertiti un numar din baza 10 in baza 2")
        print("x. Iesire")
        optiune = input()
        if optiune == '1':
            n = int(input("Introduceti un numar natural: "))
            if is_superprime(n):
                print(f"{n} este superprim")
            else:
                print(f"{n} nu este superprim")
        elif optiune == '2':
            n = input("Introduceti un numar natural: ")
            print(f"{n} in baza 2: {get_base_2(n)}")
        elif optiune == 'x':
            end = True
        else:
            print("Optiune gresita")


if __name__ == "__main__":
    main()
