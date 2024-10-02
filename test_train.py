import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# import mlflow
# import mlflow.tensorflow
import os

# Enable auto-logging for MLflow
# mlflow.tensorflow.autolog()

# Define output path
output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)

# Generate some example data
X = np.random.rand(1000, 20)
y = np.random.rand(1000, 1)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a simple sequential model
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Start an MLflow run
# with mlflow.start_run() as run:
    # Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # Evaluate the model
loss, mae = model.evaluate(X_test, y_test, verbose=2)

    # Log additional detailed metrics manually (in addition to autologging)
    # mlflow.log_metric("test_loss", loss)
    # mlflow.log_metric("test_mae", mae)

    # Save the training history as an artifact (example plot)
try:
    import matplotlib.pyplot as plt
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss')
    plt.savefig(os.path.join(output_dir, "loss_plot.png"))
    # mlflow.log_artifact(os.path.join(output_dir, "loss_plot.png"))
except ImportError:
    print("matplotlib is not installed, skipping plot generation")

    # Save the model to the output directory
model_save_path = os.path.join(output_dir, "model.h5")
model.save(model_save_path)
    # mlflow.log_artifact(model_save_path)

    # Output to check if everything went fine
    # print(f"Model training and logging finished with run_id: {run.info.run_id}")
print(f"Model saved at {model_save_path}")
