import axios from 'axios';
const API = axios.create({ baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000' });
API.interceptors.request.use(cfg => {
  const token = localStorage.getItem('token');
  if (token) cfg.headers.Authorization = `Bearer ${token}`;
  return cfg;
});
API.interceptors.response.use(
  res => res,
  err => {
    const url = err.config?.url || '';
    const isAuthAttempt = url.includes('/auth/login') || url.includes('/auth/register');
    if (err.response?.status === 401 && !isAuthAttempt) {
      localStorage.removeItem('token');
      if (!window.location.pathname.startsWith('/login')) {
        window.location.href = '/login';
      }
      return new Promise(() => {});
    }
    return Promise.reject(err);
  }
);
export default API;