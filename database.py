import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv('DB_PATH', 'jokes.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # יצירת טבלת בדיחות
    c.execute('''
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # יצירת טבלת דירוגים
    c.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke_id INTEGER,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (joke_id) REFERENCES jokes (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_joke(content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO jokes (content) VALUES (?)', (content,))
    joke_id = c.lastrowid
    conn.commit()
    conn.close()
    return joke_id

def add_rating(joke_id, rating):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO ratings (joke_id, rating) VALUES (?, ?)', (joke_id, rating))
    conn.commit()
    conn.close()

def get_all_jokes_with_ratings():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT j.id, j.content, 
               COALESCE(AVG(r.rating), 0) as avg_rating,
               COUNT(r.id) as rating_count
        FROM jokes j
        LEFT JOIN ratings r ON j.id = r.joke_id
        GROUP BY j.id
        ORDER BY j.created_at DESC
    ''')
    results = c.fetchall()
    conn.close()
    return results 