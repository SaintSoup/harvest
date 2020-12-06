
from datetime import datetime
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import butter, lfilter

def import_data(path_to_dataset,seperator=',',sampling_freq=1000,order=['ax','ay','az','time'],abstime=0,stamp=0): 
    #imports data, seperated by a comma (default), with a 1 kHz frequency
    #the order of the data columns by default ax, ay, az, and are the timestamps provided              (abstime=1) or are timestamps in delta times and a list of data to keep
    data_init = pd.read_csv(filepath_or_buffer=path_to_dataset,sep=seperator, header=0,names=order)
    data_init.header('dt')
    if data_init.header('dt') != None:
        #Adding A cummulative sum comlun(for absolute time), this will serve as identification and         will help during plotting
        data_init["time"]=data_init["dt"].cumsum()
    #----------------------------------------
    # 
    # if stamp:
    #To generate a time stamp 
    #    data_init["timestamp"]= data_init["time"].apply(lambda x: datetime(microseconds = x*))
    #
    #----------------------------------------

    #data_init[][len(data_init)-1]
    data_init.drop(headers=["az","ay"])

    data_out=pd.headers(data_init.headers())
    #Homogenizing the sampling rate (we settle for the case where delta t is 1)
    num_cols = len(data_init.columns())
    j=0
    for index in len(data_init):
        if data_init["dt"].loc(index) == 1:
            data_out.loc[j] =data_init[index]
            j+=1
        else:
            for i in range(0,data_init["dt"].loc()):
                data_out.loc[j] = [np.NaN for p in range(0,num_cols)]
                j+=1
            data_out.loc[j] =data_init[index]
            j+=1
    data_init.drop(headers=["dt"])
    return data_out

def data_probe(df):
    print("-------Information about the dataframe-------")
    df.info()
    df.describe()
    print("-------Head and Tail of the dataframe-------")
    df.Head()
    df.Tail()
    if df.value_counts():
        print("-------Count of missing data in the dataframe-------")
        df.value_counts()

def filter(method='linear',df=None,fs=1000,cutoff="50",order=2):
    #takes in a dataframe, a sampling frequency (1 kHz by default), a cutoff frquency, and an order and applies a lowpass butterworth filter to the acceleration data
    df["ax"]=df["ax"].interpolate(method=method, limit_direction='forward')
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    data=df["ax"].to_numpy()
    y = lfilter(b, a, data)
    data_out =pd.dataframe(y)
    return data_out

def extremes(df, fs):
    #determining the extrema 
    df['min'] = df['ax'][(df['ax'].shift(1) > df['ax']) & (df['ax'].shift(-1) > df['ax'])]
    df['max'] = df['ax'][(df['ax'].shift(1) < df['ax']) & (df['ax'].shift(-1) < df['ax'])]
    #computing the difference between consecutive extrema as well as the time difference between each extreme  (following)
    min=df['ax'].loc[0]
    max=df['ax'].loc[0]
    delta_t=0
    i_last_min=0
    i_last_max=0
    for index in len(df):
        if df['min'].loc[index]:
            min= df['min'].loc[index]
            df['delta_ext'].loc[index]=max-min
            df['next_ext'].loc[i_last_min] = delta_t
            delta_t=0
            i_last_min=index
        if df['max'].loc[index]:
            max= df['max'].loc[index]
            df['delta_ext'].loc[index]=max-min 
            df['next_ext'].loc[i_last_max] = delta_t
            delta_t=0
            i_last_min=index
        delta_t+= 1/fs
        #and then you fill the empty slots with a linear interpolation of the time 
    return df

def interpolate(df):
    #just a wrapper. Used to fill the NaNs
    df=df.interpolate(method='spline',order=5, limit_direction='forward')
    return df