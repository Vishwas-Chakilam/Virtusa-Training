import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# basic config for the page
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰", layout="wide")

# names for my storage and categores
db_file = "expenses.csv"
choices = ["Food", "Travel", "Bills", "Shopping", "Entertainment", "Health", "Other"]

# making sure the file exists when we start
if not os.path.exists(db_file):
    df_init = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df_init.to_csv(db_file, index=False)

def read_file():
    # just reading the csv back
    return pd.read_csv(db_file)

def add_entry(dt, cat, amt, info):
    # adding a row to our csv
    df = read_file()
    new_row = pd.DataFrame([[dt, cat, amt, info]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(db_file, index=False)

# CSS for the look of the app
st.markdown("""
<style>
    .stApp { background-color: #f0f2f6; }
    .heading { font-size: 2.2rem; font-weight: 700; color: #1e3a8a; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="heading">💰 Expense Tracker App</div>', unsafe_allow_html=True)

# sidebar to add stuff
data_df = read_file()
with st.sidebar:
    st.header("Add New Item")
    with st.form("my_form", clear_on_submit=True):
        sel_date = st.date_input("Date", datetime.now())
        sel_cat = st.selectbox("Pick Category", choices)
        sel_amt = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        sel_desc = st.text_input("Note")
        
        btn = st.form_submit_button("Save Expense")
        if btn:
            add_entry(sel_date.strftime("%Y-%m-%d"), sel_cat, sel_amt, sel_desc)
            st.success("Saved!")
            st.rerun()

    st.markdown("---")
    st.header("Download Area")
    if not data_df.empty:
        # exporting logic
        my_csv = data_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Export transactions (CSV)",
            data=my_csv,
            file_name=f"my_expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
    else:
        st.write("Nothing to download yet.")

# main part of the screen
if data_df.empty:
    st.info("The list is empty. Add something using the sidebar!")
else:
    # fixing the dates
    data_df['Date'] = pd.to_datetime(data_df['Date'])
    data_df['Month'] = data_df['Date'].dt.strftime('%B %Y')

    # summary numbers
    col_a, col_b, col_c = st.columns(3)
    sum_total = data_df['Amount'].sum()
    top_cat = data_df.groupby('Category')['Amount'].sum().idxmax()
    top_val = data_df.groupby('Category')['Amount'].sum().max()
    daily_avg = sum_total / len(data_df['Date'].unique())

    with col_a:
        st.metric("Total Spent", f"${sum_total:,.2f}")
    with col_b:
        st.metric("Biggest Spender", top_cat, f"${top_val:,.2f}")
    with col_c:
        st.metric("Daily Avg", f"${daily_avg:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    # display tabs
    t1, t2, t3 = st.tabs(["Charts", "History", "Monthly"])

    with t1:
        st.subheader("Visual Analysis")
        left, right = st.columns(2)
        
        with left:
            st.write("**Where's the money going?**")
            grouped = data_df.groupby('Category')['Amount'].sum()
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=140)
            ax.axis('equal')
            st.pyplot(fig)

        with right:
            st.write("**Daily Spending Trend**")
            daily_data = data_df.groupby('Date')['Amount'].sum().reset_index()
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            ax2.plot(daily_data['Date'], daily_data['Amount'], marker='x', color='blue')
            plt.xticks(rotation=45)
            st.pyplot(fig2)

    with t2:
        st.subheader("Raw Data")
        st.dataframe(data_df.sort_values(by='Date', ascending=False)[["Date", "Category", "Amount", "Description"]], width="stretch")

    with t3:
        st.subheader("By Month")
        months = data_df.groupby('Month')['Amount'].sum().reset_index()
        st.bar_chart(data=months, x="Month", y="Amount")

st.markdown("---")
st.caption("Smart Expense Tracker")
