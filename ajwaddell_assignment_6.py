count = 0
contact = []
cont_info = input("Enter contact information (format: name|phone|email|address):")
print()
while cont_info.upper() != "DONE":
    contact.append(cont_info)
    cont_info = input()
    count += 1
contacts_modified = []
states_abbreviated = {
    "al", "ak", "az", "ar", "ca", "co", "ct","dc", "de", "fl", "ga", 
    "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md", 
    "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", 
    "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc", 
    "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"
}
for contacts_amounts, contact_entry in enumerate(contact, start=1):
    cont_info_parts = contact_entry.split("|")
    if len(cont_info_parts) != 4:
        continue
    cont_name, cont_phone, cont_email, cont_address = cont_info_parts
    cont_name = cont_name.strip().replace("-", " ").replace("_", " ")
    split_cont_name = cont_name.split()
    cont_name_list = []
    for part in split_cont_name:
        split_parts = "".join(char for char in part if char.isalpha() or char == "'")
        if split_parts:
            cont_name_list.append(split_parts.title())
    name = " ".join(cont_name_list)
    cont_email = cont_email.strip().lower()
    digits_only = "".join(char for char in cont_phone if char.isdigit())
    if len(digits_only) == 10:
        phone_format = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    elif len(digits_only) == 11 and digits_only.startswith("1"):
        phone_format = f"({digits_only[1:4]}) {digits_only[4:7]}-{digits_only[7:]}"
    else:
        phone_format = cont_phone.strip()
    address = cont_address.strip().replace(",", "").replace(".", "")
    part_address = address.split()
    final_address_parts = [] 
    for part in part_address:
        if len(part) == 2 and part.isalpha() and part.lower() in states_abbreviated:
            final_address_parts.append(part.upper())
        else:
            final_address_parts.append(part.title())
    address_format = " ".join(final_address_parts)
    contacts_modified.append({
        "name": name, 
        "phone": phone_format, 
        "email": cont_email, 
        "address": address_format
    })
print()
print("=== CONTACT DIRECTORY ===")
for num, contact_record in enumerate(contacts_modified, start=1):
    print(f"\nCONTACT {num}:") 
    print(f"Name:    {contact_record['name']}")
    print(f"Phone:   {contact_record['phone']}")
    print(f"Email:   {contact_record['email']}")
    print(f"Address: {contact_record['address']}")
print()
print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(contacts_modified)}")
print()
print("=== FORMATTED FOR PRINTING ===")
for contact_record in contacts_modified:
    main_name = contact_record["name"]
    main_phone = contact_record["phone"]
    main_email = contact_record["email"]
    name_parts = main_name.split()
    if len(name_parts) >= 2:
        last_name = name_parts[-1]
        middle_name = " ".join(name_parts[:-1])
        # Format as Last Name, First/Middle Name(s)
        name = f"{last_name}, {middle_name}"
    else:
        name = main_name
    print(f"{name:<30}{main_phone:<20}{main_email}")