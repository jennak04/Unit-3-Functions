# the raise syntax
# basic syntax
"""
raise ExceptionType("Your message!")
Examples:
raise ValueError("Quantity must be at least 1")
raise TypeError("Expected a player object, got a potato")
raise PermissionError("You are not a mod")
"""

def open_loot_box(player, quantity):
    if quantity <= 0:
        return None
    # rest of the code
    
# raising excpetion
def open_loot_box(player, quantity):
    if quantity <= 0:
        raise ValueError("Bad quantity")
    # rest of the code
    
VALID_PROTEINS = ["chicken", "steak", "barbacoa", "carnitas"]
VALID_RICE = ["white", "brown", "none"]
VALID_BEANS = ["black", "pinto", "none"]
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """Build a chipotle bowl with validation

    Raises:
    ValueError: if the protein is invalid
    TypeError: if extras is not a list
    """
    
    # check if extras is a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list!")
    
    #Validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' isn't valid! Choose from {VALID_PROTEINS}")
    # Return the bowl
    return {
        "protein": protein.lower(),
        "rice": rice.lower(),
        "extras": extras,
        "price": 10.50
    }
    
# test the function
try:
    #bowl = build_bowl("chicken", "brown", "corn")
    bowl = build_bowl("chicken", "brown", ["corn"])
    print(f"Created: {bowl}")
    
except Exception as e:
    print(f"Error: {e}")