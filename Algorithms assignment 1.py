#Fatima Khan
#100812028
# Class: Algorithms & Data Structure
# Assignment: 1

#using linked lists to manage products

#product class
class Product:
    def __init__(self, product_id, name, price, category):
        #initializing the product attributes
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        #pointer to the next product in the linked list
        self.next = None  

#creating a linked list of products with given details

#ProductList Class
class ProductList:
    def __init__(self):
        #initialize the head of the linked list to None
        self.head = None  

    def __iter__(self):
        #start from the head of the list
        current = self.head  
        while current:
            #yield the current product
            yield current  
            #move to the next product
            current = current.next  

#to insert, update, delete, and search products

    def insert(self, product_id, name, price, category):
        #create a new product
        new_product = Product(product_id, name, price, category) 
        if not self.head:
            #if the list is empty, set the new product as the head
            self.head = new_product 
        else:
            current = self.head
            while current.next:
                #shifts to the end of the list
                current = current.next 
                #append the new product at the end
            current.next = new_product 

    def display(self):
        #start from the head of the list
        current = self.head  
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Price: {current.price}, Category: {current.category}")
            #moves to the next product
            current = current.next  

#reads product data from file and stors it in linked list

def load_product_data(filename):
    #creates an empty product list
    products = ProductList()  
    #opens the file in read mode
    with open(filename, 'r') as file:  
        for line in file:
            #splits the line into product attributes
            product_id, name, price, category = line.strip().split(", ")  
            #inserts the product into the list
            products.insert(int(product_id), name, float(price), category) 
    #return the product list         
    return products  

#testing the loading and display function

if __name__ == "__main__":
    #loading products from the file
    products = load_product_data("product_data.txt")  
    #displays the loaded products
    products.display()  



class Product:
    def __init__(self, product_id, name, price, category):
        #initialize the product attributes
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        #pointer to the next product in the linked list
        self.next = None  

class ProductList:
    def __init__(self):
        #initializing the head of the linked list to None
        self.head = None  

    def load_from_file(self, filename):
        #opens the file in read mode
        with open(filename, 'r') as file:  
            for line in file:
                #splits the line into product attributes
                product_id, name, price, category = line.strip().split(", ")  
                #insert the product into the list
                self.insert(int(product_id), name, float(price), category)  

    def insert(self, product_id, name, price, category):
        #createa a new product
        new_product = Product(product_id, name, price, category) 
        if not self.head:
             #if the list is empty, set the new product as the head
            self.head = new_product 
        else:
            current = self.head
            while current.next:
                #shift to the end of the list
                current = current.next 
            #append the new product at the end    
            current.next = new_product  

    def update(self, product_id, new_name, new_price, new_category):
        #start from the head of the list
        current = self.head  
        while current:
            #find the product by ID
            if current.product_id == product_id: 
                #update product name
                current.name = new_name  
                #update product price
                current.price = new_price  
                #update product category
                current.category = new_category  
                #exit the loop once the product is updated
                break  
            #move to the next product
            current = current.next  

    def delete(self, product_id):
        if not self.head:
             #if the list is empty, return
            return 

        if self.head.product_id == product_id:
            #if the head is the product to delete, move the head
            self.head = self.head.next  
            return

        prev = None
        current = self.head
        while current:
            #find the product by ID
            if current.product_id == product_id:  
                #removes the product by updating the previous product's next pointer
                prev.next = current.next  
                #exits the loop once the product is deleted
                break  
            #moves to the next product
            prev = current  
            current = current.next

    def search(self, product_id):
        #start from the head of the list
        current = self.head 
        while current:
            #finds the product by ID
            if current.product_id == product_id:  
                #returns the found product
                return current  
            #move to the next product
            current = current.next  
        #return None if the product is not found
        return None  

#bubble sort algorithm

    def bubble_sort_by_price(self):
        if not self.head:
            #if the list is empty, return None
            return None  
        #creates a new empty product list for sorting
        sorted_list = ProductList()  
        current = self.head
        while current:
            #insert products into the sorted list
            sorted_list.insert(current.product_id, current.name, current.price, current.category)  
            current = current.next

        sorted_head = None
        while sorted_list.head:
            #get the minimum price node
            min_node = self._get_min_node(sorted_list)  
            if not sorted_head:
                #sets the sorted head if not set
                sorted_head = min_node 
                #sets the sorted tail 
                sorted_tail = min_node  
            else:
                 #append the minimum node to the sorted list
                sorted_tail.next = min_node 
                #update the sorted tail 
                sorted_tail = min_node  
            #removes the minimum node from the unsorted list
            sorted_list.delete(min_node.product_id)  

        return sorted_head

    def _get_min_node(self, product_list):
        #assume the first product is the minimum
        min_node = product_list.head  
        current = product_list.head.next
        while current:
            if current.price < min_node.price:  
                #updates the minimum node if a lower price is found
                min_node = current
            current = current.next
        return min_node

#method for complexity analysis
    def bubble_sort_time_complexity(self, n):
        #best case: List is already sorted
        best_case_operations = n - 1  
        print(f"Best Case Time Complexity: O({best_case_operations})")

        #average case: Random order
        average_case_operations = (n * (n - 1)) // 2  
        print(f"Average Case Time Complexity: O({average_case_operations})")

        #worst case: List is in reverse order
        worst_case_operations = (n * (n - 1)) // 2  
        print(f"Worst Case Time Complexity: O({worst_case_operations})")

    def display(self):
        #start from the head of the list
        current = self.head  
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Price: {current.price}, Category: {current.category}")
            #move to the next product
            current = current.next  

#test the operations with user input
if __name__ == "__main__":
    products = ProductList()

    #load products from the file
    products.load_from_file("product_data.txt")  

    while True:
        print("\n1. Insert Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Display Products")
        print("6. Display Products Sorted by Price")
        print("7. Complexity Analysis")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            category = input("Enter Product Category: ")
            products.insert(product_id, name, price, category)
            print("Product added successfully.")
            products.display()
        elif choice == '2':
            product_id = int(input("Enter Product ID to update: "))
            name = input("Enter new Product Name: ")
            price = float(input("Enter new Product Price: "))
            category = input("Enter new Product Category: ")
            products.update(product_id, name, price, category)
            print("Product updated successfully.")
            products.display()
        elif choice == '3':
            product_id = int(input("Enter Product ID to delete: "))
            products.delete(product_id)
            print("Product deleted successfully.")
            products.display()
        elif choice == '4':
            product_id = int(input("Enter Product ID to search: "))
            found_product = products.search(product_id)
            if found_product:
                print(f"Product found - Name: {found_product.name}, Price: {found_product.price}, Category: {found_product.category}")
            else:
                print("Product not found.")
        elif choice == '5':
            print("Products:")
            products.display()
        elif choice == '6':
            sorted_head = products.bubble_sort_by_price()
            if sorted_head:
                sorted_products = ProductList()
                sorted_products.head = sorted_head
                print("Products sorted by price:")
                sorted_products.display()
            else:
                print("No products to sort.")
        elif choice == '7':
            #performing complecity analysis
            n = 0
            current = products.head
            while current:
                n += 1
                current = current.next
            products.bubble_sort_time_complexity(n)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
#end of code:)


