import pandas as pd
import os

file_path = "data/packet_data.csv"

def save_packet(src, dst, size, protocol):

    data = {
        "source_ip": src,
        "destination_ip": dst,
        "packet_size": size,
        "protocol": protocol
    }

    df = pd.DataFrame([data])

    # अगर file exist नहीं करती तो header लिखेगा
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)