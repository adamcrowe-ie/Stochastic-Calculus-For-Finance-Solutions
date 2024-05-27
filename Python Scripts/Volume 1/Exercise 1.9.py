NEXT_STOCK_PRICE_HEADS = lambda sp: sp+10
NEXT_STOCK_PRICE_TAILS = lambda sp: sp-10
STRIKE_PRICE = 80
PAYOFF_PERIOD = 5
PAYOFF = lambda sp: max(sp - STRIKE_PRICE, 0)

history: dict = {}

def dv_price(period: int, stock_price: float) -> float:
    if period == PAYOFF_PERIOD: return PAYOFF(stock_price)

    global history
    key: str = f"period: {period}, stock_price: {stock_price}"

    if key in history: return history[key]
    
    dv_price_next_period_heads: float = dv_price(period + 1, NEXT_STOCK_PRICE_HEADS(stock_price))
    dv_price_next_period_tails: float = dv_price(period + 1, NEXT_STOCK_PRICE_TAILS(stock_price))

    history[key] = 0.5 * (dv_price_next_period_heads + dv_price_next_period_tails)
    return history[key]

if __name__ == "__main__":
    answer = dv_price(0, 80)
    print(f"v_0(80) = {answer}")