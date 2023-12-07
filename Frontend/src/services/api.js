import axios from 'axios';

let baseURL = import.meta.env.VITE_API_ENDPOINT
const instance = axios.create({
    baseURL: baseURL,
    headers: {
        'content-type': 'application/json'
    },

    credentials: "include",
    timeout: 30000,
    timeoutErrorMessage: 'Timeout'
})
export default instance
