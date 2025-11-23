# app.py
import streamlit as st
from bank import Bank

# Load data from JSON on each run
Bank.load()

st.title("Bank Account Management")

menu = st.sidebar.selectbox(
    "Select Action",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

# Create Account 

if menu == "Create Account":
    st.header("Create New Account")
    with st.form("create_account_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, step=1)
        email = st.text_input("Email")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        success, message, account = Bank.create_account(
            name=name,
            age=int(age),
            email=email,
            pin=pin,
        )
        if success:
            st.success(message)
            st.write("Your account details:")
            st.json(account)
        else:
            st.error(message)

#Deposit Money

elif menu == "Deposit Money":
    st.header("Deposit Money")
    with st.form("deposit_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount", min_value=1, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        success, message = Bank.deposit(acc_no, pin, int(amount))
        if success:
            st.success(message)
        else:
            st.error(message)

#Withdraw Money

elif menu == "Withdraw Money":
    st.header("Withdraw Money")
    with st.form("withdraw_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount", min_value=1, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        success, message = Bank.withdraw(acc_no, pin, int(amount))
        if success:
            st.success(message)
        else:
            st.error(message)

# Show Details 

elif menu == "Show Details":
    st.header("Show Account Details")
    with st.form("details_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Show Details")

    if submitted:
        success, message, user = Bank.get_details(acc_no, pin)
        if success:
            st.success(message)
            st.json(user)
        else:
            st.error(message)

# Update Details 

elif menu == "Update Details":
    st.header("Update Account Details")
    with st.form("update_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("Current PIN", type="password", max_chars=4)
        new_name = st.text_input("New Name (leave blank to keep current)")
        new_email = st.text_input("New Email (leave blank to keep current)")
        new_pin = st.text_input(
            "New PIN (leave blank to keep current)", type="password", max_chars=4
        )
        submitted = st.form_submit_button("Update")

    if submitted:
        name_arg = new_name.strip() or None
        email_arg = new_email.strip() or None
        pin_arg = new_pin.strip() or None

        success, message = Bank.update_details(
            account_no=acc_no,
            pin=pin,
            name=name_arg,
            email=email_arg,
            new_pin=pin_arg,
        )
        if success:
            st.success(message)
        else:
            st.error(message)

#  Delete Account

elif menu == "Delete Account":
    st.header("Delete Account")
    with st.form("delete_form"):
        acc_no = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox("I confirm that I want to delete this account.")
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        if not confirm:
            st.warning("You must confirm deletion.")
        else:
            success, message = Bank.delete_account(acc_no, pin)
            if success:
                st.success(message)
            else:
                st.error(message)
