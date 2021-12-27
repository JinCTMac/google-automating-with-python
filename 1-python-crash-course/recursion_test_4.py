def count_users(group):
    count = 0
    # previously, this code added count += 1, then checked if a member was part of a group or not
    # this needs to be made an else statement, where count += 1 is only given if the member isn't part of a group, else it calls the function to count users again for the group the member is in
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18
