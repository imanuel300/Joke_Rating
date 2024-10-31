import streamlit as st
import database as db

# הגדרות העמוד
st.set_page_config(
    page_title="דירוג בדיחות 😄",
    page_icon="🎭",
    layout="wide"
)

# CSS מותאם אישית - אותו CSS כמו בדף הראשי
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700;900&display=swap');
    
    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
    }
    
    /* הדר */
    .header {
        background: linear-gradient(135deg, #1a5f7a, #0d2b36);
        padding: 40px 20px;
        margin: -80px -80px 40px -80px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    /* כותרות */
    .header h1 {
        color: white;
        font-weight: 900;
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header h3 {
        color: #a8d8ea;
        font-weight: 500;
        font-size: 1.5rem;
        margin-bottom: 0;
    }
    
    /* עיצוב הטופס */
    .stTextArea textarea {
        font-size: 1.2rem;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #e1e8ed;
        direction: rtl;
    }
    
    .stButton>button {
        background: #1a5f7a;
        color: white;
        border-radius: 12px;
        padding: 15px 25px;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        background: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(26, 95, 122, 0.2);
    }

    /* התאמה למובייל */
    @media (max-width: 768px) {
        .header {
            margin: -20px -20px 20px -20px;
            padding: 30px 15px;
        }
        
        .header h1 {
            font-size: 2rem;
        }
        
        .header h3 {
            font-size: 1.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# כותרת ראשית בתוך הדר
st.markdown("""
<div class="header">
    <h1>🎭 מערכת דירוג בדיחות</h1>
    <h3>😄 מקום מושלם לדרג בדיחות!</h3>
</div>
""", unsafe_allow_html=True)

# כפתורי ניווט
col1, col2 = st.columns(2)
with col1:
    if st.button("📊 בדיחות קיימות", use_container_width=True):
        st.switch_page("app.py")
with col2:
    if st.button("🎯 הוספת בדיחה", use_container_width=True, type="primary"):
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# טופס הוספת בדיחה
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.form("new_joke_form", clear_on_submit=True):
        joke_content = st.text_area(
            "הכניסו את הבדיחה שלכם כאן:",
            height=150,
            placeholder="כתבו כאן את הבדיחה שלכם...",
            key="joke_input"
        )
        
        submitted = st.form_submit_button(
            "שליחת הבדיחה ✨",
            use_container_width=True,
            type="primary"
        )
        
        if submitted and joke_content.strip():
            joke_id = db.add_joke(joke_content)
            st.success("הבדיחה נוספה בהצלחה! 🎉")
            st.balloons()
            
            # מעבר לדף הראשי
            st.switch_page("app.py")