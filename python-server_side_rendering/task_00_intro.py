"""
This module provides a function to generate personalized invitation files
from a template string and a list of attendee dictionaries.
"""

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string containing placeholders.
        attendees (list): A list of dictionaries, each containing attendee data.

    Behavior:
        - Validates input types.
        - Handles empty template and empty attendees list.
        - Replaces missing values with "N/A".
        - Creates output files named output_X.txt (X starting from 1).
    """
    # Validate input types
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        try:
            content = template
            # Replace placeholders with attendee data or "N/A" if missing or None
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key, "N/A")
                if value is None:
                    value = "N/A"
                content = content.replace(f"{{{key}}}", str(value))

            # Write to output file
            filename = f"output_{idx}.txt"
            with open(filename, "w") as f:
                f.write(content)

        except Exception as e:
            print(f"Error generating file for attendee {idx}: {e}")
