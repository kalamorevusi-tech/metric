# Metric – Finance Math Tools

Hi, I'm Vusi, a Math of Finance student in Gaborone, Botswana.  
This repository contains Python tools for quantitative finance, starting with the **Black-Scholes option pricer**.

## What's inside
- `black_scholes.py` → Calculates European call and put option prices using the classic Black-Scholes model (with example output)

## How to run
```bash
pip install numpy scipy
python black_scholes.py
## Example Output (At-the-money option)

Inputs:
- Stock price (S) = 100
- Strike price (K) = 100
- Time to expiration (T) = 1 year
- Risk-free rate (r) = 5%
- Volatility (σ) = 20%

Results:
