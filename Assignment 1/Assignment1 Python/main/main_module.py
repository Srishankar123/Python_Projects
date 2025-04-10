from dao.customer_dao import CustomerDAO
from entity.customer import Customer
from exception.user_defined_exception import (
    CustomerNotFoundException,
    ProductNotFoundException,
    InventoryNotFoundException,
    OrderNotFoundException
)
from dao.products_dao import ProductDAO
from dao.inventory_dao import InventoryDAO
from dao.orders_dao import OrderDAO
from dao.order_details_dao import Order_Details_DAO




class MainModule:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        self.products_dao = ProductDAO()
        self.inventory_dao = InventoryDAO()
        self.orders_dao = OrderDAO()
        self.order_details_dao= Order_Details_DAO()

    def print_menu(self):
        print("\n========== TechShop Menu ==========")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Total Orders By This Customer")
        print("6. Get Product Details")
        print("7. Update Product Info")
        print("8. Check Product Stock")
        print("9. Calculate Total Amount")
        print("10. Get Order Details")
        print("11. Subtotal For OrderDetail")
        print("12. Get Order Detail Info")
        print("13. Update Quantity in Order")
        print("14. Add Discount to Order")
        print("15. Get Product from Inventory")
        print("16. Get Quantity in Stock")
        print("17. Add to Inventory")
        print("18. Remove from Inventory")
        print("19. Update Stock Quantity")
        print("20. Check Product Availability")
        print("21. Get Total Inventory Value")
        print("22. List Low Stock Products")
        print("23. List Out-of-Stock Products")
        print("24. List All Products with Stock")
        print("25. Exit")

        return int(input("Enter your choice: "))

    def run(self):
        while True:
            choice = self.print_menu()
            #In Customer Table Funcs
            try:
                if choice == 1:
                    customer_id = int(input("Enter Customer ID: "))
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    email = input("Email: ")
                    phone = input("Phone: ")
                    address = input("Address: ")
                    cust = Customer(customer_id, first_name, last_name, email, phone, address)
                    self.customer_dao.create_customer(cust)
                    print("✅ Customer added successfully!")

                elif choice == 2:
                    customer_id = int(input("Enter Customer ID: "))
                    customer = self.customer_dao.read_customer(customer_id)
                    if not customer:
                        raise CustomerNotFoundException()
                    print("✅ Customer Details:")
                    print(customer.__dict__)

                elif choice == 3:
                    customer_id = int(input("Enter Customer ID: "))
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    email = input("Email: ")
                    phone = input("Phone: ")
                    address = input("Address: ")
                    cust = Customer(customer_id, first_name, last_name, email, phone, address)
                    self.customer_dao.update_customer(cust)
                    print("✅ Customer updated successfully!")

                elif choice == 4:
                    customer_id = int(input("Enter Customer ID: "))
                    self.customer_dao.delete_customer(customer_id)
                    print("✅ Customer deleted successfully!")


                elif choice == 5:
                    customer_id = int(input("Enter Customer ID: "))
                    total_orders = self.customer_dao.calculate_total_orders(customer_id)
                    print(f"📊 Total orders placed by customer {customer_id}: {total_orders}")

                # In Products Table Func
                elif choice == 6:
                    product_id = int(input("Enter Product ID: "))
                    product = self.products_dao.get_product_details(product_id)
                    print("📦 Product Details:")
                    print(f"ID: {product.product_id}")
                    print(f"Name: {product.product_name}")
                    print(f"Description: {product.description}")
                    print(f"Price: ₹{product.price}")


                elif choice == 7:
                    product_id = int(input("Enter Product ID: "))
                    new_price = float(input("Enter new price: "))
                    new_description = input("Enter new description: ")
                    self.products_dao.update_product_info(product_id, new_price, new_description)


                elif choice == 8:
                    product_id = int(input("Enter Product ID: "))
                    in_stock = self.inventory_dao.is_product_in_stock(product_id)
                    if in_stock:
                        print(f"✅ Product {product_id} is in stock.")
                    else:
                        print(f"❌ Product {product_id} is out of stock.")

                # For Order TAble Func

                elif choice == 9:
                    order_id = int(input("Enter Order ID: "))
                    total_amount = self.orders_dao.calculate_total_amount(order_id)
                    print(f"🧾 Total Amount for Order {order_id}: ₹{total_amount}")


                elif choice == 10:
                    order_id = int(input("Enter Order ID: "))
                    order_details = self.orders_dao.get_order_details(order_id)
                    print(f"📦 Order Details for Order ID {order_id}:")
                    for detail in order_details:
                        print(
                            f"🔹 Product: {detail[1]}, Quantity: {detail[2]}, Price: ₹{detail[3]}, Subtotal: ₹{detail[4]}")

                elif choice == 11:
                    order_id = int(input("Enter Order ID: "))
                    product_id = int(input("Enter Product ID: "))
                    subtotal = self.order_details_dao.calculate_subtotal(order_id, product_id)
                    print(f"🧾 Subtotal for Product {product_id} in Order {order_id}: ₹{subtotal}")

                elif choice == 12:
                    order_detail_id = int(input("Enter Order Detail ID: "))
                    detail = self.order_details_dao.get_order_detail_info(order_detail_id)
                    print("📦 Order Detail Info:")
                    for key, val in detail.items():
                        print(f"{key}: {val}")

                elif choice == 13:
                    order_detail_id = int(input("Enter Order Detail ID: "))
                    new_quantity = int(input("Enter New Quantity: "))
                    self.order_details_dao.update_quantity(order_detail_id, new_quantity)
                    print("✅ Quantity updated successfully.")

                elif choice == 14:
                    order_detail_id = int(input("Enter Order Detail ID: "))
                    discount = float(input("Enter Discount Percentage (%): "))
                    result = self.order_details_dao.add_discount(order_detail_id, discount)
                    print("🧾 Discount Applied:")
                    for key, val in result.items():
                        print(f"{key}: ₹{val:.2f}")


                elif choice == 15:
                    product_id = int(input("Enter Product ID: "))
                    product = self.inventory_dao.get_product(product_id)
                    print("📦 Product from Inventory:")
                    print(f"ID: {product.product_id}")
                    print(f"Name: {product.product_name}")
                    print(f"Description: {product.description}")
                    print(f"Price: ₹{product.price}")

                elif choice == 16:
                    product_id = int(input("Enter Product ID: "))
                    quantity = self.inventory_dao.get_quantity_in_stock(product_id)
                    print(f"📦 Quantity in stock for Product {product_id}: {quantity}")

                elif choice == 17:
                    product_id = int(input("Enter Product ID: "))
                    add_qty = int(input("Enter quantity to add to inventory: "))
                    self.inventory_dao.add_to_inventory(product_id, add_qty)


                elif choice == 18:
                    product_id = int(input("Enter Product ID: "))
                    remove_qty = int(input("Enter quantity to remove: "))
                    self.inventory_dao.remove_from_inventory(product_id, remove_qty)
                    print(f"✅ Removed {remove_qty} units from inventory.")

                elif choice == 19:
                    product_id = int(input("Enter Product ID: "))
                    new_qty = int(input("Enter new stock quantity: "))
                    self.inventory_dao.update_stock_quantity(product_id, new_qty)
                    print(f"✅ Inventory updated to {new_qty} units for Product {product_id}.")

                elif choice == 20:
                    product_id = int(input("Enter Product ID: "))
                    check_qty = int(input("Enter quantity to check availability for: "))
                    available = self.inventory_dao.is_product_available(product_id, check_qty)
                    if available:
                        print(f"✅ {check_qty} units are available in inventory.")
                    else:
                        print(f"❌ Only limited stock available. {check_qty} units not in stock.")


                elif choice == 21:
                    value = self.inventory_dao.get_inventory_value()
                    print(f"💰 Total Inventory Value: ₹{value:.2f}")

                elif choice == 22:
                    threshold = int(input("Enter stock threshold: "))
                    low_stock = self.inventory_dao.list_low_stock_products(threshold)
                    if low_stock:
                        print("📉 Low Stock Products:")
                        for product in low_stock:
                            print(f"ProductID: {product[0]}, Name: {product[1]}, Stock: {product[2]}")
                    else:
                        print("✅ All products are above the threshold.")

                elif choice == 23:
                    out_of_stock = self.inventory_dao.list_out_of_stock_products()
                    if out_of_stock:
                        print("❌ Out-of-Stock Products:")
                        for product in out_of_stock:
                            print(f"ProductID: {product[0]}, Name: {product[1]}")
                    else:
                        print("✅ No products are out of stock.")


                elif choice == 24:
                    products = self.inventory_dao.list_all_products()
                    if products:
                        print("📦 All Products in Inventory:")
                        for prod in products:
                            print(f"ProductID: {prod[0]}, Name: {prod[1]}, Quantity in Stock: {prod[2]}")
                    else:
                        print("📭 No products found in inventory.")


                elif choice == 25 :
                    print("👋 Exiting TechShop... Goodbye!")
                    break

                else:
                    print("❌ Invalid choice. Please try again.")
            except CustomerNotFoundException as ce:
                    print("⚠️", ce)
            except ProductNotFoundException as pe:
                print("⚠️", pe)
            except InventoryNotFoundException as ie:
                print("⚠️", ie)
            except OrderNotFoundException as oe:
                print("⚠️", oe)
            except Exception as e:
                print("❌ Error:", e)




if __name__ == '__main__':
    app = MainModule()
    app.run()






