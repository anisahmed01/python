# bank.py
import json
import random
import string
from pathlib import Path


class Bank:
    DB_PATH = Path("data.json")
    data = []

    # basic storage 

    @classmethod
    def load(cls):
        """Load data.json into Bank.data."""
        if cls.DB_PATH.exists():
            try:
                cls.data = json.loads(cls.DB_PATH.read_text())
            except json.JSONDecodeError:
                # Corrupt file -> start clean
                cls.data = []
        else:
            cls.data = []

    @classmethod
    def save(cls):
        """Save Bank.data into data.json."""
        cls.DB_PATH.write_text(json.dumps(cls.data, indent=2))

    # helpers 

    @classmethod
    def _generate_account_no(cls) -> str:
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    @classmethod
    def _find_user(cls, account_no: str, pin: str):
        for user in cls.data:
            if user["accountNo"] == account_no and user["pin"] == pin:
                return user
        return None

    #  core operations (create, deposit, withdraw, get_details,update_details, delete_account

    @classmethod
    def create_account(cls, name: str, age: int, email: str, pin: str):
        """Create account and return (success, message, account_dict or None)."""
        if age < 18:
            return False, "Age must be 18 or above.", None

        # PIN as *string* to preserve leading zeros like '0123'
        if not pin.isdigit() or len(pin) != 4:
            return False, "PIN must be a 4-digit number.", None

        account_no = cls._generate_account_no()
        account = {
            "Name": name,
            "age": age,
            "email": email,
            "pin": pin,          # stored as string
            "accountNo": account_no,
            "balance": 0,
        }

        cls.data.append(account)
        cls.save()
        return True, "Account created successfully.", account

    @classmethod
    def deposit(cls, account_no: str, pin: str, amount: int):
        """Deposit money. Returns (success, message)."""
        user = cls._find_user(account_no, pin)
        if user is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."
        if amount > 10000:
            return False, "You can deposit a maximum of 10000 at a time."

        user["balance"] += amount
        cls.save()
        return True, f"Deposited {amount} successfully. New balance: {user['balance']}"

    @classmethod
    def withdraw(cls, account_no: str, pin: str, amount: int):
        """Withdraw money. Returns (success, message)."""
        user = cls._find_user(account_no, pin)
        if user is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."
        if amount > 10000:
            return False, "You can withdraw a maximum of 10000 at a time."
        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount
        cls.save()
        return True, f"Withdrew {amount} successfully. New balance: {user['balance']}"

    @classmethod
    def get_details(cls, account_no: str, pin: str):
        """Get account details. Returns (success, message, user_dict or None)."""
        user = cls._find_user(account_no, pin)
        if user is None:
            return False, "Invalid account number or PIN.", None

        # Return a copy so caller can't accidentally mutate internals
        return True, "Account details fetched.", user.copy()

    @classmethod
    def update_details(cls, account_no: str, pin: str, name=None, email=None, new_pin=None):
        """
        Update name/email/pin. Pass None for fields you don't want to change.
        Returns (success, message).
        """
        user = cls._find_user(account_no, pin)
        if user is None:
            return False, "Invalid account number or PIN."

        if name:
            user["Name"] = name
        if email:
            user["email"] = email
        if new_pin:
            if not new_pin.isdigit() or len(new_pin) != 4:
                return False, "New PIN must be a 4-digit number."
            user["pin"] = new_pin

        cls.save()
        return True, "Details updated successfully."

    @classmethod
    def delete_account(cls, account_no: str, pin: str):
        """Delete account. Returns (success, message)."""
        user = cls._find_user(account_no, pin)
        if user is None:
            return False, "Invalid account number or PIN."

        cls.data.remove(user)
        cls.save()
        return True, "Account deleted successfully."
