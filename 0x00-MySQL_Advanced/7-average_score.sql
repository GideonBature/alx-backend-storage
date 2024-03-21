-- script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the avarage score for a student. Note: An avarage score
-- can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
	DECLARE average FLOAT;
	SET average = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
	UPDATE users SET average_score = average WHERE id = user_id;
END$$
DELIMITER ;
