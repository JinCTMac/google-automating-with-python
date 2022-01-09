def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary:
        # Now go through the users in the group aka the value list
        for user in group_dictionary[group]:
            if user not in user_groups:
                user_groups[user] = []
            # as user_groups[user] is an empty array, we can just use .append to append the group name into the array
            user_groups[user].append(group)

# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return (user_groups)

print(
    groups_per_user({
        "local": ["admin", "userA"],
        "public": ["admin", "userB"],
        "administrator": ["admin"]
    }))
