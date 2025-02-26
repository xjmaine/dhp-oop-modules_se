from user_module import User, Profile


def main():
    # get user information from command line
    email_input = input("Email: ")
    password_input = input("Password: ")
    first_name_input = input("First Name: ")
    last_name_input = input("Last Name: ")
    sex_input = input("Sex (M/F): ")
    age_input = int(input("Age: "))
    bio_input = input("Bio: ")

    # create a new user
    new_user = User(
        email=email_input,
        password=password_input
    )

    # create a new profile
    _ = Profile(
        user=new_user,
        first_name=first_name_input,
        last_name=last_name_input,
        sex=sex_input,
        age=age_input,
        bio=bio_input if bio_input.strip() else None
    )

    # print the user information
    print(User.list_of_users)
    print(Profile.list_of_profiles)


# if module is run as a script run the main function
if __name__ == "__main__":
    main()
