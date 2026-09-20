import requests
import streamlit as st

st.title("✨ AI Astrologer - भविष्य जानें ✨")

user_query = st.text_input("अपना सवाल यहाँ लिखें:")

if st.button("भविष्य जानें ✨"):
  if user_query:
    webhook_url = (
        "https://rani-gupta.app.n8n.cloud/webhook/5c173db2-0142-4389-af48-18f13e346c7f"
    )

    try:
      response = requests.post(webhook_url, json={"question": user_query})

      if response.status_code == 200:
        res_data = response.json()

        # यहाँ हम n8n के पूरे जंजाल में से सिर्फ काम का जवाब ढूंढ रहे हैं
        if isinstance(res_data, dict):
          # अगर जवाब 'response' या 'output' के अंदर है
          astrology_output = (
              res_data.get("response")
              or res_data.get("output")
              or res_data.get("body", {}).get("response")
              or str(res_data)
          )
        else:
          astrology_output = str(res_data)

        st.success("भविष्यवाणी:")
        st.write(astrology_output)
      else:
        st.error(f"एरर आ गया: {response.status_code}")

    except Exception as e:
      st.error(f"कुछ गड़बड़ हो गई: {e}")
  else:
    st.warning("कृपया पहले अपना सवाल लिखें!")
      
