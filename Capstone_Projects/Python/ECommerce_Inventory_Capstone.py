import json
import os
from datetime import datetime

class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {"pid": self.pid, "name": self.name, "price": self.price, "stock": self.stock}

class InventoryManager:
    FILE_PATH = "inventory.json"
    
    def __init__(self):
        self.products = {}
        self._load()

    def _load(self):
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, 'r') as f:
                    data = json.load(f)
                    for pid, p in data.items():
                        self.products[pid] = Product(p['pid'], p['name'], p['price'], p['stock'])
            except json.JSONDecodeError:
                self.products = {}
                
    def _save(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump({pid: p.to_dict() for pid, p in self.products.items()}, f, indent=4)

    def add_product(self, pid, name, price, stock):
        if pid in self.products:
            print(f"Error: Product ID {pid} already exists.")
            return
        self.products[pid] = Product(pid, name, price, stock)
        self._save()
        print(f"Product '{name}' added successfully.")

    def process_order(self, pid, quantity):
        if pid not in self.products:
            print("Error: Product not found.")
            return
        
        prod = self.products[pid]
        if prod.stock >= quantity:
            prod.stock -= quantity
            self._save()
            total = prod.price * quantity
            print(f"Order processed. Invoice Total: ${total:.2f}. Remaining Stock: {prod.stock}")
        else:
            print(f"Error: Insufficient stock. Available: {prod.stock}")

    def generate_report(self):
        print(f"\n--- Inventory Report [{datetime.now().strftime('%Y-%m-%d %H:%M')}] ---")
        total_value = 0
        for p.pid, prod in self.products.items():
            val = prod.price * prod.stock
            total_value += val
            print(f"[{prod.pid}] {prod.name.ljust(15)} | Stock: {prod.stock} | Price: ${prod.price:.2f} | Value: ${val:.2f}")
        print("-" * 50)
        print(f"Total Framework Value: ${total_value:.2f}\n")

if __name__ == "__main__":
    app = InventoryManager()
    print("Welcome to E-Commerce Capstone Inventory Manager")
    # For simulation, initializing state if empty
    if not app.products:
        app.add_product("P101", "Laptop", 999.99, 10)
        app.add_product("P102", "Mouse", 19.99, 50)
    
    app.generate_report()
    app.process_order("P101", 2)
    app.process_order("P102", 55) # Should fail
    app.generate_report()