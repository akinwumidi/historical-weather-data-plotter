import sqlite3
from db_connector import connect_to_database

class UserInterface():
    def __init__(self, connection):
        self.connection = connection        

    def display_menu(self):
        print("********************************************************************************")
        print("++++++ Weather Data Analysis App Main Menu =====")
        print("A. Basic Operations")
        print("B. Visualization Operations (Charts)")
        print("C. Database Operations")
        print("0. Quit")
        print("********************************************************************************")

    def display_basic_operations_menu(self):
        print("\n++++++ A. Basic Operations")
        print("1. Print all Countries ID and Name Data contained in database")
        print("2. Print all City ID and Name Data contained in database")
        print("3. Generate Average Annual Temperature for specific city for a given year")
        print("4. Generate Average 7 day precipitation for a desired city from a specific date")
        print("5. Generate Average mean temperature for all cities between two dates")
        print("6. Generate Average Annual precipitation for all countries for a specific year")
        print("0. Back to Main Menu")

    def display_visualization_operations_menu(self):
        print("\n++++++ B. Visualization Operations( Charts )")
        print("7. Plot Bar Chart for Average seven day precipitation for cities from a specified date")
        print("8. Plot Bar Chart for Average precipitation between specific dates")
        print("9. Plot Bar Chart for Average Yearly precipitation for all countries")
        print("10. Plot Group Bar Chart showing Min/Max temperatures and precipitation by Month for cities/country")
        print("11. Multiline Chart for Daily Min and Max Temperature")
        print("12. Scatter Plot for Average Temperature vs Average Precipitation")
        print("0. Back to Main Menu")

    def display_database_operations_menu(self):
        print("\n===== C. Database Operations")
        print("13. Update database from Meteo Api for specific City between 2 Dates")
        print("0. Back to Main Menu")

    def get_all_cities(self):
        try:
            query = "SELECT * FROM [cities]"
            cursor = self.connection.cursor()
            results = cursor.execute(query)
            for row in results:
                print(f"City Id: {row['id']} || Name: {row['name']} || Longitude: {row['longitude']} || Latitude: {row['latitude']}")

        except sqlite3.OperationalError as ex:
            print(ex)

    def main(self):
        self.get_all_cities()
        

# if __name__ == __main__:
if __name__ == "__main__":
    connection = connect_to_database("database/weather_data.db")
    app_menu = UserInterface(connection)
    app_menu.main()
    
    #close db conenction
    connection.close()