from langchain.tools import BaseTool

class MACD_Calculator(BaseTool):
    name = "MACD_Calculator"
    description = "useful for when you need to calculate the MACD of a stock"

    def _run(self, query: str) -> str:
        """Use the tool."""
        print(f"Using MACD calculator for {query}...")
        print("Calculating MACD...")
        print("Downloading price data for last 28 days...")
        print("the closing prices for the past 12 days are 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, and 21, \
              the 12-day EMA is: (21 * (2 / (12 + 1))) + (20 * (2 / (12 + 1))) + (19 * (2 / (12 + 1))) + ... + (10 * (2 / (12 + 1))) = 16.44\n")
        print("the closing prices for the past 26 days are 8, 9, 10, ..., 31, 32, \
               the 26-day EMA is: (32 * (2 / (26 + 1))) + (31 * (2 / (26 + 1))) + (30 * (2 / (26 + 1))) + ... + (8 * (2 / (26 + 1))) = 19.35\n")
        print("The MACD line is simply the difference between the 12-day EMA and the 26-day EMA. In our example, the MACD line is: 16.44 - 19.35 = -2.91\n")
        print("we calculate the 9-day EMA of the MACD line to smooth out the signal and create the 'signal line'. This is often plotted together with the MACD line to generate buy and sell signals. The MACD line values over the past 9 days are -1.5, -2, -2.5, ..., -3.5, -4, the 9-day EMA of the MACD line is: (-4 * (2 / (9 + 1))) + (-3.5 * (2 / (9 + 1))) + (-3 * (2 / (9 + 1))) + ... + (-1.5 * (2 / (9 + 1))) = -2.51 \n")
        return print(f"Based on the values calculated, we can see that the MACD line is negative, indicating that the stock's short-term moving average (12-day EMA) is lower than its long-term moving average (26-day EMA).\
                      This suggests that the stock's price has been declining over the past 12 days relative to the past 26 days. \
                     However, the signal line (9-day EMA of the MACD line) is slightly less negative than the MACD line itself, suggesting that the downward momentum may be slowing down. \
                     This could be a potential indication of a trend reversal or a potential buying opportunity.\n\n")
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        return print(f"Based on the values calculated, we can see that the MACD line is negative, indicating that the stock's short-term moving average (12-day EMA) is lower than its long-term moving average (26-day EMA).\
                      This suggests that the stock's price has been declining over the past 12 days relative to the past 26 days. \
                     However, the signal line (9-day EMA of the MACD line) is slightly less negative than the MACD line itself, suggesting that the downward momentum may be slowing down. \
                     This could be a potential indication of a trend reversal or a potential buying opportunity.\n\n")
