def total(basket):
    # Constants
    BOOK_PRICE = 8
    DISCOUNTS = {
        1: 1.00,  # No discount for a single book
        2: 0.95,  # 5% discount for two different books
        3: 0.90,  # 10% discount for three different books
        4: 0.80,  # 20% discount for four different books
        5: 0.75   # 25% discount for five different books
    }
    
    def calculate_group_discount(group):
        """Calculate the price for a group of books applying the discount, in cents."""
        unique_books = len(set(group))
        discount = DISCOUNTS[unique_books]
        # Calculate the group price in cents
        return int(unique_books * BOOK_PRICE * discount * 100)
    
    def best_price(basket):
        """Determine the best price for the given basket of books."""
        if not basket:
            return 0.0
        
        # Start with an impossibly high price to ensure we find the minimum
        min_price = float('inf')
        
        # Generate all possible groupings and calculate the price for each
        for group_size in DISCOUNTS.keys():
            if group_size <= len(basket):
                group = basket[:group_size]
                remaining_basket = basket[group_size:]
                price_for_group = calculate_group_discount(group)
                # Recursively calculate the best price for the remaining basket
                total_price = price_for_group + best_price(remaining_basket)
                min_price = min(min_price, total_price)
        
        return min_price
    
    # Sort the basket to ensure that the same books are grouped together for discount calculation
    sorted_basket = sorted(basket)
    # Calculate the best price for the sorted basket and convert it to an integer
    return int(best_price(sorted_basket))
