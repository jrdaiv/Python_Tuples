# traveler name
# origin aka home
# destination
# make sure it loops thru lists
# print a formated string for each

itinerary = [{"Alice", "New York", "London"}, {"Bob", "Tokyo", "San Francisco"}]

def flight_tix(itinerary):
    for i, info in enumerate(itinerary):
        traveler_name, origin, destination = info
        print(f"Itinerary {i}: {traveler_name} - From {origin} - To {destination}")
        
flight_tix(itinerary)





