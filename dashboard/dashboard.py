import streamlit as st
import pandas as pd
import numpy as np
import os, datetime

from dashboard.utils import *

class Dashboard:
    def __init__(self, df_day, df_hour):
        self.df_day = preprocess_df(df_day)
        self.df_hour = preprocess_df(df_hour)
    
    def run(self):
        min_date = self.df_day['dteday'].min()
        max_date = self.df_day['dteday'].max()
        header, _ = st.columns([0.8, 0.2])
        mode_square, date_square, time_square_start, time_square_end = header.columns([10,15,8,8])
        mode = mode_square.radio("Select mode:", ["Daily", 'Hourly'])

        if mode == "Daily": 
            date = date_square.date_input(
                    label='Date Range',
                    min_value=min_date,
                    max_value=max_date,
                    value=[min_date, max_date]
                )
            
            df_cur = filter_df(self.df_day, date)
            
            monthly_plot = monthly_bar(df_cur)
            st.pyplot(monthly_plot.figure)
            
            column1, column2 = st.columns(2)

            seasonly_group_plot = group_pie(df_cur, by='season')
            column1.pyplot(seasonly_group_plot)

            monthly_group_plot = group_pie(df_cur, by='mnth')
            column2.pyplot(monthly_group_plot)

        else : 
            date = date_square.date_input(
                    label='Date Range',
                    min_value=min_date,
                    max_value=max_date,
                    value=[min_date, max_date]
                )
            time_start = time_square_start.time_input('Hour Start', datetime.time(0, 00))
            time_end = time_square_end.time_input('Hour End', datetime.time(23, 00))
            
            df_cur = filter_df(self.df_hour, date, (time_start, time_end))
            
            hourly_plot = group_bar(df_cur)
            st.pyplot(hourly_plot.figure)

            column1, column2 = st.columns(2)

            seasonly_group_plot = group_pie(df_cur, by='season')
            column1.pyplot(seasonly_group_plot)

            monthly_group_plot = group_pie(df_cur, by='mnth')
            column2.pyplot(monthly_group_plot)

        st.dataframe(df_cur)


