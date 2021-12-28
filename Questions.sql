/*Which position pays the most per state?*/

SELECT t.state,p.position,sub.max_salary
FROM (
	SELECT p.id id,p.position,s.amount AS max_salary,
	ROW_NUMBER() OVER (PARTITION BY t.state ORDER BY s.amount DESC) AS rn
	FROM players p
	JOIN salary s
	ON p.id = s.id_player
	JOIN teams t
	ON t.id = p.team_id
)AS sub 
JOIN players p 
ON p.id = sub.id
JOIN teams t
ON t.id = p.team_id
AND sub.rn = 1;

/*Average, minimum and maximum salary by height?*/

SELECT DISTINCT p.height height, 
	AVG(s.amount::NUMERIC) OVER salary_by_height AS avg_salary,
	MIN(s.amount) OVER salary_by_height AS min_salary,
	MAX(s.amount) OVER salary_by_height AS max_salary
FROM players p
JOIN salary s
ON s.id_player = p.id
WINDOW salary_by_height AS (PARTITION BY p.height ORDER BY p.height DESC)
ORDER BY 1 DESC;

