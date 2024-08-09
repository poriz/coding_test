SELECT 
    CASE 
    WHEN (A = B AND A=C AND B=C) THEN 'Equilateral' 
    WHEN ((A = B OR A=C OR B=C) AND ((A + B) > C)) THEN 'Isosceles' 
    WHEN ((A <> B AND A<>C AND B<>C) AND ((A + B) > C)) THEN 'Scalene' 
    WHEN ((A + B) <= C) THEN 'Not A Triangle' END 
FROM triangles;