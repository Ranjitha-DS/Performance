import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def titlemsg():
    st.title("FCE Model Monitoring")
def write():
    st.title("Collection Efficiency for Pilot Regions")
    st.markdown("Welcome! Please select from the filters in the sidebar to the left of your screen to narrow down your search within the log analysis tool.")

    df = pd.read_csv(r'C:\Users\ranjitha_scienaptic\Downloads\May24th_files\CollectionEff_Pilot.csv',index_col=False)
    df1 = pd.read_csv(r'C:\Users\ranjitha_scienaptic\Downloads\May24th_files\Collection_NonPilot.csv',index_col=False)
    #df['FCE%'] = df['FCE%'].str.rstrip("%").astype(float)/100*100
    #df['Collection Efficiency'] = df['Collection Efficiency'].str.rstrip("%").astype(float)/100*100
    #df['Resolution'] = df['Resolution'].str.rstrip("%").astype(float)/100*100
    #df['AWS'] = df['AWS'].str.rstrip("%").astype(float)/100*100
    #fce_1=df['#FCE'].tail(1)
    #fce_perc_1=df['FCE%'].tail(1)
    #coll_3 = df['Collection Efficiency'].tail(1)
    #res_4 = df['Resolution'].tail(1)
    #aws_5 = df['AWS'].tail(1)
    #col1, col2, col3, col4, col5 = st.columns(5)
    #col1.metric("#FCE", "873", "4%")
    #col2.metric("FCE%", "100 %", "4%")
    #col3.metric("Collection Efficiency", "30%", "-4%")
    #col4.metric("Resolution", "68 %", "2%")
    #col5.metric("AWS", "57 %", "-8%")
    df = df.iloc[:-1 , :]
    df1 = df1.iloc[:-1 , :]
    selected_options =[]
    # log table for the app...
    #st.dataframe(df)
    options = df['FCE_SEGMENT'].unique().tolist()
    selected_options = st.sidebar.multiselect('Which Segment do you want?',options)
    print(len(selected_options))
    filtered_df = df[df['FCE_SEGMENT'].isin(selected_options)]
    filtered_df1 = df1[df1['FCE_SEGMENT'].isin(selected_options)]
    if(len(selected_options)==0):
        #st.dataframe(filtered_df)
        cm = sns.palplot(sns.color_palette("BuGn_r", 10))
        hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
        df11 = df.head(3)
        df12 = df1.head(3)
        st.dataframe(df.style
        .background_gradient(cmap='RdYlGn', subset=(df.index[0:6],['2021-09','2021-10','2021-11','2021-12',	'2022-01','2022-02','2022-03','2022-04','2022-05']))
        .set_properties(subset=['2021-09','2021-10','2021-11','2021-12','2022-01','2022-02','2022-03','2022-04','2022-05']))

        chart_df = df[['FCE_SEGMENT', '2021-09','2021-10','2021-11','2021-12','2022-01','2022-02','2022-03','2022-04','2022-05']]

        # chart_df = chart_df.astype(str)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-09'],
                    mode='lines+markers',
                    name='2021-09'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-10'],
                    mode='lines+markers',
                    name='2021-10'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-11'],
                    mode='lines+markers',
                    name='2021-11'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-12'],
                    mode='lines+markers',
                    name='2021-12'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-01'],
                    mode='lines+markers',
                    name='2022-01'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-02'],
                    mode='lines+markers',
                    name='2022-02'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-03'],
                    mode='lines+markers',
                    name='2022-03'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-04'],
                    mode='lines+markers',
                    name='2022-04'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-05'],
                    mode='lines+markers',
                    name='2022-05'))

        fig.update_layout(
           title="Month wise Collection Efficiency of Pilot Regions",
           xaxis_title="FCE Segment",
           yaxis_title="Collection Efficiency",
           legend_title="Metrics",
            )
        st.plotly_chart(fig, use_container_width=True)

        st.title("Collection Efficiency for Non Pilot Regions")
        st.dataframe(df1.style
        .background_gradient(cmap='RdYlGn', subset=(df1.index[0:6],['2021-09','2021-10','2021-11','2021-12','2022-01','2022-02','2022-03','2022-04','2022-05']))
        .set_properties(subset=['2021-09','2021-10','2021-11','2021-12','2022-01','2022-02','2022-03','2022-04','2022-05']))

        chart_df = df1[['FCE_SEGMENT', '2021-09','2021-10','2021-11','2021-12','2022-01','2022-02','2022-03','2022-04','2022-05']]

        # chart_df = chart_df.astype(str)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-09'],
                    mode='lines+markers',
                    name='2021-09'))
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-10'],
                    mode='lines+markers',
                    name='2021-10'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-11'],
                    mode='lines+markers',
                    name='2021-11'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2021-12'],
                    mode='lines+markers',
                    name='2021-12'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-01'],
                    mode='lines+markers',
                    name='2022-01'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-02'],
                    mode='lines+markers',
                    name='2022-02'))
     
        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-03'],
                    mode='lines+markers',
                    name='2022-03'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-04'],
                    mode='lines+markers',
                    name='2022-04'))

        fig.add_trace(go.Scatter(x=chart_df['FCE_SEGMENT'].astype(str), y=chart_df['2022-05'],
                    mode='lines+markers',
                    name='2022-05'))
  

        fig.update_layout(
           title="Month wise Collection Efficiency of Non Pilot Regions",
           xaxis_title="FCE Segment",
           yaxis_title="Collection Efficiency",
           legend_title="Metrics",
            )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.dataframe(filtered_df)
        st.dataframe(filtered_df1)

