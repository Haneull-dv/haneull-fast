
CREATE TABLE members(
    user_id SERIAL PRIMARY KEY, 
    name VARCHAR(10) NOT NULL UNIQUE, 
    email VARCHAR(20)UNIQUE, 
    password VARCHAR(20) NOT NULL 
    
);