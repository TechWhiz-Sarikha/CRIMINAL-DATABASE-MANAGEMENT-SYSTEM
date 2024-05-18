import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('criminal_management_system.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS criminals
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER,
              crime TEXT,
              sentence TEXT)''')
conn.commit()

st.title("Criminal DataBase Management System ")

st.sidebar.title("Navigation")
menu = ["Add Criminal", "View Criminals", "Update Criminal", "Delete Criminal"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Criminal":
    st.subheader("Add Criminal")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    crime = st.text_input("Crime")
    sentence = st.text_input("Sentence")

    if st.button("Add Criminal"):
        c.execute("INSERT INTO criminals (name, age, crime, sentence) VALUES (?, ?, ?, ?)",
                  (name, age, crime, sentence))
        conn.commit()
        st.success("Criminal added successfully!")

elif choice == "View Criminals":
    st.subheader("View Criminals")
    c.execute("SELECT * FROM criminals")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Crime", "Sentence"])
    st.dataframe(df)

elif choice == "Update Criminal":
    st.subheader("Update Criminal")

    id = st.number_input("Enter ID of the criminal to update", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    crime = st.text_input("Crime")
    sentence = st.text_input("Sentence")

    if st.button("Update Criminal"):
        c.execute("UPDATE criminals SET name = ?, age = ?, crime = ?, sentence = ? WHERE id = ?",
                  (name, age, crime, sentence, id))
        conn.commit()
        st.success("Criminal updated successfully!")

elif choice == "Delete Criminal":
    st.subheader("Delete Criminal")

    id = st.number_input("Enter ID of the criminal to delete", min_value=1, step=1)

    if st.button("Delete Criminal"):
        c.execute("DELETE FROM criminals WHERE id = ?", (id,))
        conn.commit()
        st.success("Criminal deleted successfully!")

conn.close()
