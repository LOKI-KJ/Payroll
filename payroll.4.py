from datetime import datetime, timedelta

# ==========================================
# SECTION: [E053]
# GROUP NUMBER: GRP 2
# GROUP LEADER: 
# MEMBERS: 
#   - Paderes, Aaron Daneil
#   - Cajeda, 
#   - Muyco, Rosalinda
#   - Saba, Rovie Aaron
#   - Gaciano, Jheremy Kurt
#   - David, Charles Howard
# ==========================================

employees = {}

def get_current_timestamp():
    return datetime.now().strftime("%m/%d/%y %I:%M:%S %p")

def main_menu():
    while True:
        print("\n" + "=" * 50 + " CC03 PAYROLL SYSTEM " + "=" * 50)
        print(f"{' ' * 75}{get_current_timestamp()}")
        print("1. PAYROLL")
        print("2. REGISTER EMPLOYEE")
        print("3. VIEW EMPLOYEE")
        print("4. EXIT")
        print("-" * 123)
        
        choice = input("Enter your choice here: ").strip()
        
        if choice == '1':
            process_payroll()
        elif choice == '2':
            register_employee()
        elif choice == '3':
            view_employee()
        elif choice == '4':
            print("\n" + "=" * 50 + " PAYROLL SYSTEM " + "=" * 50)
            print(f"{' ' * 75}{get_current_timestamp()}")
            print("\nGOODBYE!")
            print("=" * 123)
            break
        else:
            print("INVALID INPUT. TRY AGAIN!")

def register_employee():
    while True:
        print("\n" + "=" * 50 + " REGISTER EMPLOYEE " + "=" * 50)
        print(f"{' ' * 75}{get_current_timestamp()}")
        print("\n>> Employee Details")
        
        emp_id = input("Enter Employee ID: ").strip()
        if emp_id in employees:
            print("EMPLOYEE ID ALREADY EXISTS. TRY AGAIN!")
            if not ask_continue("register another employee"):
                break
            continue
            
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        
        while True:
            tin = input("Enter 12-Digit TIN ID#: ").strip()
            if tin.isdigit() and len(tin) == 12:
                break
            print("INVALID INPUT. TRY AGAIN!")
            
        while True:
            sss = input("Enter 10-Digit SSS ID#: ").strip()
            if sss.isdigit() and len(sss) == 10:
                break  
            print("INVALID INPUT. TRY AGAIN!")
            
        
        while True:
            philhealth = input("Enter 12-Digit PHILHEALTH ID#: ").strip()
            if philhealth.isdigit() and len(philhealth) == 12:
                break
            print("INVALID INPUT. TRY AGAIN!")
            
        while True:
            dept_choice = input("Enter Department (1) Guidance (2) Faculty ").strip()
            if dept_choice == '1':
                department = "Guidance"
                break
            elif dept_choice == '2':
                department = "Faculty"
                break
            print("INCORRECT CHOICE. TRY AGAIN!")
            
        while True:
            pos_choice = input("Enter Position (1) Full-Time (2) Part-Time: ").strip()
            if pos_choice == '1':
                position = "Full-Time"
                break
            elif pos_choice == '2':
                position = "Part-Time"
                break
            print("INCORRECT CHOICE. TRY AGAIN!")
            
        while True:
            try:
                rate_per_hour = float(input("Enter Rate per Hour: "))
                if rate_per_hour > 0:
                    break
                print("INVALID INPUT. TRY AGAIN!")
            except ValueError:
                print("INVALID INPUT. TRY AGAIN!")
                
        employees[emp_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "tin": tin,
            "sss": sss,
            "philhealth": philhealth,
            "department": department,
            "position": position,
            "rate_per_hour": rate_per_hour,
            "payroll_entries": []
        }
        
        if not ask_continue("register another employee"):
            break

