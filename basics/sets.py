active_users = {"user1", "user2", "user3", "user5"}
premium_users = {"user3", "user4", "user5", "user6"}

print(f"Both active and premium users:{active_users & premium_users}")
print(f"Unique accross both group combined:{active_users | premium_users}")
print(f"Active but not premium:{active_users-premium_users}")