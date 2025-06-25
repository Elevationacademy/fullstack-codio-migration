Implement a travel agency.

Specifications:
- Use a factory method to provide the vehicles for the agency.
- The factory should be a singleton.
- The travel agency has 4 buses, 8 taxis, 3 boats, and one plane.
- `Plane`, `Bus`, `Taxi`, and `Boat` all implement the `Vehicle` interface.
- `Vehicle` has the `transport(Passenger passenger)` method that accepts a passenger and prints it's name to mark a successful transport.
- A `Passenger` has a name and a favorite `Vehicle`.

- Your program should assign passengers to the available vehicles.
- If a passenger's favorite vehicle is available assign it to him, otherwise, assign a random available vehicle.
- When all vehicles are used, invoke the transport method of all of them.

Example flow:
- The program generated the passenger:
{name:"shlomi", favorite: PLANE}
- The agency has no PLANE available, so shlomy gets a taxi.
- Now the agency has one less taxi available.
