-- 사용자 테이블 (users)
CREATE TABLE members(
    user_id SERIAL PRIMARY KEY,  -- 자동 증가 ID
    name VARCHAR(10) NOT NULL UNIQUE,  -- 사용자 이름 (중복 불가)
    email VARCHAR(20)UNIQUE,  -- 이메일 (중복 불가)
    password VARCHAR(20) NOT NULL  -- 비밀번호 해시
    
);