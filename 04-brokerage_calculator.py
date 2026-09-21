buy_price = 50.0
buy_quantity = 65
sell_price = 100
brokerage = 0
sebi_charge = 10

stt_buy = (0.1*buy_price * buy_quantity)/100
nse_charge = (0.00307/100) * (buy_price * buy_quantity)

stamp_charge = (0.015 * buy_price * buy_quantity )/100

gst = (brokerage + sebi_charge + nse_charge) * (18/100)
total_cost = (buy_quantity*buy_price) + brokerage + sebi_charge + stt_buy + nse_charge + gst
print(f"Total Cost: Rs.{total_cost}")