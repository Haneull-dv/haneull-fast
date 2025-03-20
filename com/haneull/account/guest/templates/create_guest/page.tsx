// @ts-nocheck
'use client';

import React, { useEffect, useState } from 'react';

interface Customer {
  user_id: string;
  email: string;
  name: string;
  password: string;
}

export default function CustomerListPage() {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        setLoading(true);
        // API 엔드포인트 - 먼저 /api 접두사를 추가해 수정합니다
        const url = 'http://localhost:8000/api/customer/list';
        console.log('🔍 API 호출 URL:', url);
        
        const response = await fetch(url, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          console.error(`❌ API 응답 오류:`, response.status, response.statusText);
          throw new Error(`API 요청 실패: ${response.status}`);
        }

        const data = await response.json();
        console.log('✅ 받은 데이터:', data);
        setCustomers(Array.isArray(data) ? data : []);
        setError(null);
      } catch (err) {
        console.error('❌ 고객 데이터 로딩 오류:', err);
        setError('고객 데이터를 불러오는 중 오류가 발생했습니다.');
      } finally {
        setLoading(false);
      }
    };

    fetchCustomers();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">고객 목록</h1>
      
      {loading && <p className="text-gray-500">데이터를 불러오는 중...</p>}
      
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}
      
      {!loading && !error && customers.length === 0 && (
        <p className="text-gray-500">고객 데이터가 없습니다.</p>
      )}
      
      {customers.length > 0 && (
        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border border-gray-200">
            <thead>
              <tr className="bg-gray-100">
                <th className="py-2 px-4 border-b">사용자 ID</th>
                <th className="py-2 px-4 border-b">이메일</th>
                <th className="py-2 px-4 border-b">이름</th>
                <th className="py-2 px-4 border-b">비밀번호</th>
              </tr>
            </thead>
            <tbody>
              {customers.map((customer) => (
                <tr key={customer.user_id} className="hover:bg-gray-50">
                  <td className="py-2 px-4 border-b">{customer.user_id}</td>
                  <td className="py-2 px-4 border-b">{customer.email}</td>
                  <td className="py-2 px-4 border-b">{customer.name}</td>
                  <td className="py-2 px-4 border-b">{customer.password}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
} 