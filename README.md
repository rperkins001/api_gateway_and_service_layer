# api_gateway_and_service_layer
# API Gateway Example

This repository demonstrates the concept of an API gateway that interacts with multiple data 
sources and passes API calls onto the service layer. This example was created to showcase how 
an API gateway can be designed to handle requests from various sources and direct them to the 
appropriate services, potentially with different outcomes.

**Note**: This is a code system example and not a fully functional implementation. The data 
sources and server are not set up, and the application is not expected to work as-is. The purpose 
of this example is to provide an understanding of how an API gateway can be structured.

## File Structure

The project follows a well-organized structure with a separation of concerns, 
which makes it easier to understand and maintain:

- api_gateway
    - __init__.py
    - api_gateway.py
- config
    - api_config.py
- service_layer
    - __init__.py
    - customer_tickets_service.py
    - dns_service.py
    - jira_tickets_service.py
- sources
    - customer_tickets
        - __init__.py
        - customer_tickets.py
    - dns
        - __init__.py
        - dns.py
    - jira_tickets
        - __init__.py
        - jira_tickets.py
- utils
    - __init__.py
    - error_handling.py
    - logging.py
- main.py

## Explanation

This example demonstrates an API gateway that receives incoming API requests and 
directs them to the appropriate service layer based on the data source (Jira, customer, or DNS). 
The service layer handles the business logic for each data source and returns the results back 
to the API gateway. The API gateway then sends the response back to the client.

This example showcases the following concepts:

1. API Gateway: Directs incoming API requests to the appropriate service layer based on the data source.
2. Service Layer: Handles the business logic for each data source and interacts with the respective sources.
3. Separation of Concerns: The project is structured to separate the concerns of API gateway, service layer, and data sources, 
   making it easier to understand and maintain.
4. Utility Functions: Utility functions for error handling and logging have been included for better code reusability.

## Additional Notes

This example is intended to demonstrate the architecture and structure of an API gateway system that interacts with 
multiple data sources. It is not a fully functional implementation, and the data sources and server are not set up. 
Please keep this in mind when reviewing the code.


