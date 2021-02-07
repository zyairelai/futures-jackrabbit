import config
import binance_futures
from termcolor import colored

def current_minute(minute):
    if minute == 1: klines = klines = binance_futures.KLINE_INTERVAL_1MINUTE()
    elif minute == 3: klines = klines = binance_futures.KLINE_INTERVAL_3MINUTE()
    elif minute == 5: klines = klines = binance_futures.KLINE_INTERVAL_5MINUTE()

    first_run_Open  = round(((float(klines[0][1]) + float(klines[0][4])) / 2), config.round_decimal)
    first_run_Close = round(((float(klines[0][1]) + float(klines[0][2]) + float(klines[0][3]) + float(klines[0][4])) / 4), config.round_decimal)
    first_Open      = round(((first_run_Open + first_run_Close) / 2), config.round_decimal)
    first_Close     = round(((float(klines[1][1]) + float(klines[1][2]) + float(klines[1][3]) + float(klines[1][4])) / 4), config.round_decimal)
    previous_Open   = round(((first_Open + first_Close) / 2), config.round_decimal)
    previous_Close  = round(((float(klines[2][1]) + float(klines[2][2]) + float(klines[1][3]) + float(klines[2][4])) / 4), config.round_decimal)

    current_Open    = round(((previous_Open + previous_Close) / 2), config.round_decimal)
    current_Close   = round(((float(klines[3][1]) + float(klines[3][2]) + float(klines[3][3]) + float(klines[3][4])) / 4), config.round_decimal)
    current_High    = max(float(klines[3][2]), current_Open, current_Close)
    current_Low     = min(float(klines[3][3]), current_Open, current_Close)

    # print("The current_Open is  :   " + str(current_Open))
    # print("The current_Close is :   " + str(current_Close))
    # print("The current_High is  :   " + str(current_High))
    # print("The current_Low is   :   " + str(current_Low))

    if (current_Open == current_High):
        minute_candle = "RED"
        print(colored("RECENT " + str(minute) + " MINUTE  :   " + minute_candle, "red"))

    elif (current_Open == current_Low):
        minute_candle = "GREEN"
        print(colored("RECENT " + str(minute) + " MINUTE  :   " + minute_candle, "green"))

    elif (current_Open > current_Close):
        minute_candle = "RED_INDECISIVE"
        print(colored("RECENT " + str(minute) + " MINUTE  :   " + minute_candle, "red"))

    elif (current_Close > current_Open):
        minute_candle = "GREEN_INDECISIVE"
        print(colored("RECENT " + str(minute) + " MINUTE  :   " + minute_candle, "green"))

    else:
        minute_candle = "NO_MOVEMENT"
        print(colored("RECENT " + str(minute) + " MINUTE  :   " + minute_candle, "white"))
    return minute_candle

def emergency_minute():
    klines = klines = binance_futures.KLINE_INTERVAL_1MINUTE()

    first_run_Open  = round(((float(klines[0][1]) + float(klines[0][4])) / 2), config.round_decimal)
    first_run_Close = round(((float(klines[0][1]) + float(klines[0][2]) + float(klines[0][3]) + float(klines[0][4])) / 4), config.round_decimal)
    first_Open      = round(((first_run_Open + first_run_Close) / 2), config.round_decimal)
    first_Close     = round(((float(klines[1][1]) + float(klines[1][2]) + float(klines[1][3]) + float(klines[1][4])) / 4), config.round_decimal)

    previous_Open   = round(((first_Open + first_Close) / 2), config.round_decimal)
    previous_Close  = round(((float(klines[2][1]) + float(klines[2][2]) + float(klines[1][3]) + float(klines[2][4])) / 4), config.round_decimal)
    previous_High   = max(float(klines[2][2]), previous_Open, previous_Close)
    previous_Low    = min(float(klines[2][3]), previous_Open, previous_Close)

    current_Open    = round(((previous_Open + previous_Close) / 2), config.round_decimal)
    current_Close   = round(((float(klines[3][1]) + float(klines[3][2]) + float(klines[3][3]) + float(klines[3][4])) / 4), config.round_decimal)
    current_High    = max(float(klines[3][2]), current_Open, current_Close)
    current_Low     = min(float(klines[3][3]), current_Open, current_Close)

    if (current_Open == current_High) and (current_Low < previous_Low): return "RED"
    elif (current_Open == current_Low) and (current_High < previous_High): return "GREEN"
    elif (current_Open > current_Close) and (current_Low < previous_Low): return "RED"
    elif (current_Close > current_Open) and (current_High < previous_High): return "GREEN"
    else: return "INDECISIVE"
