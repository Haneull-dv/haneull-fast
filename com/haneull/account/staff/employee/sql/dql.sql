-- 🔍 모든 사용자 조회
SELECT * FROM member;

-- 🔍 특정 사용자 조회 (이름이 'Alice'인 경우)
SELECT * FROM member WHERE name = 'Alice';

-- 🔍 특정 이메일로 사용자 조회
SELECT * FROM member WHERE email = 'alice@example.com';

-- 🔍 가장 최근 가입한 사용자 3명 조회 (user_id 기준)
SELECT * FROM member ORDER BY user_id DESC LIMIT 3;
