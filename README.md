# 🎉 Age, Gender, and Ethnicity Prediction 📸

---

## 📖 **English** 🇬🇧

---

### 🚀 **Welcome to Age, Gender, and Ethnicity Prediction App!** 🌐

This project uses deep learning models to predict age, gender, and ethnicity from facial images. It's built using **TensorFlow** and **Streamlit** and is accessible on:

🌐 [https://agegenderprediction-furkansukan.streamlit.app/](https://agegenderprediction-furkansukan.streamlit.app/)

---

## 🛠️ **Technologies Used** 🔧

- **Python Libraries** 📚:
  - `streamlit` 🖥️
  - `tensorflow` 🤖
  - `PIL (Pillow)` 📸
  - `numpy` 🔢

---

## 📝 **How to Set Up and Run** 📦

### 1️⃣ **Clone the Repository** 🔄

```bash
git clone https://github.com/yourusername/age-gender-prediction.git
```

### 2️⃣ **Install Dependencies** 🔌

Make sure you have all the necessary packages installed:

```bash
pip install streamlit tensorflow Pillow numpy
```

### 3️⃣ **Run the Application** 🚀

Start the Streamlit app locally:

```bash
streamlit run app.py
```

### 4️⃣ **Upload an Image 📷**

- Upload a facial image through the interface.
- The model will predict the **age, gender**, and **ethnicity** in real-time. 🔍

---

## 📊 **Model Architecture** 🧠

Here's a quick look at the model:

```python
model = tf.keras.Sequential([
    L.InputLayer(input_shape=(48, 48, 1)),
    L.Conv2D(32, (3, 3), activation='relu'),
    L.BatchNormalization(),
    L.MaxPooling2D((2, 2)),
    L.Conv2D(64, (3, 3), activation='relu'),
    L.MaxPooling2D((2, 2)),
    L.Flatten(),
    L.Dense(64, activation='relu'),
    L.Dropout(rate=0.5),
    L.Dense(1, activation='sigmoid')
])

model.compile(optimizer='sgd',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])
```

### 📢 **Callback for Early Stopping** ⏱️

The training stops automatically when validation loss reaches **0.2700**.

---

## 📅 **Dataset Information** 🔍

### **About Dataset** 📖

- The dataset contains facial images labeled by **age, gender**, and **ethnicity**.
- Initially collected from the **UTK Dataset** and multiple sources requiring **data cleaning** and **preprocessing**.
- All data has been arranged in a simple **CSV format** for ease of access and usage. 📈

### 📊 **Dataset Content** 📜

- **27305 rows**
- **5 columns**  
  Contains age, gender, ethnicity, and facial image data. 

### 🙌 **Acknowledgements** 🙏

- Original JPEG files were sourced from **Kaggle**. 🕵️‍♂️


---

## 📞 Contact
If you have any questions or suggestions, feel free to reach out to me:

Feel free to reach out for questions or feedback via:
- **Email:** [furkansukan10@gmail.com](furkansukan10@gmail.com)
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/furkansukan/)
- **Kaggle:** [Kaggle Profile](https://www.kaggle.com/furkansukan)
- **Website:** [Project Website](https://agegenderprediction-furkansukan.streamlit.app/)

---

---

## 🇹🇷 **Türkçe** 🗨️

---

### 🚀 **Yaş, Cinsiyet ve Etnisite Tahmini Uygulaması!** 📸

Bu proje, yüz resimlerinden **yaş, cinsiyet** ve **etnisite** tahmin etmek için derin öğrenme modellerini kullanmaktadır. **TensorFlow** ve **Streamlit** kullanılarak oluşturulmuştur ve erişilebilir:

🌐 [https://agegenderprediction-furkansukan.streamlit.app/](https://agegenderprediction-furkansukan.streamlit.app/)

---

## 🛠️ **Kullanılan Teknolojiler** 🔧

- **Python Kütüphaneleri** 📚:
  - `streamlit` 🖥️
  - `tensorflow` 🤖
  - `PIL (Pillow)` 📸
  - `numpy` 🔢

---

## 📝 **Kurulum ve Çalıştırma Talimatları** 📦

### 1️⃣ **Depoyu Clone’la** 🔄

```bash
git clone https://github.com/yourusername/age-gender-prediction.git
```

### 2️⃣ **Gerekli Paketleri Yükle** 🔌

```bash
pip install streamlit tensorflow Pillow numpy
```

### 3️⃣ **Uygulamayı Çalıştır** 🚀

Streamlit uygulamasını yerel olarak başlat:

```bash
streamlit run app.py
```

### 4️⃣ **Bir Resim Yükle 📷**

- Arayüz üzerinden yüz resmini yükle.
- Model, anlık olarak **yaşı, cinsiyeti** ve **etnisiteyi** tahmin eder! 🔍

---

## 📊 **Model Yapısı** 🧠

```python
model = tf.keras.Sequential([
    L.InputLayer(input_shape=(48, 48, 1)),
    L.Conv2D(32, (3, 3), activation='relu'),
    L.BatchNormalization(),
    L.MaxPooling2D((2, 2)),
    L.Conv2D(64, (3, 3), activation='relu'),
    L.MaxPooling2D((2, 2)),
    L.Flatten(),
    L.Dense(64, activation='relu'),
    L.Dropout(rate=0.5),
    L.Dense(1, activation='sigmoid')
])

model.compile(optimizer='sgd',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])
```

### ⏱️ **Erken Durdurma CallBack** 🔥

Validation kaybı **0.2700** değerine ulaştığında eğitim otomatik olarak durur.

---

## 📅 **Dataset Hakkında** 🔍

### 📖 **Dataset Bilgisi** 📜

- Dataset, yüz resimlerinden **yaş, cinsiyet** ve **etnisite** gibi bilgileri içeriyor.
- UTK datasetinden alınmış ve pek çok kaynak üzerinden temizlenerek bir **CSV formatına** uygun hale getirilmiştir.

### 📊 **Dataset Yapısı** 📜

- **27305 satır**
- **5 sütun**  
  Yaş, cinsiyet, etnisite, ve yüz verilerini içerir.

### 🙌 **Teşekkürler** 🙏

- Orijinal JPEG dosyaları, **Kaggle** platformundan alınmıştır. 🕵️‍♂️

## 📞 İletişim
If you have any questions or suggestions, feel free to reach out to me:

Feel free to reach out for questions or feedback via:
- **Email:** [furkansukan10@gmail.com](furkansukan10@gmail.com)
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/furkansukan/)
- **Kaggle:** [Kaggle Profile](https://www.kaggle.com/furkansukan)
- **Website:** [Project Website](https://agegenderprediction-furkansukan.streamlit.app/)
