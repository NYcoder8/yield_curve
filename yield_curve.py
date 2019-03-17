import pandas as pd
import matplotlib.pyplot as plt


def get_yield_curve():
    ust_url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2019'
    yield_curve = pd.read_html(ust_url, parse_dates = True) 
    
    # The yield curve is in table 1
    yield_curve = yield_curve[1].dropna(how = 'any')
    
    # Get just the 10 and 2 year and remove the string in first row
    yield_curve_10_2 = yield_curve[[0,6,10]][1:]
    yield_curve_10_2.columns = ['date', '2 yr', '10 yr']
    
    yield_curve_10_2[[6,10]] = yield_curve_10_2[['2 yr','10 yr']].astype(float)
    yield_curve_10_2['10-2'] = yield_curve_10_2[10] - yield_curve_10_2[6]
    return yield_curve_10_2


yield_spread = get_yield_curve()

# Need to convert to datetime before plotting with this version of matplotlib
yield_spread['date'] = pd.to_datetime(yield_spread['date'])

# plot
plt.style.use("ggplot")
plt.plot(yield_spread['date'], yield_spread['10-2'])
plt.xlabel('Date')
plt.ylabel('10-2 Spread')
plt.legend()
plt.show()
