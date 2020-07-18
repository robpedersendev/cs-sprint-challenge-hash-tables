#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Instantiate the ticket_origination dictionary
    ticket_origination = {}

    # Create a for loop the iterates through all the tickets
    for ticket in tickets:
        # Set the ticket.source to ticket
        ticket_origination[ticket.source] = ticket

    # Set cur_ticket to index with the key of "NONE"
    cur_ticket = ticket_origination["NONE"]
    # Create the array for the "overly_complicated_python_function_to_figure_out_your_route" array
    overly_complicated_python_function_to_figure_out_your_route = []

    # Run a for loop for the length of the tickets_organization array
    while True:
        # Add the cur_ticket's destination to the overly_complicated_python_function_to_figure_out_your_route array
        overly_complicated_python_function_to_figure_out_your_route.append(cur_ticket.destination)
        # If the tickets ending destination is "NONE" (the last ticket)
        if cur_ticket.destination == "NONE":
            # End the loop
            break
        # Set the current ticket to be the value of the index of cur_ticket within the ticket_organization array
        cur_ticket = ticket_origination[cur_ticket.destination]

    # Return the array
    print(overly_complicated_python_function_to_figure_out_your_route)
    return overly_complicated_python_function_to_figure_out_your_route
