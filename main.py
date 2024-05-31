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


def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_new = load_lottieurl2("https://lottie.host/0abc754c-c54d-4aab-898b-9923552d577c/W7Ya6JpC22.json")

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
        st.subheader("Enter you DOB below:")

        a1 = st.text_input("Year : ")
        a2 = st.text_input("Month : ")
        a3 = st.text_input("Day : ")

        Button = st.button("Done")

        current_year = datetime.now().year
        ry = int(current_year)

        current_month = datetime.now().month
        rm = int(current_month)

        current_day = datetime.now().day
        rd = int(f"{current_day:02d}")

        global month
        global day
        global year

        if a3 and a2 and a1:
            try:
                cd = int(a3)
                bc = int(a2)
                ab = int(a1)

                if cd > rd:
                    ab2 = (rd+30) - cd
                else:
                    ab2 = rd - cd

                day = str(ab2)

                if cd > rd and bc < rm:
                    bc2 = rm - (bc + 1)
                elif cd > rd and bc > rm:
                    bc2 = (rm + 12) - (bc + 1)
                elif bc > rm:
                    bc2 = (rm + 12) - bc
                else:
                    bc2 = (rm - bc)

                month = str(bc2)

                if bc > rm:
                    cd2 = (ry - (ab + 1))
                else:
                    cd2 = (ry - ab)

                year = str(cd2)

            except ValueError:
                st.error()

            if Button:
                if year == 0:
                    st.write("Your age is " + month + " month and " + day + " day")
                elif month == 0:
                    st.write("Your age is " + year + " year and " + day + " day")
                elif day == 0:
                    st.write("Your age is " + year + " year and " + month + " month")
                else:
                    st.write("Your age is " + year + " year " + month + " month and " + day + " day")

    with right_column:
        st_lottie(lottie_new, height=300)
