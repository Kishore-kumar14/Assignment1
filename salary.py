# --- LOGIC MODULE (Member A) ---
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

# --- UI / RUNNER MODULE (Member B) ---
def run_app():
    try:
        # Input
        basic_salary = float(input("Enter the Basic Salary: "))

        # Processing (Calling the Logic)
        hra, da = calculate_allowances(basic_salary)
        gross, tax, net = calculate_net_pay(basic_salary, hra, da)

        # Output
        print("\n" + "="*30)
        print(f"{'SALARY SLIP':^30}")
        print("="*30)
        print(f"Basic Pay:   ${basic_salary:,.2f}")
        print(f"HRA (20%):   ${hra:,.2f}")
        print(f"DA (10%):    ${da:,.2f}")
        print(f"Tax (5%):    ${tax:,.2f}")
        print("-" * 30)
        print(f"NET SALARY:  ${net:,.2f}")
        print("="*30)

    except ValueError:
        print("Error: Please enter a numeric value.")

if __name__ == "__main__":
    run_app()







