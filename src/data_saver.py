import csv

def save2Csv(table_data_list, csv_file):
    """
    Save a list of table strings to a CSV file.

    :param table_data_list: List of table strings formatted like Markdown tables.
    :param csv_file: Name of the output CSV file (default is "research_articles.csv").
    """
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Loop through each table in the list
        for table_data in table_data_list:
            # Parse the table into rows of data
            lines = table_data.strip().split("\n")

            # Extract headers and data
            headers = [header.strip() for header in lines[0].strip("|").split("|")]
            rows = []
            for line in lines[2:]:  # Skip the header and separator lines
                row = [cell.strip() for cell in line.strip("|").split("|")]
                rows.append(row)

            # Write headers only for the first table
            if file.tell() == 0:
                writer.writerow(headers)

            # Write rows
            writer.writerows(rows)

    print(f"Data successfully saved to {csv_file}")

def save2Textt(table_data_list, text_file="research_articles.txt"):
    """
    Save a list of dictionaries representing table rows to a text file.

    :param table_data_list: List of dictionaries where each dictionary represents a row in the table.
    :param text_file: Name of the output text file (default is "research_articles.txt").
    """
    with open(text_file, mode='w', encoding='utf-8') as file:
        # Write headers based on the first dictionary's keys
        headers = list(table_data_list[0].keys())
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "| " + " | ".join(["-" * len(header) for header in headers]) + " |"

        # Write headers and separator to the text file
        file.write(header_line + "\n")
        file.write(separator_line + "\n")

        # Loop through each dictionary in the list and write its values as a table row
        for row_dict in table_data_list:
            row_line = "| " + " | ".join(str(row_dict[key]) for key in headers) + " |"
            file.write(row_line + "\n")

        file.write("\n")

    print(f"Data successfully saved to {text_file}")

