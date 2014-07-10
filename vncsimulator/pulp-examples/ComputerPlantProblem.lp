\* Computer Plant Problem *\
Minimize
Total_Costs: 5 Route_San_Francisco_San_Diego + 3 Route_San_Francisco_Barstow
 + 2 Route_San_Francisco_Tucson + 6 Route_San_Francisco_Dallas
 + 4 Route_Los_Angeles_San_Diego + 7 Route_Los_Angeles_Barstow
 + 8 Route_Los_Angeles_Tucson + 10 Route_Los_Angeles_Dallas
 + 6 Route_Phoenix_San_Diego + 5 Route_Phoenix_Barstow
 + 3 Route_Phoenix_Tucson + 8 Route_Phoenix_Dallas + 9 Route_Denver_San_Diego
 + 8 Route_Denver_Barstow + 6 Route_Denver_Tucson + 5 Route_Denver_Dallas
 + 70000 BuildaPlant_San_Francisco + 70000 BuildaPlant_Los_Angeles
 + 65000 BuildaPlant_Phoenix + 70000 BuildaPlant_Denver
Subject To
Sum_of_Products_into_Stores_Barstow: Route_San_Francisco_Barstow
 + Route_Los_Angeles_Barstow + Route_Phoenix_Barstow + Route_Denver_Barstow
 >= 1000
Sum_of_Products_into_Stores_Dallas: Route_San_Francisco_Dallas
 + Route_Los_Angeles_Dallas + Route_Phoenix_Dallas + Route_Denver_Dallas
 >= 1200
Sum_of_Products_into_Stores_San_Diego: Route_San_Francisco_San_Diego
 + Route_Los_Angeles_San_Diego + Route_Phoenix_San_Diego
 + Route_Denver_San_Diego >= 1700
Sum_of_Products_into_Stores_Tucson: Route_San_Francisco_Tucson
 + Route_Los_Angeles_Tucson + Route_Phoenix_Tucson + Route_Denver_Tucson
 >= 1500
Sum_of_Products_out_of_Plant_Denver: Route_Denver_San_Diego
 + Route_Denver_Barstow + Route_Denver_Tucson + Route_Denver_Dallas
 - 2000 BuildaPlant_Denver <= 0
Sum_of_Products_out_of_Plant_Los_Angeles: Route_Los_Angeles_San_Diego
 + Route_Los_Angeles_Barstow + Route_Los_Angeles_Tucson
 + Route_Los_Angeles_Dallas - 2000 BuildaPlant_Los_Angeles <= 0
Sum_of_Products_out_of_Plant_Phoenix: Route_Phoenix_San_Diego
 + Route_Phoenix_Barstow + Route_Phoenix_Tucson + Route_Phoenix_Dallas
 - 1700 BuildaPlant_Phoenix <= 0
Sum_of_Products_out_of_Plant_San_Francisco: Route_San_Francisco_San_Diego
 + Route_San_Francisco_Barstow + Route_San_Francisco_Tucson
 + Route_San_Francisco_Dallas - 1700 BuildaPlant_San_Francisco <= 0
Bounds
0 <= Route_San_Francisco_Barstow
0 <= Route_San_Francisco_San_Diego
0 <= Route_San_Francisco_Tucson
0 <= Route_San_Francisco_Dallas
0 <= Route_Los_Angeles_San_Diego
0 <= Route_Los_Angeles_Barstow
0 <= Route_Los_Angeles_Tucson
0 <= Route_Los_Angeles_Dallas
0 <= Route_Phoenix_Barstow
0 <= Route_Phoenix_San_Diego
0 <= Route_Phoenix_Tucson
0 <= Route_Phoenix_Dallas
0 <= Route_Denver_San_Diego
0 <= Route_Denver_Barstow
0 <= Route_Denver_Tucson
0 <= Route_Denver_Dallas
Generals
Route_San_Francisco_Barstow
Route_San_Francisco_San_Diego
Route_San_Francisco_Tucson
Route_San_Francisco_Dallas
Route_Los_Angeles_San_Diego
Route_Los_Angeles_Barstow
Route_Los_Angeles_Tucson
Route_Los_Angeles_Dallas
Route_Phoenix_Barstow
Route_Phoenix_San_Diego
Route_Phoenix_Tucson
Route_Phoenix_Dallas
Route_Denver_San_Diego
Route_Denver_Barstow
Route_Denver_Tucson
Route_Denver_Dallas
Binaries
BuildaPlant_San_Francisco
BuildaPlant_Los_Angeles
BuildaPlant_Phoenix
BuildaPlant_Denver
End
