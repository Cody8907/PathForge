
import streamlit as st

career_map = {
    "Python": "Data Science",
    "Statistics": "Data Science",
    "Creativity": "UI/UX Design",
    "Design Tools": "UI/UX Design",
    "Math": "Quant / Finance",
    "Problem Solving": "Software Development",
}


roadmaps = {
    "Data Science": [
        ("Learn Python + Libraries", "https://www.learnpython.org/"),
        ("Master Statistics & Probability", "https://www.khanacademy.org/math/statistics-probability"),
        ("Study Machine Learning", "https://www.coursera.org/learn/machine-learning"),
        ("Build Projects & Portfolio", "https://github.com/topics/data-science-projects"),
    ],
    "UI/UX Design": [
        ("Learn Design Principles", "https://www.interaction-design.org/"),
        ("Master Figma / Adobe XD", "https://www.figma.com/resources/learn-design/"),
        ("Practice Wireframes & Prototypes", "https://www.adobe.com/products/xd.html"),
        ("Build a Portfolio", "https://www.behance.net/"),
    ],
    "Quant / Finance": [
        ("Learn Advanced Math & Probability", "https://ocw.mit.edu/courses/mathematics/"),
        ("Understand Financial Markets", "https://www.investopedia.com/markets-4427704"),
        ("Study Algorithms & Trading Systems", "https://www.quantstart.com/"),
        ("Backtest Strategies", "https://www.backtrader.com/"),
    ],
    "Software Development": [
        ("Learn Programming Fundamentals", "https://www.w3schools.com/"),
        ("Understand OOP Concepts", "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/"),
        ("Practice DSA & Problem Solving", "https://leetcode.com/"),
        ("Build Apps / Web Projects", "https://github.com/topics/web-development-project"),
    ]
}


st.set_page_config(page_title="PathForge-AI Career Advisor Prototype", layout="centered")
st.title("AI Career Advisor Prototype")
st.write("Helping students map skills → careers → learning paths")


skills = st.multiselect("Select your skills:", list(career_map.keys()))

if st.button(" Get Career Path"):
    if not skills:
        st.warning("Please select at least one skill.")
    else:
        
        chosen_career = career_map[skills[0]]
        st.success(f" Recommended Career: **{chosen_career}**")

        st.write("###  Roadmap & Resources:")
        for step, link in roadmaps[chosen_career]:
            st.markdown(f"- **{step}** → [Resource]({link})")

        st.info("This is a prototype. In the final product, recommendations will be AI-driven.")


st.write("---")
st.subheader(" Career Q&A Chatbot (Prototype)")

user_question = st.text_input("Ask me a question about careers:")

if user_question:
    
    st.write("**Answer:** (Prototype response) Based on your interests, explore free online courses and projects to strengthen your portfolio.")
    st.caption(" In final version, this will be powered by AI (LLM).")
