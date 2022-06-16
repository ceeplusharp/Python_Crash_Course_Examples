# Chapter 11: Testing a Function

def get_formatted_name(first, last, middle=None):
    """Generate a neatly formatted full name."""
    if middle is None:
        full_name = f"{first} {last}"
        return full_name.title()
    else:
        full_name = f"{first} {middle} {last}"
        return full_name.title()
