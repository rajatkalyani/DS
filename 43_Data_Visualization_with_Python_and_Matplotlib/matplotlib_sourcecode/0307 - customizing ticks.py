import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np
import datetime as dt


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def graph_data(stock):

    fig = plt.figure()
    
    ax1 = plt.subplot2grid((1,1), (0,0))
    plt.ylabel('Price')
    plt.xlabel('Date')
    
    print('Currently pulling:', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1d/csv'
    print(url)
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    
##    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter = ',',
##                                                          unpack = True,
##                                                          converters={0: bytespdate2num('%Y%m%d')})

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter = ',',
                                                          unpack = True)
    date_conv = np.vectorize(dt.datetime.fromtimestamp)
    date = date_conv(date)
    
    ax1.plot_date(date, closep,'-')
    ax1.grid(True)#, color = 'g', linestyle='-', linewidth=3)
    ax1.yaxis.label.set_color('m')
    ax1.xaxis.label.set_color('c')
    ax1.set_yticks([83.5, 84, 84.5])
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)



        
    plt.subplots_adjust(left=.09, bottom=.16, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()



stock = input('Stock to plot: ')
graph_data(stock)
