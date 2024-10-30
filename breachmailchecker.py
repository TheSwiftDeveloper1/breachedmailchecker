def wordcount(filename, email):
    try:
        with open(filename, "r") as file:
            read = file.readlines()
        
        count = 0

        for sentence in read:
            line = sentence.split()
            for each_word in line:
                word = each_word.strip("/¤%()")
                if email == word:
                    count += 1

        if count > 0:
            print(f"{email} is breached {count} times.")
        else:
            print(f"{email} is not breached.")
    
    except FileNotFoundError:
        print("The file is not found.")

while True:
    email_input = input("Enter email (or type 'exit' to quit): ")
    if email_input.lower() == "exit":
        break
    wordcount("breachedmails.txt", email_input)
