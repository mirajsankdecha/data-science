# Product Inventory Management
inventory = {}

while True:
    print("\n--- Product Inventory Management System ---")
    print("1. Add Product Details")
    print("2. Display All Products")
    print("3. Find Product by ID")
    print("4. List Products by Category")
    print("5. Update Product Details")
    print("6. Delete Product")
    print("7. Check if Product ID Exists")
    print("8. Copy Product Dictionary")
    print("9. Merge Product Dictionaries")
    print("10. Create Dictionary from Lists (IDs and Prices)")
    print("11. Add New Field to Product Record")
    print("12. Exit")

    choice = input("Enter your choice (1-12): ")

    if choice == "1":  # Add Product
        prod_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        quantity = input("Enter Quantity: ")
        price = input("Enter Price: ")
        inventory[prod_id] = {'name': name, 'category': category, 'quantity': quantity, 'price': price}
        print("Product added.")
    
    elif choice == "2":  # Display All Products
        for prod_id, details in inventory.items():
            print(f"ID: {prod_id}, Name: {details['name']}, Category: {details['category']}, Quantity: {details['quantity']}, Price: {details['price']}")
    
    elif choice == "3":  # Find Product by ID
        prod_id = input("Enter Product ID to search: ")
        if prod_id in inventory:
            print(f"ID: {prod_id}, Details: {inventory[prod_id]}")
        else:
            print("Product not found.")
    
    elif choice == "4":  # List Products by Category
        category = input("Enter Category: ")
        for prod_id, details in inventory.items():
            if details['category'] == category:
                print(f"ID: {prod_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")
    
    elif choice == "5":  # Update Product Details
        prod_id = input("Enter Product ID to update: ")
        if prod_id in inventory:
            print("What to update? (name/category/quantity/price)")
            field = input("Enter field: ")
            if field in inventory[prod_id]:
                new_value = input(f"Enter new {field}: ")
                inventory[prod_id][field] = new_value
                print(f"{field.capitalize()} updated.")
            else:
                print("Invalid field.")
        else:
            print("Product not found.")
    
    elif choice == "6":  # Delete Product
        prod_id = input("Enter Product ID to delete: ")
        if prod_id in inventory:
            del inventory[prod_id]
            print("Product deleted.")
        else:
            print("Product not found.")
    
    elif choice == "7":  # Check if Product ID Exists
        prod_id = input("Enter Product ID: ")
        if prod_id in inventory:
            print("Product ID exists.")
        else:
            print("Product ID does not exist.")
    
    elif choice == "8":  # Copy Product Dictionary
        inventory_copy = inventory.copy()
        print("Product dictionary copied.")
    
    elif choice == "9":  # Merge Product Dictionaries
        other_inventory = {}
        num_entries = int(input("Enter number of products for the second dictionary: "))
        for i in range(num_entries):
            prod_id = input(f"Enter Product ID {i+1}: ")
            name = input("Enter Name: ")
            category = input("Enter Category: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")
            other_inventory[prod_id] = {'name': name, 'category': category, 'quantity': quantity, 'price': price}
        inventory.update(other_inventory)
        print("Product dictionaries merged.")
    
    elif choice == "10":  # Create Dictionary from Lists
        ids = input("Enter Product IDs (comma-separated): ").split(",")
        prices = input("Enter Prices (comma-separated): ").split(",")
        new_dict = dict(zip(ids, prices))
        print("New dictionary created:", new_dict)
    
    elif choice == "11":  # Add New Field to Product
        prod_id = input("Enter Product ID: ")
        if prod_id in inventory:
            field = input("Enter new field (e.g., expiry date): ")
            value = input(f"Enter value for {field}: ")
            inventory[prod_id][field] = value
            print(f"Added {field} to Product ID {prod_id}.")
        else:
            print("Product not found.")
    
    elif choice == "12":  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
