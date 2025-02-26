import streamlit as st

st.set_page_config(page_title="First Assignment", page_icon="🪴")  # For example  
st.title = ("Growth Mindset challenge")

st.header("🌻 Welcome to your Growth Journey!")
st.write("This journey explores the idea that abilities can be developed through dedication and effort. You'll engage in activities that foster self-reflection, goal-setting, and resilience, empowering you to embrace challenges and learn from experiences. Get ready to cultivate a mindset focused on growth and continuous improvement!")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not an accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do.")


st.header("What’s your challenge today? 🌱💪✨")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f" 🥅You're facing {user_input}. Keep Pushing forward towards your goal!🚀")
else:
  st.warning("Tell us challenge to get started!")


#Reflexing
st.header("🧠 Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
   st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
   st.info("Reflection On past Experience help you grow! share your difficulties")


#achievements
st.header("🎉 Celebrate Your Wins!")  
achievement = st.text_input("Share something you've recently accomplished:")  

if achievement:  
    st.success(f"🎊 Amazing! You achieved: {achievement}")  
else:  
    st.info("Big or small, every achievement counts! 🎈 Share it now! 💪")  

#footer
st.write("- - -")
st.write("Believe in yourself and your journey. Every step you take, no matter how small, brings you closer to your goals. 🌟 Keep pushing forward, embrace challenges, and remember: growth happens outside your comfort zone. You've got this! 💪✨")
st.write("©️ Created by Muhammad Ashhad Khan")
