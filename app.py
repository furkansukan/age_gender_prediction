import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Modeli yükleme
age_model = tf.keras.models.load_model('age.h5')
gender_model = tf.keras.models.load_model('gender_fixed.h5')
ethnicity_model = tf.keras.models.load_model('ethnicity_fixed.h5')

# Sayfa başlığı
st.title('Photo Prediction Page')
st.write('Upload a photo and we will predict age, gender, and ethnicity.')

# Fotoğraf yükleme
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Fotoğrafı yükleme ve ön işleme
    image = Image.open(uploaded_image).convert("L")  # Gri tonlama
    image = image.resize((48, 48))  # Resize to 48x48
    image_array = np.array(image) / 255.0  # Normalize etme (0-1 arası)

    # Shape'i model gerekliliklerine uygun hale getirme
    image_array = image_array.reshape(1, 48, 48, 1)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Modellerden tahmin yapma
    age_prediction = age_model.predict(image_array)[0][0]
    gender_prediction = gender_model.predict(image_array)[0][0]
    ethnicity_prediction = ethnicity_model.predict(image_array)[0][0]

    # Sonuçları gösterme
    st.write(f"### Predictions")
    st.write(f"Age: {int(age_prediction)} years")
    st.write(f"Gender: {'Female' if gender_prediction > 0.5 else 'Male'}")

    ethnicity_map = {
        0: "Asyalı",
        1: "Afrikalı",
        2: "Avrupalı",
        3: "Güney Amerikalı",
        4: "Okyanusyalı"
    }
    ethnicity_prediction = int(ethnicity_prediction)  # Prediction değerini integer yap

    # Dictionary üzerinden kıtayı bul ve Streamlit'e yazdır
    if ethnicity_prediction in ethnicity_map:
        st.write(f"Ethnicity: {ethnicity_map[ethnicity_prediction]}")
    else:
        st.write(f"Ethnicity: {ethnicity_map.get(ethnicity_prediction, 'Dünyalı')}")
        st.write('---')
        st.write('Şaka tabi, nereli olduğunu bulamadık!')