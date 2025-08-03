import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

print("Loading dataset...")
df = pd.read_csv("network_data.csv")

drop_cols = ['Label', 'Attempted Category', 'Timestamp']
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

df = df.select_dtypes(include=[np.number]).dropna()

print("Data shape after cleaning:", df.shape)

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df.values)

input_dim = X_scaled.shape[1]
input_layer = Input(shape=(input_dim,))
encoded = Dense(16, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)
autoencoder = Model(input_layer, decoded)

autoencoder.compile(optimizer='adam', loss='mse')
print("Training autoencoder...")
autoencoder.fit(X_scaled, X_scaled, epochs=20, batch_size=32, verbose=1)

X_pred = autoencoder.predict(X_scaled)
mse = np.mean(np.power(X_scaled - X_pred, 2), axis=1)

threshold = np.percentile(mse, 95)
anomalies = mse > threshold

print("Anomalies detected at rows:", np.where(anomalies)[0].tolist())
print("Total anomalies found:", np.sum(anomalies))
