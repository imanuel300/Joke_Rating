import streamlit as st
import database as db
from datetime import datetime
import os
from dotenv import load_dotenv

# טעינת משתני סביבה
load_dotenv()

# אתחול מסד הנתונים
db.init_db()

# הגדרות הדף
st.set_page_config(
    page_title="דירוג בדיחות 😄",
    page_icon="🎭",
    layout="wide"
)

# CSS מותאם אישית
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700;900&display=swap');
    
    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
    }
    
    /* עיצוב כללי */
    .main {
        max-width: 1200px;
        margin: 0 auto;
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
    
    /* טאבים */
    .stTabs {
        margin-top: -20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 1.2rem;
        font-weight: 500;
        color: #1a5f7a;
        padding: 15px 30px;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        background: #1a5f7a;
    }
    
    /* כרטיס בדיחה */
    .joke-card {
        background: white;
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: none;
    }
    
    .joke-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.12);
    }
    
    .joke-content {
        font-size: 1.4rem;
        line-height: 1.8;
        color: #2C3E50;
        margin: 20px 0;
        padding: 30px;
        background: #f8fafc;
        border-radius: 15px;
        text-align: center;
        font-weight: 500;
    }
    
    /* מיכל דירוג */
    .rating-container {
        background: #f1f5f9;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }
    
    .rating-stars {
        font-size: 32px;
        margin: 15px 0;
        color: #f1c40f;
    }
    
    .rating-text {
        color: #34495E;
        font-size: 1.1rem;
        font-weight: 500;
        margin: 15px 0;
    }
    
    /* כפתורי דירוג */
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
    
    /* הודעות */
    .stSuccess {
        background: #2ecc71;
        color: white;
        padding: 15px;
        border-radius: 12px;
        font-weight: 500;
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
        
        .joke-card {
            padding: 20px;
            margin: 20px 5px;
        }
        
        .joke-content {
            font-size: 1.2rem;
            padding: 20px;
            line-height: 1.6;
        }
        
        .rating-stars {
            font-size: 28px;
        }
        
        .stButton>button {
            padding: 12px 20px;
            font-size: 1rem;
        }
    }

    /* תיקון למיקום הקונטיינר */
    .st-emotion-cache-zt5igj {
        position: relative;
        width: 100% !important;
        display: flex;
        -webkit-box-align: center;
        align-items: center;
        overflow: visible;
        margin: 0 !important;
        padding: 0 !important;
        left: unset;
    }

    /* במקרה שהקלאס משתנה */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* עיצוב כפתור מחיקה */
    .delete-button {
        background: #e74c3c !important;
        margin-top: 10px;
    }
    
    .delete-button:hover {
        background: #c0392b !important;
    }
    
    /* מודל אישור מחיקה */
    .delete-modal {
        background: rgba(0,0,0,0.8);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    
    .delete-modal button {
        margin: 10px;
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

# משתנה גלובלי לשמירת הטאב הנוכחי
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0

# בתחילת הקובץ, אחרי ההגדרות הראשוניות
if 'submitted_joke' not in st.session_state:
    st.session_state.submitted_joke = False

# כפתורי ניווט במקום טאבים
col1, col2 = st.columns(2)
with col1:
    if st.button("📊 בדיחות קיימות", use_container_width=True, type="primary"):
        st.query_params.clear()
        st.rerun()
with col2:
    if st.button("🎯 הוספת בדיחה", use_container_width=True):
        st.switch_page("pages/add_joke.py")

st.markdown("<hr>", unsafe_allow_html=True)

# תצוגת הבדיחות
jokes = db.get_all_jokes_with_ratings()

if not jokes:
    st.info("👋 עדיין אין בדיחות במערכת. היה הראשון להוסיף בדיחה!")

for joke in jokes:
    joke_id, content, avg_rating, rating_count = joke
    
    with st.container():
        st.markdown(f"""
        <div class="joke-card">
            <div class="joke-content">{content}</div>
            <div class="rating-container">
                <p class="rating-stars">{'⭐' * int(round(avg_rating)) if avg_rating > 0 else '☆☆☆☆☆'}</p>
                <p class="rating-text">דירוג ממוצע: {avg_rating:.1f}/5<br>({rating_count} דירוגים)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # התאמת הדירוג למובייל
        st.markdown('<div class="rating-text">דרג/י את הבדיחה:</div>', unsafe_allow_html=True)
        
        # יצירת כפתורי דירוג בשורה אחת
        col1, col2, col3, col4, col5 = st.columns(5)
        rating = None
        for i, col in [(1, col1), (2, col2), (3, col3), (4, col4), (5, col5)]:
            if col.button(f"{'⭐' * i}", key=f"star_{joke_id}_{i}", use_container_width=True):
                rating = i
        
        if rating:
            db.add_rating(joke_id, rating)
            st.success("תודה על הדירוג! 🌟")
            st.rerun()
        
        # כפתור מחיקה
        delete_key = f"delete_{joke_id}"
        confirm_key = f"confirm_{joke_id}"
        
        if delete_key not in st.session_state:
            st.session_state[delete_key] = False
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🗑️ מחק בדיחה", key=f"delete_button_{joke_id}", 
                       type="secondary", use_container_width=True):
                st.session_state[delete_key] = True
        
        # חלון אישור מחיקה
        if st.session_state[delete_key]:
            with st.container():
                st.markdown("""
                <div class="delete-modal">
                    <h3>האם את/ה בטוח/ה שברצונך למחוק את הבדיחה?</h3>
                    <p>פעולה זו אינה הפיכה</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("כן, מחק", key=f"confirm_delete_{joke_id}", 
                               type="primary", use_container_width=True):
                        db.delete_joke(joke_id)
                        st.success("הבדיחה נמחקה בהצלחה!")
                        st.rerun()
                with col2:
                    if st.button("ביטול", key=f"cancel_delete_{joke_id}", 
                               type="secondary", use_container_width=True):
                        st.session_state[delete_key] = False
                        st.rerun()

# בדיקה אם יש פרמטר tab בכתובת
if 'tab' in st.query_params and st.query_params['tab'] == 'jokes':
    st.query_params.clear()
    st.switch_page("app.py")