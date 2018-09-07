def new_password(oldpassword, newpassword):
    if newpassword == oldpassword or len(newpassword) < 6:
        return False
    else:
        return True

print(new_password("hhhhhhh","dasdadsdddd"))
print(new_password("hhhhhhh","hhhhhhh"))
print(new_password("hhhhhhh","g"))