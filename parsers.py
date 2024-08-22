def parse(user_input):
    parts = user_input.split("2,4")
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}