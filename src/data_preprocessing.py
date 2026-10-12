import pandas as pd
from datasets import Dataset

def load_ticket_dataset():
    """
    Carga el dataset de tickets de soporte bancario para los modelos de Hugging Face.
    """
    data = {
        "text": [
            "Mi transferencia SPEI no se refleja en la cuenta destino desde hace dos horas.",
            "Excelente atención por parte del asesor en sucursal, resolvieron mi duda rápido.",
            "Quiero consultar los requisitos para solicitar un crédito hipotecario tradicional.",
            "¡Ayuda! Detecté un cargo no reconocido en mi tarjeta de crédito hace unos minutos.",
            "El cajero automático no me entregó el dinero pero el saldo ya fue descontado.",
            "Gracias por la pronta respuesta a mi aclaración de comisiones bancarias.",
            "No puedo acceder a la aplicación móvil, me aparece error de credenciales.",
            "Bloqueé mi tarjeta por seguridad, ¿cuál es el procedimiento de reposición?",
            "El servicio de banca por internet funciona muy bien hoy.",
            "Me cobraron una comisión que no corresponde en mi estado de cuenta actual."
        ],
        "label": [2, 1, 0, 2, 2, 1, 2, 0, 1, 2]
    }
    
    df = pd.DataFrame(data)
    dataset = Dataset.from_pandas(df)
    return df, dataset

if __name__ == "__main__":
    df, _ = load_ticket_dataset()
    print(f">> Dataset cargado con éxito. Total de registros: {len(df)}")