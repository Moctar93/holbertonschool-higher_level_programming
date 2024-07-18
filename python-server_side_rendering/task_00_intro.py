import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a sting.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: Nodata provied, no output files generated.")
        return
    

    for index, attendee in enumerate(attendees, start=1):
        personalized_content = template
        personalized_content = personalized_content.replace("{name}",attendee.get("name", "N/A"))
        personalized_content = personalized_content.replace("{event_title}",attendee.get("event_title", "N/A"))
        personalized_content = personalized_content.replace("{event_date}",attendee.get("event_date", "N/A"))
        personalized_content = personalized_content.replace("{event_location}",attendee.get("event_location", "N/A"))
        
        output_filename = f"output_{index}.txt"

        if os.path.exists(output_filename):
            print(f"Error: {output_filename} already exists.")
            continue

        try:
            with open(output_filename, "w") as file:
                file.write(personalized_content)
            print(f"Generated : {output_filename}")
        except Exception as e:
            print(f"Error: Unable to write to {output_filename}.")
            print(e)
