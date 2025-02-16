from __future__ import annotations
import sys
from option import Result, Ok, Err
import textwrap
from pydantic import BaseModel, Field
from frontend.helpers import styling

if sys.version_info >= (3, 11):
    from typing import Self, TYPE_CHECKING
else:
    from typing_extensions import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from .employee import Employee


class Payroll(BaseModel):
    """Monthly payroll for an employee."""

    salary: int = Field(default_factory=int)
    bonus: int = Field(default_factory=int)
    tax: int = Field(default_factory=int)
    punish: int = Field(default_factory=int)
    total: int = Field(default_factory=int)

    def set_salary(self, _salary: str) -> Result[Self, str]:
        salary = int(_salary)
        self.salary = salary
        self.calculate_total()
        return Ok(self) if salary >= 0 else Err("Salary cannot be negative.")

    def set_bonus(self, _bonus: str) -> Result[Self, str]:
        bonus = int(_bonus)
        self.bonus = bonus
        self.calculate_total()
        return Ok(self) if bonus >= 0 else Err("Bonus cannot be negative.")

    def set_tax(self, _tax: str) -> Result[Self, str]:
        tax = int(_tax)
        self.tax = tax
        self.calculate_total()
        return Ok(self) if tax >= 0 else Err("Tax cannot be negative.")

    def calculate_bonus(self, employees: list[Employee]) -> None:
        """Calculate bonus for each employee based on their sales count."""
        bonus_budget = 100  # temporary value for now
        num_employees = len(employees)

        top_10 = int(num_employees * 0.1)
        middle_80 = int(num_employees * 0.8)

        employees.sort(key=lambda employee: employee.performance.sales_count, reverse=True)

        for i in range(top_10):
            employees[i].payroll.set_bonus(str(bonus_budget * 0.5 / top_10))
        for i in range(top_10, top_10 + middle_80):
            employees[i].payroll.set_bonus(str(bonus_budget * 0.5 / middle_80))
        for i in range(top_10 + middle_80, num_employees):
            employees[i].payroll.set_bonus(str(0))
        return None

    def set_punish(self, _punish: str) -> Result[Self, str]:
        punish = int(_punish)
        self.punish = punish
        self.calculate_total()
        return Ok(self) if punish >= 0 else Err("Punish cannot be negative.")

    def calculate_total(self) -> Self:
        self.total = self.salary + self.bonus - self.tax - self.punish
        return self

    def __str__(self) -> str:
        self.calculate_total()
        return textwrap.dedent(
            f"""\
            {styling('Salary', self.salary)}\
            {styling('Bonus', self.bonus)}\
            {styling('Tax', self.tax)}\
            {styling('Punish', self.punish)}\
            {styling('Total', self.total)}\
        """
        )

    class Config:
        arbitrary_types_allowed = True
