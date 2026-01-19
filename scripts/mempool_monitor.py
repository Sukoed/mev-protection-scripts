def check_for_frontrun(gas_price, avg_gas):
    if gas_price > avg_gas * 2:
        return "Warning: High gas detected. Potential front-run attempt."
    return "Mempool status: Normal."

if __name__ == "__main__":
    print(check_for_frontrun(200, 50))
