from inventory import Inventory

SAMPLE = [
    "Milk, MLK001,1.25,12",
    "Bread, BRD002,0.90,3",
    "Eggs, EGG003,2.40,30",
    "Coffee, COF004,7.50,2",
]

def main():
    inv = Inventory.from_lines(SAMPLE)
    print(f"{'Product':<10} | {'SKU':<8} | {'Price':<6} | {'Qty':<4} | {'Line Value':<10}")
    print("-" * 50)
    for p in inv.products.values():
        print(f"{p.name:<10} | {p.sku:<8} | ${p.price:<5.2f} | {p.quantity:<4} | ${p.line_value:<9.2f}")
    print("-" * 50)
    print(f"Total Inventory Value: ${inv.total_value():.2f}")
    low_stock = [p.name for p in inv.products.values() if p.is_low_stock]
    print(f"Low Stock Items (<5): {', '.join(low_stock)}")

if __name__ == "__main__":
    main()
