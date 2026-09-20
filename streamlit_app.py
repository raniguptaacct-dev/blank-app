import requests
import streamlit as st

st.title("✨ AI Astrologer - भविष्य जानें ✨")

# यूजर से सवाल पूछने का बॉक्स
user_query = st.text_input(
    "अपना सवाल यहाँ लिखें:", "Mera naam Rani Gupta hai mera bhavishya bataiye"
)

if st.button("भविष्य जानें ✨"):
  if user_query:
    # n8n वेबहुक का यूआरएल
    webhook_url = (
        "https://rani-gupta.app.n8n.cloud/webhook/5c173db2-0142-4389-af48-18f13e346c7f"
    )

    try:
      # वेबहुक पर डेटा भेजना
      response = requests.post(webhook_url, json={"query": user_query})

      if response.status_code == 200:
        data = response.json()

        # यहाँ हम सीधे उस 'output' या जवाब को निकाल रहे हैं जो AI ने भेजा है
        # अगर डेटा किसी डिक्शनरी या लिस्ट के रूप में है, तो उसे यहाँ संभाल लेंगे
        if isinstance(data, dict):
          astrology_result = data.get("response") or data.get(
              "output", str(data)
          )
        else:
          astrology_result = str(data)

        # स्क्रीन पर सिर्फ साफ-सुथरा ज्योतिषीय जवाब दिखेगा
        st.success("भविष्यवाणी:")
        st.write(astrology_result)
      else:
        st.error(
            f"सर्वर से कनेक्ट करने में दिक्कत आ रही है (Error Code:"
            f" {response.status_code})"
        )

    except Exception as e:
      st.error(f"कुछ गड़बड़ हो गई है: {e}")
  else:
    st.warning("कृपया पहले अपना सवाल लिखें!")
      
