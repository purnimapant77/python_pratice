#Cinema ticket pricing
print("**Cinema ticket pricing system**")

age=int(input("Enter your age:"))
day=input("Enter the day of week:").strip().lower()
member=input("Are you a member of the cinema club? (yes/no):").strip().lower()
is_member=member=="yes"
full_price=500

if age < 5:
    category = "Child"
    age_discount = 100
elif age < 18:
    category = "Minor"
    age_discount = 50
elif age >= 60:
    category = "Senior"
    age_discount = 30
else:
    category = "Adult"
    age_discount = 0
price = full_price - (full_price * age_discount / 100)
weekday_discount = 0
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}
if is_member and day in weekdays:
    weekday_discount = 10
    price -= price * 0.10
if age < 5:
    popcorn_offer = "No popcorn needed (free entry)"
else:
    if is_member:
        popcorn_offer = "Large Free Popcorn"
    else:
        popcorn_offer = "Small Free Popcorn"

message = "Free Entry!" if price == 0 else "Enjoy the Show!"

# Output
print("\n***** Ticket Summary *****")
print("Category:", category)
print("Age Discount:", age_discount, "%")
print("Extra Discount:", weekday_discount, "%")
print("Popcorn Offer:", popcorn_offer)
print("Final Price: Rs.", round(price, 2))
print(message)
