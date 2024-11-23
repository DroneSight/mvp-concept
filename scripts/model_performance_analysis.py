import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv(
    "ship-detection/train-results-for-sentinel-1-SAR-over-100-epochs/results.csv"
)

# Plot precision, recall, and mAP metrics
plt.figure(figsize=(12, 6))

plt.plot(
    results_df["epoch"], results_df["metrics/precision(B)"], label="Precision"
)
plt.plot(results_df["epoch"], results_df["metrics/recall(B)"], label="Recall")
plt.plot(results_df["epoch"], results_df["metrics/mAP50(B)"], label="mAP@0.5")
plt.plot(
    results_df["epoch"],
    results_df["metrics/mAP50-95(B)"],
    label="mAP@0.5:0.95",
)

plt.xlabel("Epoch")
plt.ylabel("Value")
plt.title("Validation Metrics Over Epochs")
plt.legend()
plt.grid(True)
plt.show()


# Plot training and validation losses
plt.figure(figsize=(12, 6))

plt.plot(
    results_df["epoch"], results_df["train/box_loss"], label="Train Box Loss"
)
plt.plot(
    results_df["epoch"],
    results_df["val/box_loss"],
    label="Validation Box Loss",
)
plt.plot(
    results_df["epoch"], results_df["train/cls_loss"], label="Train Class Loss"
)
plt.plot(
    results_df["epoch"],
    results_df["val/cls_loss"],
    label="Validation Class Loss",
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training and Validation Losses Over Epochs")
plt.legend()
plt.grid(True)
plt.show()


final_metrics = results_df.iloc[-1][
    [
        "metrics/precision(B)",
        "metrics/recall(B)",
        "metrics/mAP50(B)",
        "metrics/mAP50-95(B)",
    ]
]
print("Final Validation Metrics:")
print(final_metrics)
