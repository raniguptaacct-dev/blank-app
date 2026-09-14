import streamlit as st
import requests

st.title("✨ AI Astrologer - भविष्य जानें ✨")

# यूजर से सवाल पूछने के लिए इनपुट बॉक्स
user_question = st.text_input("अपना सवाल यहाँ लिखें:")

if st.button("भविष्य जानें ✨"):
    if user_question:
        with st.spinner("ज्योतिष गणना की जा रही है..."):
            # आपका n8n वेबहुक लिंक
            webhook_url = "https://rani-gupta.app.n8n.cloud/webhook/5c173db2-0142-4389-af48-18f13e346c7f"
            
            try:
                # n8n को डेटा भेजना
                response = requests.post(webhook_url, json={"question": user_question})
                
                # रिस्पोंस को पढ़ना
                res_data = response.json()
                
                # केवल 'response' वाली चाबी (Key) का टेक्स्ट निकालना
                if isinstance(res_data, dict) and "response" in res_data:
                    st.success("✨ भविष्यवाणी:")
                    st.write(res_data["response"])
                else:
                    st.write(res_data)
                    
            except Exception as e:
                st.error(f"त्रुटि आई है: {e}")
    else:
        st.warning("कृपया पहले अपना सवाल लिखें!")
        
