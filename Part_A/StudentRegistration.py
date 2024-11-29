#  StudentRegistration.py 
#  This program processes student details, summay fee then 
#  displays this information onto the screen.  
#  Author: Panupong Jangjun
#  Date: 29/11/2024

def printHeadings():
    print("---- HOLMESGLEN INSITITUTE ----")
    print("ID\tNAME\t\t\tCOURSE\tFEE")

def inputStudentDetails(student_number):
    print("\nEnter details for Student "+str(student_number)+": ")
    student = {}
    student['ID'] = input("Enter student's ID: ")
    student['NAME'] = input("Enter student's NAME: ")
    student['COURSE'] = input("Enter student's COURSE: ")
    try:
        student['FEE'] = float(input("Enter Course Fee: $"))
    except ValueError:
        print("Invalid input! Please enter a valid number for the fee.")
        return 0  
    return student

def outputTotalFee(totalFees):
    print("\n-----------------------------------")
    print(f"Total Fees Collected: ${totalFees:.2f}")
    print("-----------------------------------")
    
def main():
    totalFees = 0  # Initialize the total fees to 0
    students = []
    print("HOW MANY STUDENT DO YOU WANT TO CREATE? ")
    totalStudent = int(input("Enter Number of Student: "))
    # Input details for 3 students
    for student_number in range(1, totalStudent+1):
        returnData = inputStudentDetails(student_number)  # Get each student's fee
        students.append(returnData)
        totalFees += returnData['FEE']  # Accumulate the total fees
    
    # Display the program heading
    printHeadings()  
    # Dislay Student 
    for student in students:
        print(f"{student['ID']}\t{student['NAME']}\t\t{student['COURSE']}\t{student['FEE']}")
    # Output the total fees after all students' details are entered
    outputTotalFee(totalFees) 

# Execute the program
if __name__ == "__main__":
    main()