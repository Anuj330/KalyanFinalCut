import os
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KalyanFinalCut.settings")  # Replace "your_project" with the actual name of your Django project

# Import settings to initialize Django
settings._setup()

# Now you can import your models and run your functions
from .models import User, Payment
if __name__ == "__main__":
    def create_payments():
        print("Function is running...")
        users = User.objects.all()

        if users.exists():
            for user in users:
                user_details = user.userdetails_set.first()

                if user_details:
                    print("User exists:", user)
                    # Create payment entries for different months
                    for i in range(1, 13):
                        month = f'2023-{i:02d}-01'
                        print(f"Creating payment entry for {user} in {month}")
                        Payment.objects.create(
                            host=user,
                            Month=month,
                            Name=user_details.Name,
                            # Add other fields as needed
                        )
                else:
                    print("User details do not exist for:", user)
        else:
            print("No users exist.")



if __name__ == "__main__":
    create_payments()
