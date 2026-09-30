#15. Create items = ['mobile', 'laptop', 'tablet'] and budget = 50000. If laptop is available and budget is at least 40000, print You can buy laptop; otherwise print Cannot buy laptop.

items = ['mobile', 'laptop', 'tablet']
budget = 50000

if 'laptop' in items and budget > 40000:
    print("You can buy a Laptop")
else:
    print("Not")