# CRUD
from .db_connection import connect_db
from datetime import datetime

# Create new data (C)
def new_data():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        cursor = conn.cursor()

        while True:
            print("\nInput new data based on the column order:")

            # Get and validate order date
            while True:
                try:
                    order_date = input("Order date (Format: YYYY-MM-DD): ")
                    if not order_date:
                        print("No input provided. Please try again.")
                        continue
                    datetime.strptime(order_date, "%Y-%m-%d")  # date format validation
                    break
                except ValueError:
                    print("Wrong format. Please use YYYY-MM-DD format.")

            # Get customer name
            while True:
                customer_name = input("Customer name (Full name): ")
                if not customer_name:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get gender
            while True:
                gender = input("Gender (Male/Female): ")
                if not gender:
                    print("Wrong input. Please try again.")
                    continue
                break

            # Get and validate age
            while True:
                try:
                    age = int(input("Age: "))
                    if age > 100:
                        print("Please input right age.")
                        continue
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            # Get brand
            while True:
                brand = input("Brand: ")
                if not brand:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get product
            while True:
                product = input("Product: ")
                if not product:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get category
            while True:
                category = input("Category: ")
                if not category:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get and validate quantity
            while True:
                try:
                    quantity = int(input("Quantity: "))
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            # Get and validate unit price
            while True:
                try:
                    unit_price = float(input("Unit price: "))
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            # Get and validate discount percent
            while True:
                try:
                    discount_percent = int(input("Discount (%): "))
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            # Get and validate shipping cost
            while True:
                try:
                    shipping_cost = float(input("Shipping cost: "))
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            total_amount = round(
                (unit_price * quantity) * (1 - discount_percent / 100) + shipping_cost, 2
            )

            # Get payment method
            while True:
                payment_method = input(
                    "Payment method (ShopeePay/OVO/Gopay/Bank Transfer/Credit Card): "
                )
                if not payment_method:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get sales channel
            while True:
                sales_channel = input("Sales channel (Shopee/Tokopedia/Lazada/Blibli): ")
                if not sales_channel:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get and validate customer rating
            while True:
                try:
                    customer_rating = int(input("Customer rating (1,2,3,4,5): "))
                    break
                except ValueError:
                    print("Wrong format. Please enter a valid number.")

            # Get city
            while True:
                city = input("City: ")
                if not city:
                    print("No input provided. Please try again.")
                    continue
                break

            # Get province
            while True:
                province = input("Province: ")
                if not province:
                    print("No input provided. Please try again.")
                    continue
                break

            query = """
        INSERT INTO data_transaction_ecommerce
        (order_date, customer_name, gender, age, brand, product, category, quantity, unit_price, discount_percent, shipping_cost, total_amount, payment_method, sales_channel, customer_rating, city, province)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
            data = (
                order_date,
                customer_name,
                gender,
                age,
                brand,
                product,
                category,
                quantity,
                unit_price,
                discount_percent,
                shipping_cost,
                total_amount,
                payment_method,
                sales_channel,
                customer_rating,
                city,
                province,
            )

            cursor.execute(query, data)
            conn.commit()
            print("Data successfully inserted!")
            break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Delete data from certain rows (D)
def delete_data():
    conn = None
    cursor = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cust_id_del = int(input("Input transaction ID that you want to delete: "))
        cursor.execute(
            "DELETE FROM data_transaction_ecommerce WHERE transaction_id = %s",
            (cust_id_del,),
        )
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Transaction ID no. {cust_id_del} has been deleted.")
        else:
            print("Transaction ID not found")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_menu():
    while True:
        print(
            """
====================
    UPDATE MENU
====================
1. Insert new data
2. Delete a row
3. Exit
"""
        )
        choice = input("Select option: ").strip()
        if choice == "1":
            new_data()
        elif choice == "2":
            delete_data()
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    update_menu()