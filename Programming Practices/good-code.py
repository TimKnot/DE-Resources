# Example 1
2 * 4 + 7.0 / 4.0

# Example 2 - ignore errors
person = create_person(
    firstname,
    surname,
    age,
    city,
    nationality,
    gender,
    height
)

# Example 3
def get_length_condition(data):
    return data is not None \
        and data != "" \
        and len(data) > 3 \
        and len(data) < 20
