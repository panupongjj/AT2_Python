#  PayrollReport01.py 
#  This program processes to read and writ TEXT file
#  Author: Panupong Jangjun
#  Date: 29/11/2024

def read_data(file_parth,file_name):
    with open(file_parth+"\\"+file_name, 'r') as file:
        count = 1; 
        employees = []
        employeeTemp = []

        for line in file:
            temp = line.strip()
            employeeTemp.append(temp)
            if count == 4:
                employees.append(employeeTemp)
                employeeTemp = []
                count = 1
            else:
                count += 1
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

    return total_salary, total_employees, average_salary, manager_total, sales_total, admin_total

def write_report_to_file(file_parth,file_name, total_salary, total_employees, average_salary, manager_total, sales_total, admin_total):
    
    with open(file_parth+"\\"+file_name, 'w') as file:
        file.write(f"Total Payroll: {total_salary:.2f}\n")
        file.write(f"Number of Payroll: {total_employees}\n")
        file.write(f"Average pay: {average_salary:.2f}\n\n")
        file.write(f"Total pay for: \n")
        file.write(f"Managers: {manager_total:.2f}\n")
        file.write(f"Sales: {sales_total:.2f}\n")
        file.write(f"Admin: {admin_total:.2f}\n")


def main():
    file_parth = "C:\\JJ_CERIV_PGM\GIT\AT2_Python\Part_B"
    employee_file = 'employees.txt'
    report_file = 'PayrollReport.txt'
    
    employeesList = read_data(file_parth,employee_file)
    
    totalSalary, totalEmployees, averageSalary, managerTotal, salesTotal, adminTotal = calculate_totals(employeesList)
    
    write_report_to_file(file_parth,report_file, totalSalary, totalEmployees, averageSalary, managerTotal, salesTotal, adminTotal)

if __name__ == "__main__":
    main()