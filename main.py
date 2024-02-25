def calculate_deposit_profit(deposit_amount_usdt, deposit_rate, usdt_to_twd_exchange_rate_deposit, usdt_to_twd_exchange_rate_withdraw, days):
    # 計算存款收益
    deposit_amount_twd = deposit_amount_usdt * usdt_to_twd_exchange_rate_deposit
    daily_deposit_interest_rate = deposit_rate / 365  # 每日存款利率
    deposit_profit_twd = deposit_amount_twd * daily_deposit_interest_rate * days
    deposit_profit_usdt = deposit_profit_twd / usdt_to_twd_exchange_rate_withdraw
    return deposit_amount_twd, deposit_profit_twd, deposit_amount_usdt, deposit_profit_usdt

def calculate_revolving_credit_interest(principal, annual_interest_rate, days):
    daily_interest_rate = annual_interest_rate / 365
    total_interest = 0
    for _ in range(days):
        total_interest += principal * daily_interest_rate
        principal += principal * daily_interest_rate
    return total_interest

# 使用者輸入
deposit_amount_usdt = float(input("請輸入存款金額（單位：USDT）："))
deposit_rate = float(input("請輸入存款年化報酬率（例如，0.17代表17%）："))
usdt_to_twd_exchange_rate_deposit = float(input("請輸入入金時的USDT兌TWD匯率："))
usdt_to_twd_exchange_rate_withdraw = float(input("請輸入出金時的USDT兌TWD匯率："))
days = 365

# 計算存款收益
deposit_amount_twd, deposit_profit_twd, deposit_amount_usdt, deposit_profit_usdt = calculate_deposit_profit(deposit_amount_usdt, deposit_rate, usdt_to_twd_exchange_rate_deposit, usdt_to_twd_exchange_rate_withdraw, days)
print("【存款本金：", deposit_amount_twd, "TWD，", deposit_amount_usdt, "USDT】")
print("【存款利息：", deposit_profit_twd, "TWD，", deposit_profit_usdt, "USDT】")

principal = float(input("請輸入貸款金額（單位：TWD）："))
annual_interest_rate = float(input("請輸入年利率（例如，0.07代表7%）："))

# 計算貸款利息
total_interest = calculate_revolving_credit_interest(principal, annual_interest_rate, days)
print("【貸款本金：", principal, "TWD】")
print("【貸款利息：", total_interest, "TWD】")

# 計算淨收益
net_deposit_twd = deposit_amount_twd + deposit_profit_twd
net_deposit_usdt = deposit_amount_usdt + deposit_profit_usdt
net_profit_twd = net_deposit_twd - (principal + total_interest)
net_profit_usdt = net_deposit_usdt - (net_profit_twd / usdt_to_twd_exchange_rate_withdraw)
print("【淨收益：", net_profit_twd, "TWD，", net_profit_usdt, "USDT】")
