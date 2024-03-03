import heapq

def min_total_cost(cable_lengths):
    # Initialize total cost
    total_cost = 0
    
    # Create a min-heap to store cable lengths
    heapq.heapify(cable_lengths)
    
    # While there are at least two cables in the min-heap
    while len(cable_lengths) > 1:
        # Remove the two smallest cables from the min-heap
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        
        # Combine the two cables into one cable
        combined_cable = cable1 + cable2
        
        # Add the combined cable length to the total cost
        total_cost += combined_cable
        
        # Add the combined cable length back to the min-heap
        heapq.heappush(cable_lengths, combined_cable)
    
    return total_cost

# Example usage:
cables = [8, 4, 6, 12]
print("Minimum total cost:", min_total_cost(cables))
