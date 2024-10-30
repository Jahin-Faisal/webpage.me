import requests
import streamlit as st
from streamlit_lottie import st_lottie
from datetime import datetime


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/ee847879-e163-4edf-a752-7a6c0f6f1a63/68azfYNcDD.json")
lottie_new = load_lottieurl("https://lottie.host/0abc754c-c54d-4aab-898b-9923552d577c/W7Ya6JpC22.json")
lottie_new2 = load_lottieurl("https://lottie.host/107d5cda-01d8-4784-a219-29cbecfd7470/0JQ7cIjRh7.json")


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
    if value == 1:
        return f"{value} {unit}"
    else:
        return f"{value} {unit}s"


def wt(content):
    with open("inpt.txt", "a") as file:
        file.write(content + "\n")


with st.container():
    st.header("Hello, Welcome to this Exciting Page!")
    st.write("""A bunch of programs are here to entertain you! You can explore new customized helpful features here, too! So, without wasting anymore time let's get started!!!""")

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
            - You can see how strong is your password!
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300)

with st.container():
    st.write("---")
    st.header("Program 01")
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
        Button = st.button("Done")

        current_year = datetime.now().year
        ry = int(current_year)

        current_month = datetime.now().month
        rm = int(current_month)

        current_day = datetime.now().day
        rd = int(current_day)

        if a3 and a2 and a1:
            try:
                cd = int(a3)
                bc = month_number
                ab = int(a1)

                if cd > rd:
                    ab2 = (rd + 30) - cd
                else:
                    ab2 = rd - cd

                day = ab2

                if cd > rd and bc < rm:
                    bc2 = rm - (bc + 1)
                elif cd > rd and bc > rm:
                    bc2 = (rm + 12) - (bc + 1)
                elif bc > rm:
                    bc2 = (rm + 12) - bc
                else:
                    bc2 = (rm - bc)

                month = bc2

                if bc > rm:
                    cd2 = (ry - (ab + 1))
                else:
                    cd2 = (ry - ab)

                year = cd2

            except ValueError:
                st.error("Please enter valid inputs.")

            if Button:
                if year == 0:
                    age_message = f"Your age is {format_age_unit(month, 'month')} and {format_age_unit(day, 'day')}."
                elif month == 0:
                    age_message = f"Your age is {format_age_unit(year, 'year')} and {format_age_unit(day, 'day')}."
                elif day == 0:
                    age_message = f"Your age is {format_age_unit(year, 'year')} and {format_age_unit(month, 'month')}."
                else:
                    age_message = (f"Your age is {format_age_unit(year, 'year')}, "
                                   f"{format_age_unit(month, 'month')} and {format_age_unit(day, 'day')}.")

                st.success(age_message)
                wt(f"Day Finder: Year={a1}, Month={a2}, Day={a3}")

    with right_column:
        st_lottie(lottie_new, height=400)


with st.container():
    st.write("---")
    st.header("Program 02")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Enter any date below:")

        a11 = st.text_input("Year of the date: ", placeholder="minimum the year 1900")
        B = st.selectbox("Month of the date: ", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        month_names = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }

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
        Button = st.button("Get the day!")

        if Button:
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
                st.success(f"The day was {days_of_week[i]}")
                wt(f"Date Finder: Year={a11}, Month={B}, Day={a33}")

            except ValueError:
                st.error("Invalid input! Please make sure to enter valid data.")

    with right_column:
        st_lottie(lottie_new2, height=400)


with st.container():
    st.write("---")
    st.subheader("Coming more soon...")
