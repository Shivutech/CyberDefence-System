import streamlit as st
import pandas as pd
import time

st.title("AI Cyber Defense Dashboard")

file_path = "data/packet_data.csv"

while True:

    try:
        data = pd.read_csv(file_path)

        st.subheader("Live Packet Data")
        st.dataframe(data.tail(20))

        st.subheader("Traffic Statistics")

        total_packets = len(data)
        avg_size = data["packet_size"].mean()

        col1, col2 = st.columns(2)

        col1.metric("Total Packets", total_packets)
        col2.metric("Average Packet Size", int(avg_size))

        st.subheader("Protocol Distribution")

        st.bar_chart(data["protocol"].value_counts())

    except:
        st.write("Waiting for packet data...")

    time.sleep(3)