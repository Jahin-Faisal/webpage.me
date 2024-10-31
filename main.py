import requests
import streamlit as st
from streamlit_lottie import st_lottie
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# Define the scopes
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# Load credentials
credentials = Credentials.from_service_account_file(
    'credentials.json', scopes=scopes)

# Authorize the client
gc = gspread.authorize(credentials)

# Open the sheet
sheet = gc.open("webdatas").sheet1  # Ensure this matches your actual Google Sheet name

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_coding = load_lottieurl("https://lottie.host/ee847879-e163-4edf-a752-7a6c0f6f1a63/68azfYNcDD.json")
lottie_new = load_lottieurl("https://lottie.host/0abc754c-c54d-4aab-898b-9923552d577c/W7Ya6JpC22.json")
lottie_new2 = load_lottieurl("https://lottie.host/107d5cda-01d8-4784-a219-29cbecfd7470/0JQ7cIjRh7.json")

# Date handling functions
def get_days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

def format_age_unit(value, unit):
    return f"{value} {unit}" if value == 1 else f"{value} {unit}s"

# Append to Google Sheets
def append_to_google_sheet(content):
    try:
        sheet.append_row(content)
        st.success("Data successfully added to Google Sheets!")
    except Exception as e:
        st.error(f"Failed to append data to Google Sheets: {e}")

# Main App Content
with st.container():
    st.header("Hello, Welcome to this Exciting Page!")
    st.write(
        """A bunch of programs are here to entertain you! You can explore new customized helpful features here, too! So, without wasting any more time let's get started!"""
    )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do here")
        st.write("In very shortly :-")
        st.write("##")
        st.write(
            """
            - You can simply find out your age by entering your date of birth (DOB)!
            - You can find out any day by the date!
            - You can see how strong your password is!
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300)

with st.container():
    st.write("---")
    st.header("Program 01: Age Calculator")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Enter your DOB below:")

        a1 = st.text_input("Year : ", placeholder="maximum this year")
        a2 = st.selectbox("Month : ", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        month_names = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }

        if a1:
            try:
                year_input = int(a1)
                month_number = month_names[a2]
                days_in_month = get_days_in_month(year_input, month_number)
                day_options = list(range(1, days_in_month + 1))
            except ValueError:
                st.error("Please enter a valid year.")
                day_options = []
        else:
            day_options = list(range(1, 32))

        a3 = st.selectbox("Day : ", day_options)
        button = st.button("Calculate Age")

        current_year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day

        if button and a3 and a2 and a1:
            try:
                cd = int(a3)
                bc = month_number
                ab = int(a1)

                # Age calculation logic
                day = (current_day - cd) % 30
                month = (current_month - bc) % 12
                year = current_year - ab - ((current_month < bc) or (current_month == bc and current_day < cd))

                if day < 0:
                    day += get_days_in_month(current_year, current_month - 1)
                if month < 0:
                    month += 12

                # Constructing age message
                age_parts = []
                if year > 0:
                    age_parts.append(format_age_unit(year, 'year'))
                if month > 0:
                    age_parts.append(format_age_unit(month, 'month'))
                if day > 0:
                    age_parts.append(format_age_unit(day, 'day'))

                age_message = "Your age is " + ", ".join(age_parts) + "."
                st.success(age_message)

                # Append age message to Google Sheets
                append_to_google_sheet([a1, a2, a3, age_message])

            except ValueError:
                st.error("Please enter valid inputs.")

    with right_column:
        st_lottie(lottie_new, height=400)

with st.container():
    st.write("---")
    st.header("Program 02: Day Finder")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Enter any date below:")

        a11 = st.text_input("Year of the date: ", placeholder="minimum the year 1900")
        B = st.selectbox("Month of the date: ", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        B = month_names[B]
        if a11:
            try:
                a11 = int(a11)
                if a11 < 1900:
                    st.error("Please enter a year greater than or equal to 1900.")
                    day_options = []
                else:
                    days_in_month = get_days_in_month(a11, B)
                    day_options = list(range(1, days_in_month + 1))
            except ValueError:
                st.error("Please enter a valid year.")
                day_options = []
        else:
            day_options = list(range(1, 32))

        a33 = st.selectbox("Day of the date: ", day_options)
        button = st.button("Get the Day!")

        if button and a33 and a11:
            try:
                year = int(a11)
                e = year % 4
                d = year - 1900

                if e == 0:
                    f = (d // 4) - 1
                else:
                    f = (d - e) // 4

                G_values = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
                G = G_values[B - 1]

                h = d + f + a33 + G
                i = h % 7

                days_of_week = [
                    "Saturday", "Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday"
                ]
                day_message = f"The day was {days_of_week[i]}."
                st.success(day_message)

                # Append day message to Google Sheets
                append_to_google_sheet([a11, B, a33, day_message])

            except ValueError:
                st.error("Invalid input! Please make sure to enter valid data.")

    with right_column:
        st_lottie(lottie_new2, height=400)

with st.container():
    st.write("---")
    st.subheader("Thanks for using the app!")
