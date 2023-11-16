"""
Check if this employee has achieved his weekly target or not
"""


class Employee:
    # Public class attributes
    name = "Ben"
    designation = "Sales Executive"
    sales_made_this_week = 5

    # Public instance method
    def has_achieved_target(self) -> str:
        if self.sales_made_this_week >= 5:
            return "Target has been achieved!"
        return "Target has not been achieved!"


employee_one = Employee()
print(employee_one.name)
print(employee_one.has_achieved_target())
