import joblib

model = joblib.load("models/attack_model.pkl")

def detect(packet_size, protocol):

    prediction = model.predict([[packet_size, protocol]])

    if prediction[0] == 1:
        return "⚠ Suspicious Traffic"
    else:
        return "Normal Traffic"