from tensorflow.keras.models import load_model

# 載入舊模型
model = load_model("models/lstm_model.h5")

# 轉 SavedModel
model.save("models/lstm_model_saved")  # 生成資料夾
print("SavedModel format generated!")
