
# --- LOGIC MODULE (Member Mohammed Aaquil) ---
def calculate_allowances(basic):
    """Calculates HRA and DA."""
    hra = 0.20 * basic
    da = 0.10 * basic
    return hra, da

def calculate_net_pay(basic, hra, da):
    """Calculates gross, tax, and final net salary."""
    gross = basic + hra + da
    tax = 0.05 * gross
    net = gross - tax
    return gross, tax, net
