const API_URL = 'http://127.0.0.1:8000/api/users/';

const HEADERS = {
    headers: {
        "Content-type": "multipart/form-data",
    }
}


class AuthService {
    async login(axios, user) {

      console.log(axios)  
      return axios
        .post(API_URL + 'login/', user, HEADERS)
        .then(response => {
          if (response.data.accessToken) {
            localStorage.setItem('user', JSON.stringify(response.data));
          }
          return response.data;
        });
    }
  
    logout() {
      localStorage.removeItem('user');
    }
  
    async register(user) {
      return this.axios.post(API_URL + 'register/', user);
    }
}
  
export default new AuthService();