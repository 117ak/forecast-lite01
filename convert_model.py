from tensorflow.keras.models import load_model

# 載入舊 .h5 模型
old_model = load_model("models/lstm_model.h5")

# 儲存為 SavedModel 格式
old_model.save("models/lstm_model_v2")  # 目錄形式
print("Model converted to SavedModel format!")
