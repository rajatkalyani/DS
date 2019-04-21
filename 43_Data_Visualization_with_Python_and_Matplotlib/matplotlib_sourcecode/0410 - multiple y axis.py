import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import urllib
import numpy as np
import datetime as dt

from matplotlib import style

style.use('fivethirtyeight')

MA1 = 5
MA2 = 15

#print(plt.style.available)
#print(plt.__file__)


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows


def graph_data(stock):

    fig = plt.figure()
    
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex = ax1)
    plt.ylabel('Price')
    ax2v = ax2.twinx()
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)
    plt.ylabel('MAvgs')

    
    print('Currently pulling:', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    print(url)
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter = ',',
                                                          unpack = True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])
    print(start)

    x = 0
    y = len(date)

    new_list = []
    while x < y:
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)
        x += 1

    h_l = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date[-start:], h_l[-start:], '-')
    plt.setp(ax1.get_xticklabels(), visible=False)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='lower'))

    
    
    candlestick_ohlc(ax2, new_list[-start:], width=.6, colorup='#41ad49', colordown='#ff1717')
    ax2.grid(True)#, color = 'g', linestyle='-', linewidth=3)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))
    bbox_props = dict(boxstyle='round4, pad=0.3', fc="#c5cbdf", ec='k', lw=2)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1]+8, closep[-1]), bbox = bbox_props)


    ax2v.fill_between(date[-start:], 0, volume[-start:], facecolor='#0079a3', alpha = 0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*volume.max())



    ax3.plot(date[-start:], ma1[-start:], linewidth = 1)
    ax3.plot(date[-start:], ma2[-start:], linewidth = 1)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:]>=ma1[-start:]), facecolor='r', edgecolor='r', alpha=0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:]<=ma1[-start:]), facecolor='g', edgecolor='g', alpha=0.5)
    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))

    

        
    plt.subplots_adjust(left=.11, bottom=.16, right=.90, top=.95, wspace=.2, hspace=.0)
    plt.show()



stock = input('Stock to plot: ')
graph_data(stock)
