import pandas as pd

train = pd.read_csv("train.csv")
validation = pd.read_csv("validation.csv")
test = pd.read_csv("test.csv")

print("TRAIN")
print("Shape:", train.shape)
print(train.columns.tolist())
print()

print("VALIDATION")
print("Shape:", validation.shape)
print(validation.columns.tolist())
print()

print("TEST")
print("Shape:", test.shape)
print(test.columns.tolist())
train = pd.read_csv("train.csv")
validation = pd.read_csv("validation.csv")
test = pd.read_csv("test.csv")

print("Train shape:", train.shape)
print("Validation shape:", validation.shape)
print("Test shape:", test.shape)

print("\nTrain columns:")
print(train.columns.tolist())

print("\nMissing values in train:")
print(train.isnull().sum())