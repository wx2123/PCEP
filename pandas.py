#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:54:02 2021

@author: jt2018
"""
import pandas as pd

def make_df(cols, ind):
    data = {c:[str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data,ind)

df1 = make_df('AB',[1,2])
df2 = make_df('AB',[3,4])

print(df1); print(df2);print(pd.concat([df1,df2]))


