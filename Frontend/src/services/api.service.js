import http from './api'


class ApiService {
    getRequest = async (url, params, headers = { 'Content-Type': 'application/json' }) => {
        return await http.get(url, {
            params: params,
            headers: headers
        })
            .then(response => {
                if (response && response.status == 200) {
                    return response.data
                }
            })
            .catch(error => {
                if (error.response.status < 500) {
                    return error.response.data
                }
                console.log(error)
                return null
            });
    }

    postRequest = async (url, payload, headers = { 'Content-Type': 'application/json' }) => {
        return await http.post(url, payload, { headers: headers })
            .then(response => {
                if (response && response.status == 200) {
                    return response.data
                }
            })
            .catch(error => {
                if (error.response.status < 500) {
                    return error.response.data
                }
                console.log(error)
                return null
            });
    }
    getUser = () => {
        return this.getRequest(`/user`)
    }
    sendTelegram = (items) => {
        return this.postRequest(`/money`, items)
    }
}

export default new ApiService()
