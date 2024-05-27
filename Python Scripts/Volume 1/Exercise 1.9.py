NEXT_STOCK_PRICE_HEADS = lambda sp: sp+10
NEXT_STOCK_PRICE_TAILS = lambda sp: sp-10
STRIKE_PRICE = 80
PAYOFF_PERIOD = 5
PAYOFF = lambda sp: max(sp - STRIKE_PRICE, 0)

history = {}

def derivative_price(period: int, stock_price: float) -> float:
    price: float
    key = f"period: {period}, stock_price: {stock_price}"

    if period == PAYOFF_PERIOD:
        price = PAYOFF(stock_price)
    elif key in history:
        price = history[key]
    else:
        derivative_price_next_period_heads = derivative_price(period + 1, NEXT_STOCK_PRICE_HEADS(stock_price))
        derivative_price_next_period_tails = derivative_price(period + 1, NEXT_STOCK_PRICE_TAILS(stock_price))
        price = 0.5 * (derivative_price_next_period_heads + derivative_price_next_period_tails)

    history[key] = price
    return price

if __name__ == "__main__":
    answer = derivative_price(0, 80)
    print(f"v_0(80) = {answer}")