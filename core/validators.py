import re
import unicodedata
from datetime import datetime, date

from models.cita import TIPOS_ATENCION, PRIORIDADES

FORMATO_FECHA = "%d/%m/%Y"


def _error(mensaje: str) -> None:
    print(f"  ⚠ {mensaje}")


def _norm(texto: str) -> str:
    return unicodedata.normalize(
        "NFKD", texto.strip().lower()
    ).encode("ascii", "ignore").decode()


def _pedir_hasta_valido(prompt: str, validador):
    while True:
        try:
            entrada = input(prompt).strip()
        except EOFError:
            print()
            raise SystemExit
        try:
            return validador(entrada)
        except ValueError as e:
            _error(str(e))


def validar_nombre(texto: str) -> str:
    if len(texto) < 3 or not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", texto):
        raise ValueError("Nombre inválido: mínimo 3 letras, sin números ni símbolos.")
    return texto


def validar_cedula(texto: str) -> str:
    if not texto.isdigit() or not (7 <= len(texto) <= 10):
        raise ValueError("Cédula inválida: solo números, entre 7 y 10 dígitos.")
    return texto


def validar_tipo(texto: str) -> str:
    for t in TIPOS_ATENCION:
        if _norm(t) == _norm(texto):
            return t
    raise ValueError(f"Tipo inválido. Opciones: {', '.join(TIPOS_ATENCION)}")


def validar_prioridad(texto: str) -> str:
    for p in PRIORIDADES:
        if _norm(p) == _norm(texto):
            return p
    raise ValueError(f"Prioridad inválida. Opciones: {', '.join(PRIORIDADES)}")


def validar_fecha(texto: str) -> date:
    try:
        return datetime.strptime(texto, FORMATO_FECHA).date()
    except ValueError:
        raise ValueError("Fecha inválida. Use formato DD/MM/AAAA.")


def validar_cantidad(texto: str) -> int:
    if not texto.isdigit() or not (1 <= int(texto) <= 32):
        raise ValueError("Cantidad inválida: entero entre 1 y 32.")
    return int(texto)


def validar_opcion_menu(texto: str, opciones: range) -> int:
    if not texto.isdigit() or int(texto) not in opciones:
        raise ValueError(f"Opción inválida. Elija entre {opciones.start} y {opciones.stop - 1}.")
    return int(texto)


def validar_si_no(texto: str) -> str:
    t = texto.strip().lower()
    if t not in ("s", "n"):
        raise ValueError("Respuesta inválida. Escriba 's' o 'n'.")
    return t


def pedir_nombre() -> str:
    return _pedir_hasta_valido("Nombre del cliente: ", validar_nombre)


def pedir_cedula() -> str:
    return _pedir_hasta_valido("Cédula: ", validar_cedula)


def pedir_tipo() -> str:
    print(f"Tipos: {', '.join(TIPOS_ATENCION)}")
    return _pedir_hasta_valido("Tipo de atención: ", validar_tipo)


def pedir_prioridad() -> str:
    print(f"Prioridades: {', '.join(PRIORIDADES)}")
    return _pedir_hasta_valido("Prioridad: ", validar_prioridad)


def pedir_fecha() -> date:
    return _pedir_hasta_valido("Fecha (DD/MM/AAAA): ", validar_fecha)


def pedir_cantidad() -> int:
    return _pedir_hasta_valido("Cantidad de piezas: ", validar_cantidad)


def pedir_opcion_menu(maximo: int) -> int:
    return _pedir_hasta_valido(f"Opción (0-{maximo}): ",
                               lambda s: validar_opcion_menu(s, range(0, maximo + 1)))


def pedir_si_no(prompt: str) -> str:
    return _pedir_hasta_valido(prompt + " (s/n): ", validar_si_no)
