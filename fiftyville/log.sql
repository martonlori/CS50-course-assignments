-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Currently we know, that the mistery happened on July 28, 2023 on Humphrey Street
-- Need to start somewhere, starting at the crime scene reports. Extracting all data from 2023 July on Humphrey street, ordered by date
SELECT description, day FROM crime_scene_reports WHERE year = 2023 AND month = 'July' AND street = 'Humphrey Street' ORDER BY day ASC;
--Couldnt retrieve any info. Creating index
CREATE INDEX crime_day ON crime_scene_reports(year, month, day, street);
--trying again
SELECT description, day FROM crime_scene_reports WHERE year = 2023 AND month = 'July' AND street = 'Humphrey Street' ORDER BY day ASC;
-- Not yielding anything, trying checking how this table looks like
SELECT * FROM crime_scene_reports LIMIT 5;
--Got an example, now we see that months are numeric. Trying previous query, updating it accordingly
SELECT day, description FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Now lets check those interviews. (Updated findings.sql)
SELECT * FROM interviews LIMIT 5;
-- Lets check the interviews on that day, where bakery is mentioned
SELECT name, transcript FROM interviews WHERE year = 2023 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';
-- Updated findings. We now need to check security footage, ATM logs on Leggett Street and planes for July 29
SELECT * FROM bakery_security_logs LIMIT 50;
-- Checked how it looks, specifying
SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND minute BETWEEN 15 AND 26;
-- Updated findings, we know know a group of license plates, one belonging to the thief. Checking ATM logs
SELECT * FROM atm_transactions LIMIT 5;
-- Specify
SELECT account_number, amount FROM atm_transactions WHERE transaction_type = 'withdraw' AND atm_location = 'Leggett Street' AND year = 2023 AND month = 7 AND day = 28;
-- Update findings table with the account numbers of the thief. Lets check phone calls
SELECT * FROM phone_calls LIMIT 20;
-- Specify
SELECT caller, receiver FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 61;
-- Updated findings with possible caller-receiver combos
SELECT name FROM people WHERE phone_number IN ('(130) 555-0289', '(499) 555-9472', '(367) 555-5533', '(609) 555-5876', '(499) 555-9472', '(286) 555-6063', '(770) 555-1861', '(031) 555-6622', '(826) 555-1652', '(338) 555-6650') INTERSECT SELECT name FROM people WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8' , 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55');
-- Selected intersection of the known licencse plates and phone numbers. Now we know the 4 names possible for thief
-- Lets check the flights leaving from Fiftyville
SELECT * FROM flights LIMIT 20;
-- lets check the airports table too
SELECT * FROM airports LIMIT 15;
-- Select the flights going from Fiftyville with this id, sort them by date to find the earliest
SELECT id, year, hour, minute FROM flights WHERE origin_airport_id = 8 AND year = 2023 AND month = 7 AND day = 29 ORDER BY hour ASC;
-- we now see the earliest flights id going from Fiftyville, at 8.20. ID is 36
-- Check passengers on this flight
SELECT * FROM passengers LIMIT 50;
SELECT passport_number, seat FROM passengers WHERE flight_id = 36;
-- now we have the passport numbers of the passengers. Lets crosscheck with the people table - from the names we know
SELECT name, passport_number FROM people WHERE passport_number IN (8496433585, 9878712108, 1988161715, 8294398571, 1540955065, 5773159633, 1695452385, 7214083635) AND name IN ('Bruce', 'Diana', 'Kelsey', 'Sofia');
-- Updated findings sheet, we now have 3 names only
-- Lets get all the info from these ppl
SELECT * FROM people WHERE name IN ('Bruce', 'Kelsey', 'Sofia');
-- we can answer the destination city with our info
SELECT destination_airport_id FROM flights WHERE id = 36;
-- New York City
-- we can also find out the ban acc numbers of the possible thiefs
SELECT account_number, person_id FROM bank_accounts WHERE person_id IN (398010, 560886, 686048);
-- yielded only 1, whose person ID matches with Bruces
-- lets check with whom Bruce had a phone with after the robbery
SELECT receiver FROM phone_calls WHERE caller = '(367) 555-5533' AND year = 2023 AND month = 7 AND day = 28 AND duration < 61;
-- Lets check whose this number is, that should be the apprentice
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
