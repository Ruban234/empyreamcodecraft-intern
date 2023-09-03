import random


def generate_otp():
    return str(random.randint(100000, 999999))


def send_email(email, message):
    print(f"Sending OTP to {email}: {message}")


def main():
    
    otp = generate_otp()
    
    
    user_email = input("Enter your email: ")
    
    
    send_email(user_email, f"Your OTP is: {otp}")
    
    
    user_entered_otp = input("Enter the OTP you received: ")
    
    
    if user_entered_otp == otp:
        print("OTP verified successfully. Registration/payment process can proceed.")
    else:
        print("OTP verification failed. Please try again.")

if __name__ == "__main__":
    main()
