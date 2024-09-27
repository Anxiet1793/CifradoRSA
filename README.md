# Implementación de RSA en Python desde Cero

Este proyecto es una implementación simple del algoritmo de cifrado **RSA** en Python, sin el uso de librerías externas. El código genera claves públicas y privadas, y permite cifrar y descifrar mensajes.

## Características

- **Generación de claves RSA** (clave pública y privada) usando números primos grandes.
- **Cifrado** de mensajes utilizando la clave pública.
- **Descifrado** de mensajes cifrados utilizando la clave privada.
- Verificación de números primos usando el **Test de Primalidad de Fermat**.
- Generación de primos de tamaño variable, especificados por el usuario.

## Cómo Funciona

El algoritmo RSA funciona en tres etapas principales:

1. **Generación de claves**:
   - Selecciona dos números primos grandes, \( p \) y \( q \).
   - Calcula \( n = p \times q \) y la función totiente \( \phi(n) = (p-1) \times (q-1) \).
   - Selecciona un número \( e \) que sea coprimo con \( \phi(n) \), el cual será la clave pública.
   - Calcula el inverso modular de \( e \), llamado \( d \), que será la clave privada.

2. **Cifrado**:
   - El mensaje se cifra utilizando la clave pública \( (e, n) \) mediante la fórmula:
     \[
     C = M^e \mod n
     \]
     Donde \( M \) es el mensaje original, y \( C \) es el mensaje cifrado.

3. **Descifrado**:
   - El mensaje cifrado se descifra utilizando la clave privada \( (d, n) \) mediante la fórmula:
     \[
     M = C^d \mod n
     \]
     Donde \( M \) es el mensaje descifrado.

## Ejemplo de Uso

```python
import random

# Crear una instancia de RSA con claves de 2048 bits
rsa = RSA(bits=2048)

# Mensaje original
mensaje = "Hello World"

# Cifrar el mensaje
mensajeCifrado = rsa.cifrar(mensaje)
print(f"Mensaje cifrado: {mensajeCifrado}")

# Descifrar el mensaje
mensajeDescifrado = rsa.descifrar(mensajeCifrado)
print(f"Mensaje descifrado: {mensajeDescifrado}")