def process_payroll():
    while True:
        print("\n" + "=" * 50 + " PAYROLL SCREEN " + "=" * 50)
        print(f"{' ' * 75}{get_current_timestamp()}\n")
        
        emp_id = input("Enter Employee ID: ")
        if emp_id not in employees:
            print("EMPLOYEE ID DOES NOT EXIST. TRY AGAIN!")
            if not ask_continue("place another payroll entry", is_payroll=True):
                break
            continue
            
        while True:
            date_str = input("Enter Pay Period Date: ").strip()
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
                day = dt.day
                last_day_of_month = (dt.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
                
                if day == 15:
                    start_date = dt.replace(day=1).strftime("%Y-%m-%d")
                    end_date = dt.replace(day=15).strftime("%Y-%m-%d")
                    break
                elif day == last_day_of_month.day:
                    start_date = dt.replace(day=16).strftime("2026-03-16")
                    end_date = last_day_of_month.strftime("2026-03-31")
                    break
                else:
                    print("INCORRECT PAY PERIOD DATE ENTRY. MUST BE 15TH AND/OR END OF MONTH ONLY. TRY AGAIN!")
            except ValueError:
                print("INCORRECT PAY PERIOD DATE ENTRY. INVALID DATE. TRY AGAIN!")
                
        print(f"\n>> Pay Period Date/s: {start_date} to {end_date}")
        
        while True:
            try:
                reg_hours = float(input("Enter Total # of Regular Hours Worked: "))
                if reg_hours > 0:
                    break
                print("INVALID INPUT. TRY AGAIN!")
            except ValueError:
                print("INVALID INPUT. TRY AGAIN!")
                
        while True:
            try:
                ot_hours = float(input("Enter Total # of OT Hours Worked: "))
                if ot_hours >= 0: # 0 OT hours is acceptable as seen in sample screenshots
                    break
                print("INVALID INPUT. TRY AGAIN!")
            except ValueError:
                print("INVALID INPUT. TRY AGAIN!")
                
        entry = {
            "period": f"{start_date} to {end_date}",
            "reg_hours": reg_hours,
            "ot_hours": ot_hours
        }
        employees[emp_id]["payroll_entries"].append(entry)
        
        if not ask_continue("place another payroll entry", is_payroll=True):
            break

def view_employee():
    while True:
        print("\n" + "=" * 50 + " VIEW EMPLOYEE " + "=" * 50)
        print(f"{' ' * 75}{get_current_timestamp()}\n")
        
        emp_id = input("Enter Employee ID: ").strip()
        if emp_id not in employees:
            print("EMPLOYEE ID DOES NOT EXIST. TRY AGAIN!")
            if not ask_continue("view another employee", is_view=True):
                break
            continue
            
        emp = employees[emp_id]
        print(f"\n>> Employee Details")
        print(f"First Name: {emp['first_name']}")
        print(f"Last Name: {emp['last_name']}")
        print(f"TIN ID#: {emp['tin']}")
        print(f"SSS ID#: {emp['sss']}")
        print(f"PhilHealth ID#: {emp['philhealth']}")
        print(f"Department: {emp['department']}")
        print(f"Position: {emp['position']}")
        print(f"Rate per Hour: {emp['rate_per_hour']}")
        
        print(f"\n>> Payroll Entries")
        for entry in emp['payroll_entries']:
            reg_pay = entry['reg_hours'] * emp['rate_per_hour']
            ot_rate = emp['rate_per_hour'] * 1.5
            ot_pay = entry['ot_hours'] * ot_rate
            gross_pay = reg_pay + ot_pay
            
            tax = gross_pay * 0.15
            sss_deduction = gross_pay * 0.02
            philhealth_deduction = gross_pay * 0.05
            total_deductions = tax + sss_deduction + philhealth_deduction
            net_pay = gross_pay - total_deductions
            
            print(f"*Pay Period Date/s: {entry['period']}")
            print(f"Total # of Regular Hours Worked: {int(entry['reg_hours']) if entry['reg_hours'].is_integer() else entry['reg_hours']}")
            print(f"Total # of Overtime Hours Worked: {int(entry['ot_hours']) if entry['ot_hours'].is_integer() else entry['ot_hours']}")
            print(f"Total Regular Pay: P{reg_pay:,.2f}")
            print(f"Total Overtime Pay: P{ot_pay:,.2f}")
            print(f"Total Gross Pay: P{gross_pay:,.2f}")
            print("Deductions:")
            print(f"Tax (15%): P{tax:,.2f}")
            print(f"SSS (2%): P{sss_deduction:,.2f}")
            print(f"PhilHealth (5%): P{philhealth_deduction:,.2f}")
            print(f"Total Deductions: P{total_deductions:,.2f}")
            print(f"Total Net Pay: P{net_pay:,.2f}")
            
        if not ask_continue("view another employee", is_view=True):
            break

def ask_continue(action_text, is_payroll=False, is_view=False):
    prompt_key = f"Do you want to {action_text}? (Y/N): "
    while True:
        ans = input(prompt_key).strip().upper()
        if ans == 'Y':
            return True
        elif ans == 'N':
            return False

if __name__ == "__main__":
    main_menu()