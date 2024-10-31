# 🎭 Joke Rating | דירוג בדיחות

<div dir="rtl">

## 🌟 ברוכים הבאים לאפליקציית דירוג הבדיחות!

אפליקציה מהנה המאפשרת למשתמשים לשתף בדיחות ולדרג בדיחות של אחרים.

### 🔗 קישורים
- [צפייה באפליקציה](https://jokerating.streamlit.app/)
- [קוד המקור ב-GitHub](https://github.com/imanuel300/Joke_Rating)

### ✨ תכונות עיקריות
- 📝 הוספת בדיחות חדשות
- ⭐ דירוג בדיחות (1-5 כוכבים)
- 📊 צפייה בדירוג הממוצע
- 🎨 ממשק משתמש מודרני וידידותי
- 🌐 תמיכה מלאה בעברית

### 🚀 התקנה והפעלה

#### 1. הורדת הפרויקט
שכפל את המאגר למחשב שלך:

    git clone https://github.com/imanuel300/Joke_Rating.git
    cd Joke_Rating

#### 2. התקנת Python
וודא שמותקן Python ברסה 3.8 ומעלה. ניתן להוריד מ:
https://www.python.org/downloads/

#### 3. יצירת סביבה וירטואלית
צור והפעל סביבה וירטואלית:

במערכת Windows:

    python -m venv venv
    venv\Scripts\activate

במערכת Linux/Mac:

    python3 -m venv venv
    source venv/bin/activate

#### 4. התקנת הדרישות
התקן את חבילות Python הנדרשות:

    pip install --upgrade pip
    pip install -r requirements.txt

#### 5. הגדרת משתני סביבה
צור קובץ `.env` והוסף את השורות הבאות:

    DB_PATH=jokes.db
    SECRET_KEY=your_secret_key

#### 6. הפעלת האפליקציה
הפעל את האפליקציה:

    streamlit run app.py

האפליקציה תיפתח אוטומטית בדפדפן בכתובת:
http://localhost:8501

### 💻 טכנולוגיות

- **Frontend**: Streamlit
- **Database**: SQLite
- **Backend**: Python
- **Styling**: Custom CSS
- **Environment**: python-dotenv

### 🎯 שימוש באפליקציה

#### הוספת בדיחה חדשה
1. לחץ על טאב "הוספת בדיחה"
2. הכנס את הבדיחה שלך
3. לחץ על "שליחת הבדיחה"

#### דירוג בדיחות
1. עבור לטאב "בדיחות קיימות"
2. דרג בדיחות בסולם של 1-5 כוכבים
3. צפה בדירוג הממוצע ומספר המדרגים

### ⚠️ פתרון בעיות נפוצות

1. אם מופיעה שגיאת "pip not found":
   
       python -m ensurepip --default-pip

2. אם יש בעיה בהתקנת החבילות:
   
       pip install --upgrade setuptools wheel

3. אם האפליקציה לא נפתחת בדפדפן:
   פתח ידנית את הכתובת http://localhost:8501

### 📄 רישיון
MIT License - אתם מוזמנים להשתמש, לשנות ולהפיץ את הקוד בחופשיות

</div>