import random

class RSA:
    def __init__(self, bits):
        self.bits = bits
        self.clavePublica, self.clavePrivada = self.generarClaves()

    def generarClaves(self):
        p = self.obtenerNumeroPrimo(self.bits)
        q = self.obtenerNumeroPrimo(self.bits)
        n = p * q
        totient = (p - 1) * (q - 1)

        e = self.obtenerClavePublica(totient)
        d = self.inversoMultiplicativo(e, totient)

        clavePublica = (e, n)
        clavePrivada = (d, n)

        return clavePublica, clavePrivada

    def cifrar(self, mensaje):
        e, n = self.clavePublica
        mensajeCifrado = [pow(ord(char), e, n) for char in mensaje]
        return mensajeCifrado

    def descifrar(self, mensajeCifrado):
        d, n = self.clavePrivada
        mensajeDescifrado = [chr(pow(char, d, n)) for char in mensajeCifrado]
        return ''.join(mensajeDescifrado)

    def obtenerNumeroPrimo(self, bits):
        numero = random.getrandbits(bits)
        while not self.esPrimo(numero):
            numero = random.getrandbits(bits)
        return numero

    def obtenerClavePublica(self, totient):
        e = random.randint(2, totient - 1)
        while self.mcd(e, totient) != 1:
            e = random.randint(2, totient - 1)
        return e

    def inversoMultiplicativo(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def esPrimo(self, numero, precision=5):
        if numero < 2:
            return False
        for _ in range(precision):
            a = random.randint(2, numero - 1)
            if pow(a, numero - 1, numero) != 1:
                return False
        return True


# Ejemplo de uso
rsa = RSA(bits=2048 )
mensaje = "hello world"

mensajeCifrado = rsa.cifrar(mensaje)
mensajeDescifrado = rsa.descifrar(mensajeCifrado)

print(f'Mensaje original: {mensaje}')
print(f'Mensaje cifrado: {mensajeCifrado}')
print(f'Mensaje descifrado: {mensajeDescifrado}')
