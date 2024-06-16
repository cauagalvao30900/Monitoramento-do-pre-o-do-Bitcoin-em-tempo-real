import requests
import json
import time
from tkinter import Tk, Label, StringVar
from threading import Thread

# Função para buscar o preço do Bitcoin em tempo real
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price
    except Exception as e:
        print(f"Erro ao buscar preço do Bitcoin: {e}")
        return None

# Função para atualizar o preço do Bitcoin na interface gráfica
def update_price_label(price_var):
    while True:
        try:
            price = get_bitcoin_price()
            if price is not None:
                price_var.set(f"Preço do Bitcoin: $ {price:.2f}")
            else:
                price_var.set("Erro ao buscar o preço")
        except Exception as e:
            price_var.set("Erro ao buscar o preço")
            print(e)
        time.sleep(60)  # Atualiza a cada 60 segundos

# Função principal do aplicativo
def main():
    root = Tk()
    root.title("Monitor de Preço do Bitcoin")
    root.geometry("300x100")
    
    price_var = StringVar()
    price_label = Label(root, textvariable=price_var, font=("Helvetica", 16))
    price_label.pack(pady=20)
    
    # Inicia a thread para atualizar o preço do Bitcoin
    thread = Thread(target=update_price_label, args=(price_var,))
    thread.daemon = True
    thread.start()
    
    root.mainloop()

if __name__ == "__main__":
    main()
