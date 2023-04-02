try:
    with open('TotalA.exe', 'rb') as source_file:
        file_content = source_file.read()

        # Make the check for right click interface always fail when getting the cursor type
        # So that it returns the same cursor as when left click interface is used
        interface_check = b'\x83\xBB\xFA\x7E\x03\x00\x01'
        if not interface_check in file_content:
            print("Failed to find the code for the 'interface_check'")
        file_content = file_content.replace(interface_check, b'\x83\xBB\xFA\x7E\x03\x00\xFF')

        # Change the function that handles left click so that checks for right/left interface before checking the current cursor type
        left_click_function = b'\x80\xfa\x11\x7c\x27\x83\xb8\xfa\x7e\x03\x00\x01\x0f\x85\xa3\x00\x00\x00\x80\xf9\x01\x0f\x85\x9a\x00\x00\x00\xe8\x9f\x2c\xff\xff\x6a\x01\xe8\x08\x8d\xff\xff\x5e\x59\xc2\x04\x00'
        if not left_click_function in file_content:
            print("Failed to find the code for the 'left_click_function'")
        file_content = file_content.replace(left_click_function, b'\x83\xb8\xfa\x7e\x03\x00\x01\x0f\x85\x1a\x00\x00\x00\x80\xf9\x01\x0f\x85\x16\x00\x00\x00\xe8\xa4\x2c\xff\xff\x6a\x01\xe8\x0d\x8d\xff\xff\x5e\x59\xc2\x04\x00\x80\xfa\x11\x7d\xf6')

    with open('TotalA-right-click-patch.exe', 'wb') as output_file:
        output_file.write(file_content)
        print("Done!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



