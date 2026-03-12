```python
import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    """
    Black-Scholes option pricing model (European call or put).
    
    Parameters:
    S : float          Current stock price (spot price)
    K : float          Strike price
    T : float          Time to maturity (in years)
    r : float          Risk-free interest rate (annual)
    sigma : float      Volatility (annual standard deviation)
    option_type : str  'call' or 'put'
    
    Returns:
    float: Option price
    """
    if T <= 0:
        # At expiration
        return max(S - K, 0) if option_type == 'call' else max(K - S, 0)
    
    # Calculate d1 and d2 (the famous terms from your finance class)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type.lower() == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return price


# ======================
# Example run (you can change these values anytime)
# ======================
if __name__ == "__main__":
    # Standard example values (S = K = ATM option)
    S = 100.0      # Current stock price
    K = 100.0      # Strike price
    T = 1.0        # 1 year to expiration
    r = 0.05       # 5% risk-free rate
    sigma = 0.20   # 20% volatility
    
    call_price = black_scholes_price(S, K, T, r, sigma, 'call')
    put_price  = black_scholes_price(S, K, T, r, sigma, 'put')
    
    print("=== Black-Scholes Option Pricer ===")
    print(f"Call price : {call_price:.4f}")
    print(f"Put price  : {put_price:.4f}")
    print(f"Put-Call parity check: {call_price - put_price:.4f} (should ≈ {S - K*np.exp(-r*T):.4f})")
    print("\nTry changing the inputs above and run again!")
