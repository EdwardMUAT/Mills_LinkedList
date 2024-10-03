class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Current website: {self.current.data}")
        elif self.current and self.current.next is None:
            print("You are at the end of the list.")

    def go_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Current website: {self.current.data}")
        elif self.current and self.current.prev is None:
            print("You are at the beginning of the list.")

    def delete_item(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                if temp == self.tail:
                    self.tail = temp.prev
                if temp == self.current:
                    self.current = self.head
                print(f"Deleted {data} from the list.")
                return
            temp = temp.next
        print(f"{data} not found in the list.")

    def find_item(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print(f"Found {data} in the list.")
                return temp
            temp = temp.next
        print(f"{data} not found in the list.")
        return None

def menu():
    websites = LinkedList()

    # Add 20 initial websites
    default_websites = [
        "https://www.google.com", "https://www.youtube.com", "https://www.wikipedia.org", 
        "https://www.amazon.com", "https://www.facebook.com", "https://www.twitter.com", 
        "https://www.instagram.com", "https://www.linkedin.com", "https://www.netflix.com", 
        "https://www.github.com", "https://www.stackoverflow.com", "https://www.reddit.com", 
        "https://www.medium.com", "https://www.twitch.tv", "https://www.quora.com", 
        "https://www.bing.com", "https://www.yahoo.com", "https://www.nytimes.com", 
        "https://www.cnn.com", "https://www.forbes.com"
    ]
    
    for site in default_websites:
        websites.append(site)

    while True:
        print("\nMenu:")
        print("1. Display the list")
        print("2. Go forward and display the webpage")
        print("3. Go backward and display the webpage")
        print("4. Add another item to the list")
        print("5. Delete an item from the list")
        print("6. Find an item in the list")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            websites.display_list()
        elif choice == '2':
            websites.go_forward()
        elif choice == '3':
            websites.go_backward()
        elif choice == '4':
            new_site = input("Enter the URL to add: ")
            websites.append(new_site)
            print(f"Added {new_site} to the list.")
        elif choice == '5':
            delete_site = input("Enter the URL to delete: ")
            websites.delete_item(delete_site)
        elif choice == '6':
            search_site = input("Enter the URL to find: ")
            websites.find_item(search_site)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
menu()
