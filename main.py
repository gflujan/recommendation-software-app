from logo import logo
import restaurant_data as rd

input_prompt = '> '

def print_recommendations(list_of_restaurants):
   print("Here are the restaurants that fit your choice...\n")
   print('——————————————————————————————————————————\n')

   for idx, restaurant in enumerate(list_of_restaurants):
      print(f"Recommendation #{idx + 1}:\n")
      print(f"  Name: {restaurant[1]}")
      print(f"  Price: {restaurant[2]}/5")
      print(f"  Rating: {restaurant[3]}/5")
      print(f"  Address: {restaurant[4]}\n")
      print('——————————————————————————————————————————\n')
   # rof
# fed

def get_recommendations(selected_food_type):
   recommendations = []

   for restaurant in rd.restaurant_data:
      restaurant_type = restaurant[0]

      if restaurant_type == selected_food_type:
         recommendations.append(restaurant)
      # fi
   # rof

   print_recommendations(recommendations)
# fed

def select_food_type():
   print("Start by entering in the name or the beginning letters of a food type you're feeling.")
   available_food_types = []
   entered_food_type = input(input_prompt)

   for available_food_type in rd.types:
      if available_food_type == entered_food_type or available_food_type.startswith(
         entered_food_type):
         available_food_types.append(available_food_type)
      # fi
   # rof

   # TODO :: Create a 2nd conditional to handle only 1 `available_food_type`;
   # this would just display the one food type and ask the user if they want to see the restaurant recommendations for that one food type
   if len(available_food_types) > 0:
      print('\nHere are your available options:')
      available_food_types.sort()

      for idx, option in enumerate(available_food_types):
         position = idx + 1

         if position == len(available_food_types):
            print(f"{position}. {option}\n")
         else:
            print(f"{position}. {option}")
         # fi
      # rof
   else:
      print("Sorry, we couldn't find any options with that name. Please enter a new value.")
      select_food_type()
   # fi

   print("Enter the number of the food type you'd like to get recommendations for.")
   food_type_selection = input(input_prompt)
   print()
   get_recommendations(available_food_types[int(food_type_selection) - 1])
# fed

def start():
   print(logo)
   print("Welcome to my cool new restaurants recommendation software! Let's get started...\n")
   print('What is your name?')
   name = input(input_prompt)
   print()
   print(f"Hi {name}, nice to meet you! Let's figure out what you want to eat.\n")
   select_food_type()
   keep_searching = True

   while keep_searching:
      print("Would you like to search for more recommendations? Enter 'y' for yes and 'n' for no.")
      search_more = input(input_prompt)

      if search_more == 'y':
         print()
         select_food_type()
      else:
         keep_searching = False
         print()
         print('Thanks for using my cool new software! Bye!')
      # fi
   # elihw
# fed

start()
