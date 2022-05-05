INSERT INTO
	sandbox(int32_value, bool_value, string_value)
VALUES
	(186108561, 0, 'Hello there?')

UPDATE
	sandbox
SET
	int16_value = 814,
	datetime_value = '2100-12-22 03:20:40'
WHERE
	id = 5

DELETE FROM sandbox WHERE id = 9