import yfinance as yf
import time
# EJEMPLO
# Símbolo de la acción (Apple en este caso)
stock_symbol = "AAPL"

# Intervalo de tiempo intradiario (1 minuto en este caso)
interval = "1m"

# Número de días hacia atrás desde hoy
days_back = 1

# Función para obtener y mostrar datos en tiempo real
def get_and_show_realtime_data(symbol, interval, days_back):
    count = 0
    while count <= 3:
        # Obtener datos de Yahoo Finance
        stock_data = yf.download(symbol, period=f"{days_back}d", interval=interval)

        # Elimina la barra de progreso
        stock_data = stock_data.reset_index()
        
        # Obtener el último precio de cierre
        last_close_price = stock_data["Close"].iloc[-1]

        # Imprimir el precio de cierre en tiempo real
        print(f"({symbol}) Precio de cierre en tiempo real: {last_close_price:.2f}")

        # Esperar un período antes de la próxima actualización
        time.sleep(0.5)  # Actualiza cada 60 segundos
        count += 1

if __name__ == "__main__":
    get_and_show_realtime_data(stock_symbol, interval, days_back)
