import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# O'zingizning bot tokeningizni kiriting
bot = Bot(token="")
dp = Dispatcher()

class Restaran:
    def __init__(self):
        self.menu_items = {}
        self.book_tables = []
        self.orders = []

    def add_menu_item(self, item, price):
        """Adds a menu item with its price."""
        self.menu_items[item] = price
        return self.print_menu_items()

    def book_table(self, number):
        """Books a table by its number."""
        if number not in self.book_tables:
            self.book_tables.append(number)
            return f"Table {number} has been booked."
        else:
            return f"Table {number} is already booked."

    def costume_orders(self, meal, soni):
        """Records an order for a specific meal and quantity."""
        self.orders.append([meal, soni])

    def print_tables(self):
        """Returns a string representation of all booked tables."""
        result = "Booked Tables:\n"
        for table in self.book_tables:
            result += f"Table {table}\n"
        return result

    def print_orders(self):
        """Returns a string representation of all orders placed."""
        result = "Orders:\n"
        for order in self.orders:
            result += f"{order[0]}: {order[1]} ordered.\n"
        return result

    def print_menu_items(self):
        """Returns a string representation of the menu items."""
        result = "Menu Items:\n"
        for menu_item, price in self.menu_items.items():
            result += f'{menu_item}: {price} UZS\n'
        return result

    def __len__(self):  # len(class)
        return len(self.book_tables)

    def __getitem__(self, number):  # emp1[0]
        return self.book_tables[number]

    def __setitem__(self, number, value):  # emp1[0] = 5
        if value not in self.book_tables: 
            current_value = self.book_tables[number]
            # Replace the old value only if it's currently booked
            if current_value in self.book_tables: 
                self.book_tables[number] = value
                return f"Table {current_value} replaced with Table {value}."
        else:
            return f"Table {value} is already booked."

# Create an instance of Restaran
restaurant = Restaran()

# Add menu items
restaurant.add_menu_item("sho'rva", 50000)
restaurant.add_menu_item("mastava", 20000)
restaurant.add_menu_item("osh", 100000)
restaurant.add_menu_item("kabob", 5000)
restaurant.add_menu_item("salad", 5000)
restaurant.add_menu_item("ko'k choy", 1000)
restaurant.add_menu_item("qora choy", 1000)

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    # Print menu items when /start command is issued
    menu_text = restaurant.print_menu_items()
    await message.answer(menu_text)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == '__main__':
    asyncio.run(main())
