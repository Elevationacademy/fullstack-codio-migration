Build an export to JSON program using the visitor pattern.

### Specifications
- We have a `User` class that has:
1. id - int
2. name - string
3. password - string
- We have a `Asset` class that has:
1. serial number - int
2. owner - string
3. rating - double
- We have a `Group` class that has:
1. id - int
2. size - int
- Implement a visitor to export all of these to a JSON string (without using JSON.stringify).