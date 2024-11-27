import axios from 'axios';

const api = axios.create({
    baseURL: 'http://ec2-3-87-211-227.compute-1.amazonaws.com/api',
});

export default api;

export const getData = async (token) => {
    try {
      const response = await fetch(`${apiUrl}/api/endpoint/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  };
  