def write1():
    st.title("Decile Wise Performance")
    st.markdown("Welcome! Please select from the filters in the sidebar to the left of your screen to narrow down your search within the log analysis tool.")

    df = pd.read_csv(r'C:\Users\ranjitha_scienaptic\Downloads\May24th_files\Collection_NonPilot.csv',index_col=False)
    #df['FCE%'] = df['FCE%'].str.rstrip("%").astype(float)/100*100
    #df['Collection Efficiency'] = df['Collection Efficiency'].str.rstrip("%").astype(float)/100*100
    #df['Resolution'] = df['Resolution'].str.rstrip("%").astype(float)/100*100
    #df['AWS'] = df['AWS'].str.rstrip("%").astype(float)/100*100
    #fce_1=df['#FCE'].tail(1)
    #fce_perc_1=df['FCE%'].tail(1)
    #coll_3 = df['Collection Efficiency'].tail(1)
    #res_4 = df['Resolution'].tail(1)
    #aws_5 = df['AWS'].tail(1)
    #col1, col2, col3, col4, col5 = st.columns(5)
    #col1.metric("#FCE", "873", "4%")
    #col2.metric("FCE%", "100 %", "4%")
    #col3.metric("Collection Efficiency", "30%", "-4%")
    #col4.metric("Resolution", "68 %", "2%")
    #col5.metric("AWS", "57 %", "-8%")
    df = df.iloc[:-1 , :]
    selected_options =[]
    # log table for the app...
    #st.dataframe(df)
    options = df['FCE_SEGMENT'].unique().tolist()
    selected_options = st.sidebar.multiselect('Which Decile do you want?',options)
    print(len(selected_options))
    filtered_df = df[df['Decile'].isin(selected_options)]
    if(len(selected_options)==0):
        #st.dataframe(filtered_df)
        cm = sns.palplot(sns.color_palette("BuGn_r", 10))
        hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
        #df1 = df.head(3)
        st.dataframe(df.style
        .background_gradient(cmap='RdYlGn', subset=(df.index[0:9],['Collection Efficiency','Resolution','AWS']))
        .set_properties(subset=['Collection Efficiency','Resolution','AWS']))

    else:
        st.dataframe(filtered_df)