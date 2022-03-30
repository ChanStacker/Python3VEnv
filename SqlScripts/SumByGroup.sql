;with expenses as
(
	select * from MonthlyCredit where Amount > 0
),
expensesByGroup as
(
select Description, SUM(Amount) as SumTotal from expenses 
group by Description 
)
select SUM(SumTotal) from expensesByGroup where Description like '%Tesco%'


;with expenses as
(
	select * from MonthlyCredit where Amount > 0
),
expensesByGroup as
(
	select *, SUM(Amount) OVER (Partition by Description) as SumTotal from expenses expe
	left join [dbo].[ExpenseCategories] expec on expe.Description = expec.ExpenseDescription
)
select Category, SUM(Amount) from expensesByGroup group by Category

