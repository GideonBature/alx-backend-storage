-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users SET average_score = (SELECT SUM(score * weight) / SUM(weight) FROM corrections WHERE user_id = users.id) WHERE id IN (SELECT user_id FROM corrections);
END$$
DELIMITER ;
