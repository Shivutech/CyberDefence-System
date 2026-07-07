import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# dataset load
data = pd.read_csv("data/packet_data.csv")

# dummy label create (abhi training ke liye)
data["label"] = data["packet_size"].apply(lambda x: 1 if x > 1000 else 0)

X = data[["packet_size","protocol"]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

joblib.dump(model,"models/attack_model.pkl")

print("Model Trained Successfully")