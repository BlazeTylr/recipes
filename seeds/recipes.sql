-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS rrecipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name text,
  cooking_time int,
  rating int
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Beef Stew', 120, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Veg Burrito', 30, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pancake', 40, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Mixed veg', 120, 3);