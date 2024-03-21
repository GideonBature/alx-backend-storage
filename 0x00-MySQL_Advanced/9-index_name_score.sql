-- script that creates an index idx_name_first on the table names
-- and the first letter of name and the score.
-- Add a generated column to store the first letter of the name
ALTER TABLE names
ADD COLUMN first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column and score
CREATE INDEX idx_name_first_score ON names(first_letter, score);
