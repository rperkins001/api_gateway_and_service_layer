from api_gateway.api_gateway import APIGatewayService
from sources.customer_tickets.customer_tickets import CustomerTickets
from sources.jira_tickets.jira_tickets import JiraTickets
from sources.dns.dns import DNS

def main():
    # Initialize the API wall service
    api_wall_service = APIGatewayService()

    # Initialize source-specific classes
    customer_tickets = CustomerTickets(api_wall_service)
    jira_tickets = JiraTickets(api_wall_service)
    dns = DNS(api_wall_service)

    # Fetch data from customer tickets
    customer_data = customer_tickets.get_data()
    print("Customer Tickets Data:")
    print(customer_data)

    # Fetch data from Jira tickets
    jira_data = jira_tickets.get_data()
    print("Jira Tickets Data:")
    print(jira_data)

    # Fetch data from DNS
    dns_data = dns.get_data()
    print("DNS Data:")
    print(dns_data)

    # Example: Update data in Jira tickets
    if jira_tickets:
        update_data = {"key": "value"}
        update_response = jira_tickets.update_data(update_data)
        print("Update Response:")
        print(update_response)

    

if __name__ == "__main__":
    main()