from tensorflow.keras.models import load_model

# 載入舊模型
old_model = load_model("models/lstm_model.h5")

# 儲存為 SavedModel 格式
old_model.save("models/lstm_model_v2")  # 會生成 models/lstm_model_v2/ 資料夾
print("Model converted to SavedModel format!")
