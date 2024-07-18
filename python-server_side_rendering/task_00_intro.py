import os

def generate_invitation(template, attendees):
    
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error Attendees must be a list of dictionaries.")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A") or "N/A")
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

    
    output_filename = f'output_{index}.txt'

    if os.path.exists(output_filename):
            print(f"Error: File {output_filename} already exists.")
    else:
         try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(invitation)
                print(f"Invitation {index} written to {output_filename}")
         except Exception as e:
                print(f"Error: Could not write to {output_filename}. Exception: {e}")

