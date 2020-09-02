Group 2 Airport project
Mehdi, Ibrahim, Daniel

Epic story
Our epic story for this project is to create an airport interface which can be used by the airport staff. In order to fulfil our epic story, we first broke it down into manageable chunks. In this case these are our user stories

User stories
The user stories where presented to us by the product owner. It is crucial that all user stories are met in order to deem this project as successful. They are as followed:

As an airport assistant, I want to be able to create a passenger's database with name and passport no. So I can add them to flight

An airport assistant wants to be able to create a flight_info with a specific destination

As an airport assistant I want to be able to assign and/or change a plane to my flight_info, input my password and handle the problem

As an airport assistant I want to be able to add passengers to flight_trip, for the customers that have bought tickets 2DOD – Create a form for passengers to buy tickets

As an airport assistant, I want to be able to generate a flight_attendees_list_report that list of passengers name and passport number, so that I can check their identity document

By breaking down each user story, we determined how each functionality could be met. The breakdown is as followed: -	Inputs -	Outputs -	Variables -	Functions -	Tasks

This breakdown allowed us to assess each factor and essentially come up with a solution in order to fulfil the definition of done. The full breakdown can be seen here.

Definition of done
In this project the definition of done is as follows: -	Meeting all user stories -	Effective pseudo coding -	Writing clean reusable code -	Testing of functionality’s -	Successful integration of code -	Adhering to the scrum framework and agile methodology

Acceptance criteria
In this project the definition of done is as follows: -	Meeting all user stories - Meeting the definition of done

Project planning
Before starting the technicalities of the project, it was important to first thoroughly plan. This was done as follows: -	Task assignment -	GANT chart creation -	How we can meet the acceptance criteria -	How we can meet the definition of done

Database creation
After careful consideration, we decided the best way in order to incorporate a database into our project was to integrate SQL with python. The database creation in python can be seen below:

    def create_table(self):
        a = Database_OOP() #fix naming convetions
        cursor = a.connect_sql()
        table_name = "passengers"
        sql_command = f"""
DROP TABLE {table_name}
CREATE TABLE {table_name}
(
first_name VARCHAR(300),
last_name VARCHAR(300),
passport_number VARCHAR(300),
dob VARCHAR(300),
upcoming_flight VARCHAR(300),
flight_destination VARCHAR(300),
airmiles VARCHAR(300),
previous_flights VARCHAR(300),
)
"""