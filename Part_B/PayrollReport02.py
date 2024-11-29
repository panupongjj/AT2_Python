#  PayrollReport02.py 
#  This program processes to read and writ CSV file
#  Author: Panupong Jangjun
#  Date: 29/11/2024

import csv

def read_employee_data(file_parth,file_name):
    employees = []
    with open(file_parth+"\\"+file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            employees.append(row)  # Add employee record (id name, position, salary)
    return employees

def calculate_totals(employees):
    total_salary = 0
    manager_total = 0
    sales_total = 0
    admin_total = 0
    total_employees = 0

    for employee in employees:
        id, name, position, salary = int(employee[0]), employee[1], employee[2], float(employee[3])
        print(f"{id}\t{name}\t{position}\t{salary}")
        
        total_salary += salary
        total_employees += 1

        if position == "Manager":
            manager_total += salary
        elif position == "Sales":
            sales_total += salary
        elif position == "Administration":
            admin_total += salary
    
    average_salary = total_salary / total_employees if total_employees > 0 else 0

    # Return a dictionary with the calculated totals
    return {
        'total_salary': str(f"{total_salary:.2f}"),
        'total_employees': str(f"{total_employees:.2f}"),
        'average_salary': str(f"{average_salary:.2f}"),
        'manager_total': str(f"{manager_total:.2f}"),
        'sales_total': str(f"{sales_total:.2f}"),
        'admin_total': str(f"{admin_total:.2f}")
    }

def write_report_to_file(file_parth,file_name, totals):
    with open(file_parth+"\\"+file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["Total payroll", "Number of payroll", "Average payroll", "Manager Total", "Sales Total", "Admin Total"])
        
        # Write totals
        writer.writerow([
            totals['total_salary'],
            totals['total_employees'],
            totals['average_salary'],
            totals['manager_total'],
            totals['sales_total'],
            totals['admin_total']
        ])

def main():
    # File names
    file_parth = "C:\\JJ_CERIV_PGM\GIT\AT2_Python\Part_B"
    input_file = 'employees.csv'
    output_file = 'PayrollReport.csv'
    
    employees = read_employee_data(file_parth,input_file)
    
    totals = calculate_totals(employees)

    write_report_to_file(file_parth,output_file, totals)

if __name__ == "__main__":
    main()