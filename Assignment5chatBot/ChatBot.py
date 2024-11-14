class RestaurantChatbot:
    def __init__(self):
        self.menu = {"burger": 5.99, "pizza": 8.99, "pasta": 7.99, "salad": 4.99}
        self.order = {}

    def greet_user(self):
        print("Chatbot: Welcome to our restaurant!")

    def show_menu(self):
        print("Chatbot: Here's our menu:")
        for item, price in self.menu.items():
            print(f"{item.title()}: ${price:.2f}")

    def take_order(self, item):
        if item in self.menu:
            self.order[item] = self.order.get(item, 0) + 1
            print(f"Chatbot: Added {item.title()} to your order.")
        else:
            print("Chatbot: Item not found.")

    def show_order_summary(self):
        if not self.order:
            print("Chatbot: Your order is empty.")
        else:
            print("Chatbot: Your order summary:")
            total = sum(self.menu[item] * qty for item, qty in self.order.items())
            for item, qty in self.order.items():
                print(f"{item.title()} x {qty}: ${self.menu[item] * qty:.2f}")
            print(f"Total: ${total:.2f}")

    def process_input(self, user_input):
        user_input = user_input.lower()
        if "menu" in user_input:
            self.show_menu()
        elif "order" in user_input:
            item = user_input.split("order ")[-1]
            self.take_order(item)
        elif "summary" in user_input:
            self.show_order_summary()
        elif "bye" in user_input:
            print("Chatbot: Thank you! Goodbye!")
            return False
        else:
            print("Chatbot: Please ask about the menu, place an order, or view the summary.")
        return True

if __name__ == "__main__":
    chatbot = RestaurantChatbot()
    chatbot.greet_user()
    while True:
        user_input = input("You: ")
        if not chatbot.process_input(user_input):
            break