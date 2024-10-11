CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      WITH CTE AS (
        SELECT salary, row_number() over(ORDER BY salary DESC) as rk
        FROM Employee
        GROUP BY salary
      )
      SELECT salary
      from CTE WHERE rk = N
  );
END