import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="AI Astrologer", page_icon="✨", layout="centered")

st.title("✨ AI Astrologer - भविष्य जानें ✨")

user_query = st.text_input(
    "अपना सवाल यहाँ लिखें:",
    placeholder="जैसे: मेरा आने वाला समय कैसा रहेगा?",
)

if st.button("भविष्य जानें ✨"):
  if user_query:
    try:
      genai.configure(
          api_key="AQ.Ab8RN6JIaJ7bB1qKTszmV9x_Y-FrtZirvgFLZAkXH_48vjshtw"
      )

      # यहाँ मॉडल का नाम अपडेट कर दिया गया है
      model = genai.GenerativeModel("gemini-2.5-flash")

      prompt = (
          f"You are an expert AI astrologer. Give a detailed, positive, and"
          f" inspiring astrological prediction for the following query: {user_query}"
      )

      with st.spinner("भविष्य की गणना की जा रही है..."):
        response = model.generate_content(prompt)
        astrology_result = response.text

      st.success("भविष्यवाणी:")
      st.write(astrology_result)

    except Exception as e:
      st.error(
          f"कुछ गड़बड़ हो गई है। कृपया API Key चेक करें या दोबारा कोशिश करें:"
          f" {e}"
      )
  else:
    st.warning("कृपया पहले अपना सवाल लिखें!")
    
