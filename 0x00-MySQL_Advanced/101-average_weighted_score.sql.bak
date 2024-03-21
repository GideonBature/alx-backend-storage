-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary table to hold weighted scores
    CREATE TEMPORARY TABLE IF NOT EXISTS WeightedScores (
        user_id INT NOT NULL,
        weighted_score FLOAT DEFAULT 0
    );

    -- Calculate weighted scores and insert into the temporary table
    INSERT INTO WeightedScores (user_id, weighted_score)
    SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight)
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    GROUP BY c.user_id;

    -- Update the users table with the calculated average weighted scores
    UPDATE users u
    JOIN WeightedScores ws ON u.id = ws.user_id
    SET u.average_score = ws.weighted_score;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS WeightedScores;
END$$

DELIMITER ;
