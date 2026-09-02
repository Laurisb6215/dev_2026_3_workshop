class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).

        Args:
            texto (str): Cadena a verificar

        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        # Normalizamos: quitamos espacios y pasamos todo a minúsculas
        limpio = ""
        for caracter in texto:
            if caracter != " ":
                limpio += caracter.lower()

        # Comparamos carácter por carácter desde los extremos hacia el centro
        izquierda = 0
        derecha = len(limpio) - 1
        while izquierda < derecha:
            if limpio[izquierda] != limpio[derecha]:
                return False
            izquierda += 1
            derecha -= 1
        return True

    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().

        Args:
            texto (str): Cadena a invertir

        Returns:
            str: Cadena invertida
        """
        invertida = ""
        indice = len(texto) - 1
        while indice >= 0:
            invertida += texto[indice]
            indice -= 1
        return invertida

    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.

        Args:
            texto (str): Cadena para contar vocales

        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.

        Args:
            texto (str): Cadena para contar consonantes

        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        contador = 0
        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).

        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena

        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        limpio1 = texto1.replace(" ", "").lower()
        limpio2 = texto2.replace(" ", "").lower()

        if len(limpio1) != len(limpio2):
            return False

        return sorted(limpio1) == sorted(limpio2)

    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.

        Args:
            texto (str): Cadena para contar palabras

        Returns:
            int: Número de palabras en la cadena
        """
        palabras = texto.split()
        return len(palabras)

    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.

        Args:
            texto (str): Cadena

        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        palabras = texto.split(" ")
        resultado = []
        for palabra in palabras:
            if len(palabra) > 0:
                nueva_palabra = palabra[0].upper() + palabra[1:]
                resultado.append(nueva_palabra)
            else:
                resultado.append(palabra)
        return " ".join(resultado)

    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.

        Args:
            texto (str): Cadena con posibles espacios duplicados

        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        espacio_anterior = False
        for caracter in texto:
            if caracter == " ":
                if not espacio_anterior:
                    resultado += caracter
                espacio_anterior = True
            else:
                resultado += caracter
                espacio_anterior = False
        return resultado

    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().

        Args:
            texto (str): Cadena a verificar

        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if len(texto) == 0:
            return False

        digitos = "0123456789"
        inicio = 0

        # Permitimos un signo opcional al inicio
        if texto[0] == "+" or texto[0] == "-":
            inicio = 1
            if len(texto) == 1:
                return False

        for indice in range(inicio, len(texto)):
            if texto[indice] not in digitos:
                return False

        return True

    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.

        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra

        Returns:
            str: Cadena cifrada
        """
        resultado = ""
        desplazamiento = desplazamiento % 26
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
                resultado += nueva_letra
            else:
                resultado += caracter
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.

        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra

        Returns:
            str: Cadena descifrada
        """
        # Descifrar es equivalente a cifrar con el desplazamiento inverso
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().

        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar

        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        len_texto = len(texto)
        len_sub = len(subcadena)

        if len_sub == 0 or len_sub > len_texto:
            return posiciones

        for i in range(len_texto - len_sub + 1):
            coincide = True
            for j in range(len_sub):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break
            if coincide:
                posiciones.append(i)

        return posiciones